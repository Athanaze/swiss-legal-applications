from rembg import remove
from PIL import Image
import sys
import os


def remove_background(input_path, output_path):
    # Open the input image
    input_image = Image.open(input_path)
    
    # Remove the background
    output_image = remove(input_image)
    
    # Save the result
    output_image.save(output_path)

if __name__ == "__main__":
    
    # Define input and output folders
    input_folder = "selection"
    output_folder = "alpha_bg"

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop over all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # Remove background for each image
            remove_background(input_path, output_path)
            print(f"Processed {filename}")

    print("All images processed.")
