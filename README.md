# PDF Merger 🧩

A simple Python tool to merge multiple PDF files into a single PDF.

You can use it with a **graphical interface (GUI)** or from the **command line**, depending on your preference.

---

## 🖥️ Features

- Merge multiple PDF files
- Choose files using a GUI (Tkinter)
- Supports encrypted PDFs (requires password)
- Easy to use, clean interface

---

## 🔧 Requirements

- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [pycryptodome](https://pypi.org/project/pycryptodome/) (for encrypted PDF support)

Install dependencies:

```bash
pip install PyPDF2 pycryptodome
```

## 🚀 How to Run

GUI Version (recommended):
python mergerGui.py

A small window will open. Select your PDF files, choose where to save the merged result, and you’re done!

---

## 📁 Files in this Project

mergerGui.py — GUI version using Tkinter
PDFMerger.py — Command-line version
