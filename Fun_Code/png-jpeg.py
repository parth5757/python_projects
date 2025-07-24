from PIL import Image
import os

def convert_png_to_jpeg(input_path, output_path):
    with Image.open(input_path) as img:
        # Convert image to RGB (JPEG doesn't support transparency)
        rgb_image = img.convert("RGB")
        rgb_image.save(output_path, "JPEG")
        print(f"Converted: {input_path} -> {output_path}")

# Example usage:
convert_png_to_jpeg("converted.png", "output_image.jpg")
