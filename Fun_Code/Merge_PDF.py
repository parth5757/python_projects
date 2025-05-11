import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")

        self.file_list = []

        self.listbox = tk.Listbox(root, width=60, height=15)
        self.listbox.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add PDFs", command=self.add_pdfs).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Move Up", command=self.move_up).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Move Down", command=self.move_down).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Merge PDFs", command=self.merge_pdfs).grid(row=0, column=4, padx=5)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in files:
            if file not in self.file_list:
                self.file_list.append(file)
                self.listbox.insert(tk.END, file)

    def remove_selected(self):
        selected = self.listbox.curselection()
        for i in reversed(selected):
            self.file_list.pop(i)
            self.listbox.delete(i)

    def move_up(self):
        selected = self.listbox.curselection()
        for i in selected:
            if i == 0:
                continue
            self.file_list[i], self.file_list[i - 1] = self.file_list[i - 1], self.file_list[i]
            self.update_listbox()

    def move_down(self):
        selected = self.listbox.curselection()
        for i in reversed(selected):
            if i == len(self.file_list) - 1:
                continue
            self.file_list[i], self.file_list[i + 1] = self.file_list[i + 1], self.file_list[i]
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for file in self.file_list:
            self.listbox.insert(tk.END, file)

    def merge_pdfs(self):
        if not self.file_list:
            messagebox.showerror("Error", "No PDFs selected.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")])
        if not output_path:
            return

        merger = PdfMerger()
        for pdf in self.file_list:
            merger.append(pdf)

        merger.write(output_path)
        merger.close()

        messagebox.showinfo("Success", f"PDFs merged and saved as:\n{output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
