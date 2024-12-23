import tkinter as tk
from tkinter import filedialog, messagebox
import os

def list_folders(path, indent=0, output_file=None, ignore_folders=None):
    try:
        items = os.listdir(path)
    except PermissionError:
        return

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if ignore_folders and item in ignore_folders:
                continue
            output_file.write('  ' * indent + f'[{item}]\n')
            list_folders(item_path, indent + 1, output_file, ignore_folders)
        else:
            output_file.write('  ' * indent + item + '\n')

def browse_folder():
    folder_path = filedialog.askdirectory(title="Select a folder to scan")
    if folder_path:
        folder_path_var.set(folder_path)

def browse_save_file():
    output_file_path = filedialog.asksaveasfilename(
        title="Save the folder structure as",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
    )
    if output_file_path:
        save_path_var.set(output_file_path)

def submit_action():
    folder_path = folder_path_var.get()
    output_file_path = save_path_var.get()
    ignore_folders_input = ignore_folders_entry.get()
    
    # Parse ignore folders input
    ignore_list = [folder.strip() for folder in ignore_folders_input.split(",")] if ignore_folders_input else []

    if not folder_path or not output_file_path:
        messagebox.showerror("Error", "Please select both the folder and the save file path.")
        return

    try:
        with open(output_file_path, "w") as output_file:
            output_file.write(f"Selected folder: {folder_path}\n")
            list_folders(folder_path, output_file=output_file, ignore_folders=ignore_list)
        messagebox.showinfo("Success", f"Folder structure saved to {output_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("Folder Structure Saver")
root.geometry("500x300")

# Add a label and button for folder selection
select_folder_label = tk.Label(root, text="Step 1: Select a folder to save structure", font=("Arial", 12))
select_folder_label.pack(pady=10)

folder_path_var = tk.StringVar()
select_folder_button = tk.Button(root, text="Browse Folder", font=("Arial", 10), command=browse_folder)
select_folder_button.pack(pady=5)

folder_path_display = tk.Label(root, textvariable=folder_path_var, font=("Arial", 10), fg="blue", wraplength=400)
folder_path_display.pack(pady=5)

# Add a label and entry for ignore folder names
ignore_folders_label = tk.Label(root, text="Step 2: Enter folder names to ignore (comma-separated)", font=("Arial", 12))
ignore_folders_label.pack(pady=10)

ignore_folders_entry = tk.Entry(root, font=("Arial", 10), width=40)
ignore_folders_entry.pack(pady=5)

# Add a label and button for save file selection
save_file_label = tk.Label(root, text="Step 3: Select save location for folder structure", font=("Arial", 12))
save_file_label.pack(pady=10)

save_path_var = tk.StringVar()
save_file_button = tk.Button(root, text="Browse Save Location", font=("Arial", 10), command=browse_save_file)
save_file_button.pack(pady=5)

save_path_display = tk.Label(root, textvariable=save_path_var, font=("Arial", 10), fg="blue", wraplength=400)
save_path_display.pack(pady=5)

# Add a submit button to start the action
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=submit_action)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
