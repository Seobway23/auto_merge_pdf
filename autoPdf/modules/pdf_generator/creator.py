# modules/pdf_generator/creator.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from config.settings import pdf_output_directory, default_pdf_title

def create_pdf(title=default_pdf_title, filename="output.pdf"):
    c = canvas.Canvas(pdf_output_directory + filename, pagesize=letter)
    c.setFont("Helvetica", 18)
    c.drawString(200, 800, title)  # 예시로 제목만 추가
    c.save()
