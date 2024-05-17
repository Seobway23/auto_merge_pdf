# modules/ui/interface.py
import tkinter as tk
from tkinter import filedialog
from autoPdf.modules.pdf_generator.creator import create_pdf
from autoPdf.modules.merger.merger import merge_pdfs


def run_ui():
    def select_files():
        return filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])

    def start_merge():
        files = select_files()
        merge_pdfs(files)

    def start_pdf_creation():
        title = title_entry.get()
        create_pdf(title=title, filename=title.replace(" ", "_") + ".pdf")

    app = tk.Tk()
    app.title("PDF Tools")

    title_entry = tk.Entry(app)
    title_entry.pack()

    create_button = tk.Button(app, text="Create PDF", command=start_pdf_creation)
    create_button.pack()

    merge_button = tk.Button(app, text="Merge PDFs", command=start_merge)
    merge_button.pack()

    app.mainloop()
