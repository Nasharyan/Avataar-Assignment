import argparse
from pathlib import Path
from PIL import Image
import torch
from diffusers import StableDiffusionInpaintPipeline
import cv2

# Configuration class
class CFG:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    image_gen_model_id = "stabilityai/stable-diffusion-2-1"
    image_gen_steps = 15
    image_gen_guidance_scale = 7.5

# Load the image generation model
image_gen_model = StableDiffusionInpaintPipeline.from_pretrained(
    CFG.image_gen_model_id,
    torch_dtype=torch.float16,
    revision="fp16"
).to(CFG.device)

# Function to overlay the object onto a generated background
def generate_image_with_object(object_image_path, text_prompt, output_image_path):
    # Load the object image (keep object unaltered)
    object_image = Image.open(object_image_path).convert("RGBA")

    # Generate a background based on the text prompt
    generated_background = image_gen_model(
        prompt=text_prompt,
        num_inference_steps=CFG.image_gen_steps,
        guidance_scale=CFG.image_gen_guidance_scale
    ).images[0]

    # Ensure the generated background has an alpha channel for transparency
    generated_background = generated_background.convert("RGBA")

    # Resize object image to fit the background more naturally (optional, can adjust)
    object_image = object_image.resize((generated_background.width // 3, generated_background.height // 3))

    # Paste the object onto the background, maintaining transparency
    # Adjust position as needed (centered here)
    position = (
        (generated_background.width - object_image.width) // 2,
        (generated_background.height - object_image.height) // 2
    )
    combined_image = Image.alpha_composite(generated_background, Image.new("RGBA", generated_background.size))
    combined_image.paste(object_image, position, object_image)

    # Save the resulting image
    combined_image = combined_image.convert("RGB")  # Convert back to RGB for saving
    combined_image.save(output_image_path)

    print(f"Generated image saved at {output_image_path}")

# Command line argument parser
def parse_args():
    parser = argparse.ArgumentParser(description="Generate an image with an object and a text-conditioned scene.")
    parser.add_argument("--image", type=str, required=True, help="Path to the object image (e.g. ./example.jpg)")
    parser.add_argument("--text-prompt", type=str, required=True, help="Text prompt for the scene (e.g. 'product in a kitchen')")
    parser.add_argument("--output", type=str, required=True, help="Path to save the generated image (e.g. ./generated.png)")
    return parser.parse_args()

# Main function
if __name__ == "__main__":
    args = parse_args()
    generate_image_with_object(args.image, args["text_prompt"], args["output"])