# modules/merger/merger.py
from pypdfium2 import PdfDocument
from autoPdf.config.settings import pdf_output_directory

def merge_pdfs(file_list, output_filename="merged_output.pdf"):
    merged_pdf = PdfDocument.new()
    for pdf_file in file_list:
        doc = PdfDocument(pdf_file)
        merged_pdf.copy_pages_from(doc, range(doc.page_count()))
    merged_pdf.save(pdf_output_directory + output_filename)
    merged_pdf.close()
