import tkinter as tk
from tkinter import filedialog, messagebox
from autoPdf.modules.pdf_generator.creator import create_cover
from autoPdf.modules.merger.merger import merge_pdfs_with_toc


class PDFMergerUI:
    def __init__(self, root):
        self.root = root
        self.root.title('PDF Merger Tool')

        self.file_list = []

        self.select_button = tk.Button(root, text="Select PDFs", command=self.add_files)
        self.select_button.pack()

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack()

        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()
        self.title_button = tk.Button(root, text="Set Cover Title", command=self.set_cover)
        self.title_button.pack()

        self.merge_button = tk.Button(root, text="Merge PDFs", command=self.merge_files)
        self.merge_button.pack()

    def add_files(self):
        filenames = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in filenames:
            if file not in self.file_list:
                self.file_list.append(file)
                self.listbox.insert(tk.END, file)

    def set_cover(self):
        title = self.title_entry.get()
        if title:
            cover_filename = 'output/cover.pdf'
            create_cover(title, cover_filename)
            messagebox.showinfo('Success', 'Cover set successfully.')
        else:
            messagebox.showerror('Error', 'Please enter a cover title.')

    def merge_files(self):
        if self.file_list:
            cover_path = 'output/cover.pdf'
            output_path = 'output/merged_document.pdf'
            merge_pdfs_with_toc(self.file_list, cover_path, output_path)
            messagebox.showinfo('Success', 'PDFs merged successfully with TOC.')
        else:
            messagebox.showerror('Error', 'No PDF files selected.')


def run_ui():
    root = tk.Tk()
    app = PDFMergerUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_ui()
