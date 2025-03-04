import sys
import os
import json
import warnings
import subprocess
import tempfile
import shutil
import traceback
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, 
    QProgressBar, QFileDialog, QLabel, QTextEdit, QHBoxLayout, QFrame, QScrollArea
)
from PyQt6.QtCore import Qt, QTimer, QRect, QPropertyAnimation
from PyQt6.QtGui import QFont, QPainter, QPen, QColor
import torch
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from plyer import notification
try:
    import pynvml
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False
try:
    from win10toast import ToastNotifier
    WINDOWS_TOAST = True
except ImportError:
    WINDOWS_TOAST = False

# Constants
PHI_MAX_TOKENS = 1600
EMBEDDING_MAX_CHARS = 8192 * 4
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
PROGRESS_STEPS_PER_FILE = 2  # OCR, Extract (Phi optional)
SYSTEM_PROMPT = """
1. Comprenez le cas juridique.
2. Identifiez personnes et entreprises mentionnées.
3. Attribuez-leur des noms fictifs simples.
4. Reformulez le cas avec ces noms, en gardant les aspects juridiques importants.
5. Assurez une réponse claire, organisée, basée uniquement sur le texte fourni, sans ajouts externes.
6. Le but est d'avoir une réponse qui permet de comprendre toute l'affaire juridique sans révéler les noms des personnes, des addresses et des entreprises (on ne veut pas les "dox")
"""

warnings.filterwarnings("ignore", category=UserWarning)

class CustomToggleSwitch(QWidget):
    def __init__(self, label, default_state=False):
        super().__init__()
        self.state = default_state
        self.label = label
        self.setFixedSize(120, 60)  # Increased height for better padding
        self.setStyleSheet("background-color: transparent;")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(QColor("#333333"), 2)
        painter.setPen(pen)

        # Background
        bg_color = QColor("#50C878" if self.state else "#E0E0E0")
        painter.setBrush(bg_color)
        painter.drawRoundedRect(10, 10, 100, 30, 15, 15)

        # Knob
        knob_color = QColor("#FFFFFF")
        painter.setBrush(knob_color)
        knob_x = 80 if self.state else 20
        painter.drawEllipse(knob_x, 15, 20, 20)

        # Label (moved down for better spacing)
        painter.setFont(QFont("Arial", 12))
        painter.drawText(QRect(0, 40, 120, 20), Qt.AlignmentFlag.AlignCenter, self.label)

    def mousePressEvent(self, event):
        self.state = not self.state
        self.update()

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(200)
        self.fig, self.ax = plt.subplots(figsize=(5, 2))
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)  # Add padding around plot
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Update every second
        if GPU_AVAILABLE:
            pynvml.nvmlInit()

    def update_plot(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        gpu, vram = 0, 0
        if GPU_AVAILABLE and torch.cuda.is_available():
            gpu = pynvml.nvmlDeviceGetUtilizationRates(pynvml.nvmlDeviceGetHandleByIndex(0)).gpu
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(pynvml.nvmlDeviceGetHandleByIndex(0))
            vram = (memory_info.used / memory_info.total) * 100

        self.ax.clear()
        bars = self.ax.bar(['CPU', 'RAM', 'GPU', 'VRAM'], [cpu, ram, gpu, vram], color=['#4A90E2', '#50C878', '#FF6F61', '#FFD700'])
        self.ax.set_ylim(0, 100)
        self.ax.set_title("System Utilization (%)")
        for bar in bars:
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width()/2, height, f'{height:.1f}', ha='center', va='bottom')
        self.canvas.draw()

class ResultOverlay(QWidget):
    def __init__(self, parent, success=True):
        super().__init__(parent)
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 50);")  # Semi-transparent black overlay
        self.success = success
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(f"""
            font-size: 48px; font-weight: bold; color: {'#50C878' if success else '#FF6F61'};
            margin-top: 200px; font-family: Arial;
        """)
        self.label.setText("✔ Success!" if success else "✖ Error!")
        self.setVisible(False)

        # Animation for fade-in/fade-out
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.show()

    def show(self):
        self.setVisible(True)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()
        QTimer.singleShot(3000, self.hide)  # Auto-hide after 3 seconds

    def hide(self):
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.finished.connect(lambda: self.setVisible(False))
        self.animation.start()

    def mousePressEvent(self, event):
        self.hide()  # Dismiss on click

class DocumentEmbeddingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vectorizer")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setStyleSheet("""
            QMainWindow { background-color: #F5F6F5; }
            QLabel { color: #333333; font-family: Arial; }
            QPushButton {
                background-color: #4A90E2; color: #FFFFFF; border: none;
                padding: 12px 24px; font-size: 16px; border-radius: 8px;
            }
            QPushButton:hover { background-color: #357ABD; }
            QPushButton:disabled { background-color: #A0A0A0; }
            QProgressBar {
                background-color: #E0E0E0; color: #333333; border: none;
                text-align: center; font-size: 14px; border-radius: 4px;
                height: 20px;
            }
            QProgressBar::chunk { background-color: #50C878; border-radius: 4px; }
            QTextEdit {
                background-color: #FFFFFF; color: #333333;
                border: 1px solid #CCCCCC; border-radius: 4px;
                padding: 10px; font-family: Consolas; font-size: 12px;
            }
            QFrame { border: 1px solid #CCCCCC; border-radius: 4px; margin: 5px; }
            QScrollArea { border: none; }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(20, 20, 20, 20)  # Global padding for the window
        self.layout.setSpacing(15)  # Spacing between widgets

        self.header_label = QLabel("Vectorizer", self)
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("font-size: 28px; font-weight: bold; margin: 10px 0; color: #4A90E2;")
        self.layout.addWidget(self.header_label)

        controls_layout = QHBoxLayout()
        controls_layout.setContentsMargins(0, 0, 0, 15)  # Padding below controls
        controls_layout.setSpacing(20)  # Space between buttons and toggles
        self.select_button = QPushButton("Select Folder", self)
        self.select_button.clicked.connect(self.select_folder)
        controls_layout.addWidget(self.select_button, stretch=1)  # Stretch to take more space

        self.text_switch = CustomToggleSwitch("Include Text", True)
        controls_layout.addWidget(self.text_switch)

        self.phi_switch = CustomToggleSwitch("Use Phi-4", False)
        controls_layout.addWidget(self.phi_switch)
        self.layout.addLayout(controls_layout)

        self.loading_label = QLabel("Processing...", self)
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loading_label.setStyleSheet("margin: 10px 0;")
        self.loading_label.hide()
        self.layout.addWidget(self.loading_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("margin: 10px 0;")
        self.layout.addWidget(self.progress_bar)

        self.model_progress_bar = QProgressBar(self)
        self.model_progress_bar.setMinimum(0)
        self.model_progress_bar.setMaximum(100)
        self.model_progress_bar.setTextVisible(True)
        self.model_progress_bar.setStyleSheet("margin: 10px 0;")
        self.model_progress_bar.hide()
        self.layout.addWidget(self.model_progress_bar)

        split_layout = QHBoxLayout()
        split_layout.setContentsMargins(0, 0, 0, 15)  # Padding below split layout
        split_layout.setSpacing(20)  # Space between log areas

        log_frame = QFrame()
        log_layout = QVBoxLayout(log_frame)
        log_layout.setContentsMargins(10, 10, 10, 10)  # Padding inside log frame
        log_layout.setSpacing(5)
        log_layout.addWidget(QLabel("Status", self))
        self.status_log = QTextEdit(self)
        self.status_log.setReadOnly(True)
        log_layout.addWidget(self.status_log)
        split_layout.addWidget(log_frame, stretch=1)

        expert_frame = QFrame()
        expert_layout = QVBoxLayout(expert_frame)
        expert_layout.setContentsMargins(10, 10, 10, 10)  # Padding inside expert frame
        expert_layout.setSpacing(5)
        expert_layout.addWidget(QLabel("Expert Logs (Click to Expand)"))
        expert_scroll = QScrollArea()
        expert_scroll.setWidgetResizable(True)
        self.expert_log = QTextEdit(self)
        self.expert_log.setReadOnly(True)
        expert_scroll.setWidget(self.expert_log)
        expert_layout.addWidget(expert_scroll)
        split_layout.addWidget(expert_frame, stretch=1)
        self.layout.addLayout(split_layout)

        self.system_monitor = SystemMonitor()
        self.system_monitor.setStyleSheet("margin: 10px 0; border: 1px solid #CCCCCC; border-radius: 4px;")
        self.layout.addWidget(self.system_monitor)

        self.device = self.detect_device()
        self.status_log.append(f"Using device: {self.device}")
        self.expert_log.append(f"CUDA available: {torch.cuda.is_available()}")
        if self.device == "cuda":
            self.expert_log.append(f"GPU: {torch.cuda.get_device_name(0)}")
        self.expert_log.append("vLLM server at http://localhost:8000/v1")

        self.vllm_client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
        self.embedding_model = None
        self.loading_dots = 0
        self.loading_timer = QTimer(self)
        self.loading_timer.timeout.connect(self.update_loading_animation)
        self.temp_dir = tempfile.mkdtemp()

    def detect_device(self):
        if torch.cuda.is_available():
            try:
                torch.cuda.current_device()
                return "cuda"
            except Exception as e:
                self.expert_log.append(f"CUDA detection failed: {str(e)}")
                return "cpu"
        return "cpu"

    def update_loading_animation(self):
        self.loading_dots = (self.loading_dots + 1) % 4
        self.loading_label.setText("Processing" + "." * self.loading_dots)

    def select_folder(self):
        self.status_log.append("Select a folder to process")
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder:
            self.status_log.append(f"Processing folder: {folder}")
            self.select_button.setEnabled(False)
            self.loading_label.show()
            self.loading_timer.start(500)
            QTimer.singleShot(100, lambda: self.process_documents(folder))
        else:
            self.status_log.append("No folder selected")

    def notify(self, title, message):
        if WINDOWS_TOAST and sys.platform == "win32":
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True)
        else:
            notification.notify(title=title, message=message, timeout=5)

    def run_ocrmypdf(self, input_path: str, output_path: str):
        self.status_log.append(f"OCR on {os.path.basename(input_path)}")
        try:
            result = subprocess.run(
                ['ocrmypdf', '--force-ocr', input_path, output_path],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            self.expert_log.append(f"OCR stdout: {result.stdout}")
            if result.stderr:
                self.expert_log.append(f"OCR stderr: {result.stderr}")
        except Exception as e:
            self.status_log.append("OCR failed")
            self.expert_log.append(f"OCR error: {str(e)}")
            raise

    def extract_text(self, file_path: str) -> str:
        self.status_log.append(f"Extracting text from {os.path.basename(file_path)}")
        try:
            reader = PdfReader(file_path)
            text = "".join(page.extract_text() or "" for page in reader.pages).strip()
            self.expert_log.append(f"Extracted {len(text)} chars")
            return text
        except Exception as e:
            self.status_log.append("Text extraction failed")
            self.expert_log.append(f"Extraction error: {str(e)}")
            raise

    def load_embedding_model(self):
        self.status_log.append("Loading embedding model...")
        self.model_progress_bar.show()
        self.model_progress_bar.setValue(0)
        QApplication.processEvents()
        try:
            for i in range(1, 101):
                QTimer.singleShot(i * 50, lambda v=i: self.model_progress_bar.setValue(v))
                QApplication.processEvents()
            self.embedding_model = SentenceTransformer('BAAI/bge-m3').to(self.device)
            self.status_log.append(f"Model loaded on {self.device}")
            self.notify("Vectorizer", "Embedding model loaded successfully!")
        except Exception as e:
            self.status_log.append("Model loading failed")
            self.expert_log.append(f"Load error: {str(e)}")
            raise
        finally:
            self.model_progress_bar.hide()

    def unload_embedding_model(self):
        if self.embedding_model:
            del self.embedding_model
            self.embedding_model = None
            if self.device == "cuda":
                torch.cuda.empty_cache()
            self.status_log.append("Model unloaded")

    def process_text_phi(self, text: str) -> str:
        self.status_log.append("Anonymizing with Phi-4...")
        try:
            approx_tokens = len(text) // 4
            max_chunk_tokens = PHI_MAX_TOKENS - (len(SYSTEM_PROMPT) // 4) - 50
            words = text.split()
            processed_chunks = []
            current_chunk_words = []
            current_tokens = len(SYSTEM_PROMPT) // 4

            for word in words:
                word_tokens = len(word) // 4 + 1
                if current_tokens + word_tokens <= max_chunk_tokens:
                    current_chunk_words.append(word)
                    current_tokens += word_tokens
                else:
                    chunk_text = " ".join(current_chunk_words)
                    prompt = f"{SYSTEM_PROMPT}\n\nTexte à traiter:\n{chunk_text}"
                    response = self.vllm_client.completions.create(
                        model="microsoft/Phi-4-Mini-instruct",
                        prompt=prompt, max_tokens=PHI_MAX_TOKENS, temperature=0.7
                    )
                    processed_chunk = response.choices[0].text.strip().split("Texte à traiter:")[-1].strip()
                    processed_chunks.append(processed_chunk)
                    current_chunk_words = [word]
                    current_tokens = len(SYSTEM_PROMPT) // 4 + word_tokens

            if current_chunk_words:
                chunk_text = " ".join(current_chunk_words)
                prompt = f"{SYSTEM_PROMPT}\n\nTexte à traiter:\n{chunk_text}"
                response = self.vllm_client.completions.create(
                    model="microsoft/Phi-4-Mini-instruct",
                    prompt=prompt, max_tokens=PHI_MAX_TOKENS, temperature=0.7
                )
                processed_chunk = response.choices[0].text.strip().split("Texte à traiter:")[-1].strip()
                processed_chunks.append(processed_chunk)

            return " ".join(processed_chunks)
        except Exception as e:
            self.status_log.append("Phi-4 processing failed")
            self.expert_log.append(f"Phi error: {str(e)}")
            return text  # Fallback to original text

    def chunk_text(self, text: str) -> list:
        return [text[i:i + EMBEDDING_MAX_CHARS] for i in range(0, len(text), EMBEDDING_MAX_CHARS)] if text else []

    def generate_embedding(self, text: str) -> list:
        if not text:
            return []
        self.status_log.append("Generating embedding...")
        chunks = self.chunk_text(text)
        embeddings = self.embedding_model.encode(chunks, convert_to_tensor=True)
        return embeddings.mean(dim=0).cpu().tolist()

    def process_documents(self, folder: str):
        self.status_log.append("Starting processing...")
        results = {"files": {}, "full_collection": {}, "errors": []}
        pdf_files = [os.path.join(root, file) for root, _, files in os.walk(folder) for file in files if file.lower().endswith('.pdf')]
        total_files = len(pdf_files)

        if not total_files:
            self.status_log.append("No PDFs found")
            self.finish_processing(results, folder)
            return

        total_steps = total_files * PROGRESS_STEPS_PER_FILE + (total_files if self.phi_switch.state else 0) + total_files + 1
        self.progress_bar.setMaximum(total_steps)
        processed_steps = 0
        all_processed_texts = []

        try:
            intermediate_results = {}
            for pdf_file in pdf_files:
                ocr_output = os.path.join(self.temp_dir, f"{os.path.basename(pdf_file)}_ocr.pdf")
                self.run_ocrmypdf(pdf_file, ocr_output)
                processed_steps += 1
                self.progress_bar.setValue(processed_steps)

                text = self.extract_text(ocr_output)
                processed_steps += 1
                self.progress_bar.setValue(processed_steps)

                if text:
                    intermediate_results[pdf_file] = {"original_text": text}
                else:
                    results["errors"].append(f"No text from {pdf_file}")
                    results["files"][pdf_file] = {}

            if self.phi_switch.state:
                for pdf_file, data in intermediate_results.items():
                    data["processed_text"] = self.process_text_phi(data["original_text"])
                    processed_steps += 1
                    self.progress_bar.setValue(processed_steps)
                self.notify("Vectorizer", "Phi-4 anonymization completed!")
            else:
                for pdf_file, data in intermediate_results.items():
                    data["processed_text"] = data["original_text"]

            self.load_embedding_model()
            for pdf_file, data in intermediate_results.items():
                embedding = self.generate_embedding(data["processed_text"])
                processed_steps += 1
                self.progress_bar.setValue(processed_steps)
                file_data = {"embedding": embedding}
                if self.text_switch.state:
                    file_data["original_text"] = data["original_text"]
                    file_data["processed_text"] = data["processed_text"]
                results["files"][pdf_file] = file_data
                all_processed_texts.append(data["processed_text"])

            if all_processed_texts:
                full_text = " ".join(all_processed_texts)
                results["full_collection"]["embedding"] = self.generate_embedding(full_text)
                processed_steps += 1
                self.progress_bar.setValue(processed_steps)

            self.unload_embedding_model()
            self.finish_processing(results, folder)

        except Exception as e:
            self.status_log.append("Processing error occurred")
            self.expert_log.append(f"Error: {str(e)}\n{traceback.format_exc()}")
            self.finish_processing(results, folder)
            self.unload_embedding_model()

    def finish_processing(self, results: dict, folder: str):
        output_path = os.path.join(folder, "embeddings.json")
        success = len(results["errors"]) == 0
        try:
            with open(output_path, 'w') as f:
                json.dump(results, f, indent=4)
            self.status_log.append(f"Saved to {output_path}")
            self.notify("Vectorizer", f"Processing {'complete!' if success else 'failed with errors...'}")
        except Exception as e:
            self.status_log.append("Error saving results")
            self.expert_log.append(f"Save error: {str(e)}")
            success = False

        self.loading_timer.stop()
        self.loading_label.hide()
        self.select_button.setEnabled(True)
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        self.temp_dir = tempfile.mkdtemp()

        # Show overlay for success or error
        overlay = ResultOverlay(self, success=success)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DocumentEmbeddingApp()
    window.show()
    sys.exit(app.exec())
