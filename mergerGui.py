import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
 
def merge_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF Files", "*.pdf")]
    )
    
    if not files:
        return
    
    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save the merged file as..."
    )
    
    if not output_file:
        return

    merger = PyPDF2.PdfMerger()
    try:
        for file in files:
            merger.append(file)
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("success", f"The file is saved as\n{output_file}")
    except Exception as e:
        messagebox.showerror("error", f"Error during merge:\n{e}")


# Create a basic GUI window
root = tk.Tk()
root.title("Merge PDF files")
root.geometry("300x150")
root.resizable(False, False)

btn = tk.Button(root, text="Select PDF files to merge", command=merge_pdfs, font=("Arial", 12))
btn.pack(expand=True)

root.mainloop()
