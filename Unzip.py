import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to extract the ZIP file
def extract_zip():
    # Open file dialog to select a ZIP file
    zip_file = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    if not zip_file:
        return  # If no file is selected, return

    # Ask where to extract the contents
    extract_to = filedialog.askdirectory()
    if not extract_to:
        return  # If no folder is selected, return

    try:
        # Open the ZIP file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            # Show success message
            messagebox.showinfo("Success", f"Files extracted to: {extract_to}")
    except Exception as e:
        # Handle errors like corrupt zip files
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI window
root = tk.Tk()
root.title("Simple Zip Extractor")

# Set the window size
root.geometry("300x150")

# Add a button to trigger the extraction
extract_button = tk.Button(root, text="Extract ZIP", command=extract_zip, width=20, height=2)
extract_button.pack(pady=50)

# Run the Tkinter event loop
root.mainloop()
