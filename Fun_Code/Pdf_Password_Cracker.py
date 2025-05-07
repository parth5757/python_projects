import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import time
def unlock_pdf(input_pdf_path, output_pdf_path, password):
    start = time.time()
    # Open the PDF file
    with open(input_pdf_path, "rb") as input_pdf_file:
        reader = PdfReader(input_pdf_file)

        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # Attempt to decrypt the PDF with the provided password
            if reader.decrypt(password):
                writer = PdfWriter()
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])

                # Write the decrypted content to a new PDF file
                with open(output_pdf_path, "wb") as output_pdf_file:
                    writer.write(output_pdf_file)
                print(f"Successfully unlocked the PDF and saved to {output_pdf_path}")
            else:
                print("Failed to decrypt the PDF. Incorrect password.")
        else:
            print("The PDF file is not encrypted.")
    end = time.time()
    print("The time of execution of above program is :", (end-start) * 10**3, "ms")
def browse_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    input_pdf_path = filedialog.askopenfilename(title="Select Encrypted PDF File", filetypes=[("PDF files", "*.pdf")])
    return input_pdf_path

def main():
    input_pdf_path = browse_file()
    if input_pdf_path:
        output_pdf_path = filedialog.asksaveasfilename(title="Save Unlocked PDF As", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_pdf_path:
            password = input("Enter the password for the PDF: ")
            unlock_pdf(input_pdf_path, output_pdf_path, password)
        else:
            print("No output file selected.")
    else:
        print("No input file selected.")

if __name__ == "__main__":
    main()