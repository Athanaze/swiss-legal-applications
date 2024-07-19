import os
import torch
from torch import nn
from torchvision import transforms
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline
import uuid

# Set up the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
N_VARIATIONS = 50

# Load the Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

# Set up image transformations
preprocess = transforms.Compose([
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5]),
])

# Set up the input and output directories
input_dir = "portrait_images"
output_dir = "squeezed_portrait_variations"
os.makedirs(output_dir, exist_ok=True)

# Define the target aspect ratio
target_ratio = 7 / 9

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        # Load and preprocess the image
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path).convert("RGB")
        image = preprocess(image).unsqueeze(0).to(device)
        # Generate N_VARIATIONS
        for _ in range(N_VARIATIONS):
            import time

            # Start timing
            start_time = time.time()

            # Generate a variation
            with torch.no_grad():
                variation = pipe(prompt="a passport portrait", image=image, strength=0.75, guidance_scale=7.5).images[0]

            # Squeeze the generated image
            width, height = variation.size
            new_width = int(height * target_ratio)
            squeezed_variation = variation.resize((new_width, height), Image.LANCZOS)

            # Save the squeezed variation
            output_path = os.path.join(output_dir, f"squeezed_variation_{uuid.uuid4()}.png")
            squeezed_variation.save(output_path)

            # End timing and print execution time
            end_time = time.time()
            exec_time = end_time - start_time
            print(f"Execution time for variation: {exec_time:.2f} seconds")
            print(f"Saved squeezed variation {output_path}")
        print(f"Generated and squeezed {N_VARIATIONS} variations for {filename}")

print("All variations generated and squeezed successfully!")