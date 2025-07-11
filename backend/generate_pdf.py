from reportlab.pdfgen import canvas
from database import SessionLocal
from models import Project

def generate_pdf():
    db = SessionLocal()
    projects = db.query(Project).filter(Project.featured == True).all()
    db.close()

    c = canvas.Canvas("portfolio_report.pdf")
    y = 800
    for p in projects:
        text = f"{p.name} - {p.language} - ⭐{p.stars}"
        c.drawString(100, y, text)
        y -= 20
    c.save()
