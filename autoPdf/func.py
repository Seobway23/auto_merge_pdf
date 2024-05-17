import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pypdfium2 import PdfDocument

def create_cover(title):
    c = canvas.Canvas(title + "_cover.pdf", pagesize=letter)
    c.setFont("Helvetica", 18)
    c.drawCentredString(300, 700, title)
    c.save()

def merge_pdfs(pdfs, output):
    merged_pdf = PdfDocument.new()
    for pdf in pdfs:
        doc = PdfDocument(pdf)
        merged_pdf.copy_pages_from(doc, range(doc.page_count()))
    merged_pdf.save(output)
    merged_pdf.close()

def select_files():
    path = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    file_list.set(path)

def start_merge():
    title = title_entry.get()
    create_cover(title)
    pdfs = list(file_list.get()) + [title + "_cover.pdf"]
    merge_pdfs(pdfs, "output.pdf")
    messagebox.showinfo("Success", "PDF has been created and merged!")

app = tk.Tk()
app.title("PDF Merger with Cover")

file_list = tk.Variable(app)

tk.Label(app, text="Enter Title for Cover:").pack()
title_entry = tk.Entry(app)
title_entry.pack()

tk.Button(app, text="Select PDF Files", command=select_files).pack()
tk.Button(app, text="Merge PDFs", command=start_merge).pack()

app.mainloop()
