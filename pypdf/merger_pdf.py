import tkinter as tk
from tkinter import filedialog
from pypdf import PdfWriter

def select_pdfs():
    # Open a file dialog to select multiple PDF files
    pdf_files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")],
        defaultextension=".pdf"
    )
    return list(pdf_files)

def select_save_location():
    # Open a file dialog to select location and filename to save the merged PDF
    save_file = filedialog.asksaveasfilename(
        title="Save Merged PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return save_file

def merge_pdfs():
    # Initialize PdfWriter
    merger = PdfWriter()

    # Select PDFs
    pdf_files = select_pdfs()
    if not pdf_files:  # If no files are selected, return
        print("No files selected.")
        return

    # Collecting files to merge
    for pdf in pdf_files:
        merger.append(pdf)

    # Select save location
    save_location = select_save_location()
    if not save_location:  # If no save location is selected, return
        print("No save location selected.")
        return

    # Write the merged PDF to the selected location
    merger.write(save_location)
    merger.close()
    print(f"Merged PDF saved at {save_location}")

# Creating the main window
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Run the PDF merging function
    merge_pdfs()

    # Show success message
    tk.messagebox.showinfo("Success", "PDFs merged successfully!")