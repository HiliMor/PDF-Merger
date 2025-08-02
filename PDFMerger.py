import PyPDF2
import sys

merger = PyPDF2.PdfFileMerger()

#default output file name 
output_filename = "combinedDocs.pdf"

files_to_merge = []

for arg in sys.argv[1:]:
    if arg.startswith("output="):
        output_filename = arg.split("=", 1)[1]
    elif arg.endswith(".pdf"):
        files_to_merge.append(arg)

if not files_to_merge:
    print("No PDF files provided.")
    sys.exit(1)

for file in files_to_merge:
    try:
        merger.append(file)
    except Exception as e:
        print(f"Error with file {file}: {e}")

merger.write(output_filename)
merger.close()
print(f"Merged PDF saved as {output_filename}")
