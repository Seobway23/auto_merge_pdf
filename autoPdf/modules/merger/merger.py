from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm


def create_table_of_contents(file_list, toc_filename):
    # 폰트 파일의 절대 경로를 정확하게 지정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, '..', '..', 'assets', 'NanumGothic.ttf')

    # # 경로 확인 로그 출력
    # print("Attempting to load font from:", font_path)

    # 폰트 파일 존재 여부 확인
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"The font file was not found in the path: {font_path}")

        # 폰트 등록
    pdfmetrics.registerFont(TTFont('NanumGothic', font_path))

    c = canvas.Canvas(toc_filename, pagesize=letter)
    width, height = letter

    # "목차" 제목 설정
    c.setFont("NanumGothic", 16)  # 폰트와 크기 설정
    toc_title = "목차"
    title_width = c.stringWidth(toc_title, "NanumGothic", 16)
    title_x = (width - title_width) / 2
    title_y = height - 30 * mm
    c.drawString(title_x, title_y, toc_title)

    # 파일 제목 목록
    c.setFont("NanumGothic", 12)
    y_position = title_y - 30 * mm  # 제목 아래에 위치

    for pdf_file in file_list:
        title = pdf_file.split('/')[-1]
        text_width = c.stringWidth(title, "NanumGothic", 12)
        text_x = (width - text_width) / 2
        c.drawString(text_x, y_position, title)
        y_position -= 15 * mm
        if y_position < 20 * mm:  # 페이지가 다 차면 새 페이지 생성
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
