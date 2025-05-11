import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, END
from PIL import Image

class PNGtoPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("PNG to PDF Converter")
        self.png_files = []

        # Listbox to display selected files
        self.listbox = Listbox(root, selectmode=tk.SINGLE, width=60)
        self.listbox.pack(pady=10)

        # Buttons
        tk.Button(root, text="Upload PNGs", command=self.upload_files).pack()
        tk.Button(root, text="Move Up", command=self.move_up).pack()
        tk.Button(root, text="Move Down", command=self.move_down).pack()
        tk.Button(root, text="Convert & Save PDF", command=self.convert_to_pdf).pack()

    def upload_files(self):
        files = filedialog.askopenfilenames(filetypes=[("PNG Files", "*.png")])
        self.png_files = list(files)
        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, END)
        for f in self.png_files:
            self.listbox.insert(END, f)

    def move_up(self):
        idx = self.listbox.curselection()
        if idx and idx[0] > 0:
            self.png_files[idx[0]-1], self.png_files[idx[0]] = self.png_files[idx[0]], self.png_files[idx[0]-1]
            self.refresh_listbox()
            self.listbox.select_set(idx[0]-1)

    def move_down(self):
        idx = self.listbox.curselection()
        if idx and idx[0] < len(self.png_files) - 1:
            self.png_files[idx[0]+1], self.png_files[idx[0]] = self.png_files[idx[0]], self.png_files[idx[0]+1]
            self.refresh_listbox()
            self.listbox.select_set(idx[0]+1)

    def convert_to_pdf(self):
        if not self.png_files:
            messagebox.showwarning("No files", "Please upload PNG files first.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not save_path:
            return

        try:
            images = [Image.open(f).convert("RGB") for f in self.png_files]
            images[0].save(save_path, save_all=True, append_images=images[1:])
            messagebox.showinfo("Success", f"PDF saved at:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PNGtoPDFConverter(root)
    root.mainloop()
