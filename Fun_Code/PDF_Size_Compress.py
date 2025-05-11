import fitz  # PyMuPDF
from PIL import Image
import io
import tkinter as tk
from tkinter import filedialog, messagebox

def compress_pdf(input_path, output_path, img_quality=30):
    try:
        doc = fitz.open(input_path)
        for page in doc:
            images = page.get_images(full=True)
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

                # Compress image
                compressed_io = io.BytesIO()
                image.save(compressed_io, format="JPEG", quality=img_quality)
                compressed_bytes = compressed_io.getvalue()

                # Replace original image stream with compressed one
                doc.update_stream(xref, compressed_bytes)

        doc.save(output_path, garbage=4, deflate=True, clean=True)
        doc.close()

    except Exception as e:
        raise RuntimeError(f"Compression failed: {e}")

def select_and_compress():
    input_path = filedialog.askopenfilename(title="Select PDF to Compress", filetypes=[("PDF Files", "*.pdf")])
    if not input_path:
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Compressed PDF As", filetypes=[("PDF Files", "*.pdf")])
    if not output_path:
        return

    try:
        compress_pdf(input_path, output_path)
        messagebox.showinfo("Success", f"Compressed PDF saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("PDF Compressor")
root.geometry("300x150")

btn = tk.Button(root, text="Upload & Compress PDF", command=select_and_compress, height=2, width=25)
btn.pack(pady=40)

root.mainloop()