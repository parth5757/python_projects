from PIL import Image
import os
def compress_image(input_path, output_path, quality=30, max_size=(800,800)):
    # open the image
    img = Image.open(input_path)
    # convert RGB into PNG
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    # Resize the image
    img.thumbnail(max_size)
    # save to lower quality
    img.save(output_path, optimize=True, quality=quality)
    print(f"image compressed at the {output_path}")

input_path = "compressed_photo.jpg"
output_path = "Passport_Size_Photo.jpg"
compress_image(input_path, output_path)


# still more compressed image
input_path = "compressed_photo.jpg"
output_path = "Passport_Size_Picture.jpg"
compress_image(input_path, output_path, quality=20)