# pip install pillow-heif
from PIL import Image
import pillow_heif

# Register HEIF support to Pillow
pillow_heif.register_heif_opener()
def convert_heif_png(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path, format="png") # for jpg use jpeg at format and last output path use.jpg
    print(f"Converted {input_path} to {output_path}")

# Example usage
convert_heif_png(input_path="20250709_165421.heic", output_path="converted.png")