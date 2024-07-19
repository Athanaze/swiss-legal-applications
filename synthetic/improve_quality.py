import os
import cv2
import torch
from gfpgan import GFPGANer

# Set up GFPGAN model
model_path = 'experiments/pretrained_models/GFPGANv1.4.pth'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
restorer = GFPGANer(model_path=model_path, upscale=2, arch='clean', channel_multiplier=2, bg_upsampler=None)

# Set up input and output folders
input_folder = 'squeezed_portrait_variations'
output_folder = 'output_folder'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Read the image
        img = cv2.imread(input_path)
        
        # Restore the face
        _, _, restored_img = restorer.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
        
        # Define constant for the longest edge
        LONGEST_EDGE = 256

        # Resize the image to have the longest edge of LONGEST_EDGE pixels
        height, width = restored_img.shape[:2]
        if height > width:
            new_height = LONGEST_EDGE
            new_width = int(width * (LONGEST_EDGE / height))
        else:
            new_width = LONGEST_EDGE
            new_height = int(height * (LONGEST_EDGE / width))
        
        restored_img = cv2.resize(restored_img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        # Save the restored image
        cv2.imwrite(output_path, restored_img)
        
        print(f"Processed: {filename}")

print("All images processed.")