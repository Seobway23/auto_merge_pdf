# modules/pdf_generator/creator.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

def create_cover(title, filename):
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    c = canvas.Canvas(filename)
    width, height = letter
    # 첫번째: 폰트 종류, 두번째: 폰트 사이즈
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, 'assets', 'NanumGothic.ttf')

    font_name = "NanumGothic"
    font_size = 30

    pdfmetrics.registerFont(TTFont('NanumGothic', 'NanumGothic.ttf'))  # 한글 폰트 등록
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("NanumGothic", 18)
    text_width = c.stringWidth(title, "NanumGothic", 18)
    text_x = (letter[0] - text_width) / 2
    c.drawString(text_x, 750, title)
    c.showPage()
    c.save()