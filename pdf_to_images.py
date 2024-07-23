import os
import uuid
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_images(pdf_path):
    # Create a folder with a UUID
    folder_name = str(uuid.uuid4())
    os.makedirs(folder_name, exist_ok=True)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Process each page
    for i, image in enumerate(images):
        # Resize image to 1024px height, maintaining aspect ratio
        aspect_ratio = image.width / image.height
        new_width = int(1024 * aspect_ratio)
        resized_image = image.resize((new_width, 1024), Image.LANCZOS)

        # Save the image
        output_path = os.path.join(folder_name, f"p_{i:02d}.png")
        resized_image.save(output_path, "PNG")

    print(f"Images saved in folder: {folder_name}")

# Create a simple GUI for file selection
root = tk.Tk()
root.withdraw()  # Hide the main window

# Open file dialog
pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

if pdf_path:
    pdf_to_images(pdf_path)
else:
    print("No file selected.")