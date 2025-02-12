# Document Text Extractor

This tool extracts text content from PDF documents (both text-based and scanned) and images, combining them into a single text file. It's particularly optimized for French documents and uses multiple OCR approaches to ensure the best possible text extraction.

## Features

- Handles text-based PDFs using direct text extraction
- Processes scanned PDFs and images using OCR
- Supports French and English text recognition
- Combines multiple OCR approaches for better accuracy
- Creates a single output file with all extracted text

## Installation

Choose your operating system below for specific installation instructions.

### Ubuntu Installation

1. Install system dependencies:
```bash
# Update package list
sudo apt update

# Install Python 3 and pip if not already installed
sudo apt install -y python3 python3-pip

# Install Tesseract OCR and French language pack
sudo apt install -y tesseract-ocr tesseract-ocr-fra

# Install Poppler tools (required for PDF processing)
sudo apt install -y poppler-utils
```

2. Create and activate a virtual environment (recommended):
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

3. Install Python dependencies:
```bash
# Install required Python packages
pip install -r requirements.txt
```

### Arch Linux Installation

1. Install system dependencies:
```bash
# Install Tesseract OCR and French language pack
sudo pacman -S tesseract tesseract-data-fra

# Install Poppler (required for PDF processing)
sudo pacman -S poppler
```

2. Create and activate a virtual environment (recommended):
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate
```

3. Install Python dependencies:
```bash
# Install required Python packages
pip install -r requirements.txt
```

## Usage

1. Activate your virtual environment if you haven't already:
```bash
source venv/bin/activate
```

2. Run the script:
```bash
python build_full_content_text.py /path/to/input/folder [--output output.txt]
```

For example:
```bash
python build_full_content_text.py documents/ --output extracted_text.txt
```

The script will:
- Process all PDFs and images in the input folder recursively
- Extract text from each file
- Create a single output file containing all extracted text
- Show progress through logging messages

## Output Format

The output file will contain entries in the following format:

```
/full/path/to/file1:

[Extracted text content from file1]

----------------------------------------

/full/path/to/file2:

[Extracted text content from file2]

----------------------------------------
```

## Troubleshooting

1. If you get a "tesseract not found" error:
   - Make sure Tesseract is properly installed
   - Try running `tesseract --version` to verify the installation

2. If PDF processing fails:
   - Verify that Poppler is properly installed
   - Try running `pdftoppm -v` to check the Poppler installation

3. If text recognition is poor:
   - Make sure the French language pack is properly installed
   - Check if the document is clearly scanned
   - Try adjusting the image's contrast and brightness before processing

## Dependencies

### System Dependencies
- Tesseract OCR
- Tesseract French language pack
- Poppler utils

### Python Dependencies
- PyPDF2: PDF processing
- pytesseract: OCR interface
- pdf2image: PDF to image conversion
- Pillow: Image processing
- torch: Deep learning support
- transformers: TrOCR model
- numpy: Numerical processing

## License

This project is open source and available under the MIT License.
