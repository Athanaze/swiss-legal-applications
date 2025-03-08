import os
import subprocess
import tempfile
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from docx2pdf import convert as docx_convert
from pptxtopdf import convert as pptx_convert
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def process_file(input_path, output_path):
    """Process a single file: convert to PDF if needed, OCR it, and extract text."""
    ext = os.path.splitext(input_path)[1].lower()

    if ext == '.txt':
        # For plaintext files, extract text directly
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                text = f.read()
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"Error reading {input_path}: {e}")
        return
    elif ext in ['.pdf', '.docx', '.doc', '.pptx', '.ppt', '.jpg', '.jpeg', '.png', '.webp', '.gif']:
        # Handle PDFs directly; convert other types to PDF
        if ext == '.pdf':
            pdf_path = input_path
            need_to_delete = False
        else:
            # Create a temporary PDF file
            temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
            pdf_path = temp_pdf.name
            temp_pdf.close()
            need_to_delete = True
            try:
                if ext in ['.docx', '.doc']:
                    docx_convert(input_path, pdf_path)
                elif ext in ['.pptx', '.ppt']:
                    pptx_convert(input_path, pdf_path)
                elif ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif']:
                    image = Image.open(input_path)
                    # Convert image to RGB if necessary (e.g., for PNG with transparency)
                    if image.mode in ('RGBA', 'LA'):
                        image = image.convert('RGB')
                    image.save(pdf_path, 'PDF')
            except Exception as e:
                print(f"Error converting {input_path} to PDF: {e}")
                if need_to_delete:
                    os.remove(pdf_path)
                return

        # Run ocrmypdf to OCR the PDF
        temp_ocr_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        ocr_pdf_path = temp_ocr_pdf.name
        temp_ocr_pdf.close()
        try:
            # ocrmypdf preserves existing text by default, OCRs only when needed
            subprocess.run(['ocrmypdf', pdf_path, ocr_pdf_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running ocrmypdf on {pdf_path}: {e}")
            if need_to_delete:
                os.remove(pdf_path)
            os.remove(ocr_pdf_path)
            return

        # Extract text from the OCRed PDF
        try:
            text = extract_text_from_pdf(ocr_pdf_path)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"Error extracting text from {ocr_pdf_path}: {e}")

        # Clean up temporary files
        if need_to_delete:
            os.remove(pdf_path)
        os.remove(ocr_pdf_path)
    else:
        print(f"Unsupported file type: {input_path}")
        return

def process_folder(input_folder):
    """Recursively process all files in the input folder."""
    output_folder = os.path.join(input_folder, 'output')
    os.makedirs(output_folder, exist_ok=True)
    
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            input_path = os.path.join(root, file)
            rel_path = os.path.relpath(input_path, input_folder)
            output_dir = os.path.join(output_folder, os.path.dirname(rel_path))
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.txt')
            process_file(input_path, output_path)
    
    messagebox.showinfo("Done", "Processing completed.")

def select_folder():
    """Open a folder selection dialog and process the selected folder."""
    folder = filedialog.askdirectory()
    if folder:
        process_folder(folder)

if __name__ == "__main__":
    # Set up the Tkinter UI
    root = tk.Tk()
    root.title("File to Text Converter")
    button = tk.Button(root, text="Select Folder", command=select_folder)
    button.pack(pady=20)
    root.mainloop()
