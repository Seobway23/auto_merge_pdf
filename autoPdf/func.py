import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# 작업 디렉토리 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(current_dir, 'assets', 'NanumGothic.ttf')

# 폰트 등록
pdfmetrics.registerFont(TTFont('NanumGothic', font_path))

# PDF 생성
c = canvas.Canvas("example.pdf")
c.setFont("NanumGothic", 12)
c.drawString(100, 750, "안녕하세요, ReportLab에서 한글을 사용합니다!")
c.save()
