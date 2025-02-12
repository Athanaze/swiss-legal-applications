import os
from pathlib import Path
import PyPDF2
import pytesseract
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter
import logging
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
import easyocr
import cv2
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentExtractor:
    def __init__(self):
        # Initialize OCR models
        self.processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
        self.model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
        if torch.cuda.is_available():
            self.model.to('cuda')
        
        # Initialize EasyOCR with French and English language support
        self.reader = easyocr.Reader(['fr', 'en'], gpu=torch.cuda.is_available())
        
        # Configure Tesseract to use French and English
        self.tesseract_config = r'--oem 3 --psm 6 -l fra+eng'

    def enhance_image_for_ocr(self, image):
        """Simple image enhancement for better OCR results"""
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image)

        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Increase contrast slightly
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.5)

        # Increase sharpness slightly
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(1.5)

        return image

    def extract_text_from_image(self, image):
        """Extract text from an image using multiple OCR engines"""
        # Enhance the image
        enhanced_image = self.enhance_image_for_ocr(image)
        
        # Try Tesseract with French config first
        tesseract_text = pytesseract.image_to_string(enhanced_image, lang='fra', config='--psm 6')
        if len(tesseract_text.strip()) > 50:
            return tesseract_text

        # If Tesseract didn't work well, try TrOCR
        try:
            pixel_values = self.processor(enhanced_image, return_tensors='pt').pixel_values
            if torch.cuda.is_available():
                pixel_values = pixel_values.to('cuda')
            generated_ids = self.model.generate(pixel_values)
            trocr_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
            
            # If TrOCR found more text, use it
            if len(trocr_text.strip()) > len(tesseract_text.strip()):
                return trocr_text
        except Exception as e:
            logger.warning(f"TrOCR failed: {str(e)}")

        return tesseract_text

    def extract_from_pdf(self, pdf_path):
        """Extract text from a PDF file, handling both text-based and scanned PDFs"""
        try:
            # First try to extract text directly
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page in reader.pages:
                    page_text = page.extract_text()
                    text += page_text + '\n'

                # If we got meaningful text, return it
                if len(text.strip()) > 100:
                    return text

            # If we didn't get meaningful text, treat it as a scanned PDF
            images = convert_from_path(pdf_path)
            text = ''
            for image in images:
                text += self.extract_text_from_image(image) + '\n'
            return text

        except Exception as e:
            logger.error(f"Error processing PDF {pdf_path}: {str(e)}")
            return f"[Error processing file: {str(e)}]"

    def extract_from_image(self, image_path):
        """Extract text from an image file"""
        try:
            with Image.open(image_path) as img:
                return self.extract_text_from_image(img)
        except Exception as e:
            logger.error(f"Error processing image {image_path}: {str(e)}")
            return f"[Error processing file: {str(e)}]"

def build_full_content_text(input_folder, output_file='full_content.txt'):
    """Process all files in the input folder and create a single text file with all content"""
    extractor = ContentExtractor()
    supported_extensions = {'.pdf', '.png', '.jpg', '.jpeg'}

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for root, _, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                extension = os.path.splitext(file)[1].lower()

                if extension not in supported_extensions:
                    continue

                logger.info(f"Processing: {file_path}")
                out_file.write(f"\n{file_path}:\n\n")

                try:
                    if extension == '.pdf':
                        content = extractor.extract_from_pdf(file_path)
                    else:  # Image files
                        content = extractor.extract_from_image(file_path)
                    
                    out_file.write(content)
                    out_file.write('\n' + '-'*80 + '\n')  # Separator between files

                except Exception as e:
                    logger.error(f"Error processing {file_path}: {str(e)}")
                    out_file.write(f"[Error processing file: {str(e)}]\n")

    logger.info(f"Content extraction complete. Output written to {output_file}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Extract text content from PDFs and images in a folder')
    parser.add_argument('input_folder', help='Input folder containing PDFs and images')
    parser.add_argument('--output', default='full_content.txt', help='Output text file path')
    args = parser.parse_args()

    build_full_content_text(args.input_folder, args.output)
