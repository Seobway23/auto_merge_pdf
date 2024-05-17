from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os


def create_table_of_contents(file_list, toc_filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, 'assets', 'NanumGothic.ttf')

    pdfmetrics.registerFont(TTFont('NanumGothic', font_path))  # 한글 폰트 등록
    c = canvas.Canvas(toc_filename, pagesize=letter)
    width, height = letter
    c.setFont("NanumGothic", 12)  # 한글 폰트 사용
    y_position = height - 50 * mm

    for pdf_file in file_list:
        title = pdf_file.split('/')[-1]
        text_width = c.stringWidth(title, "NanumGothic", 12)
        text_x = (width - text_width) / 2
        c.drawString(text_x, y_position, title)
        y_position -= 15 * mm
        if y_positio
            n < 20 * mm:
            c.showPage()
            c.setFont("NanumGothic", 12)
            y_position = height - 50 * mm

    c.save()

def merge_pdfs_with_toc(files, cover_path, output_path):
    writer = PdfWriter()

    if cover_path:
        cover_pdf = PdfReader(cover_path)
        for page in cover_pdf.pages:
            writer.add_page(page)

    toc_path = 'output/toc.pdf'
    create_table_of_contents(files, toc_path)
    toc_pdf = PdfReader(toc_path)
    for page in toc_pdf.pages:
        writer.add_page(page)

    for pdf_file in files:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
