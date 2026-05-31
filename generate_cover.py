"""
Generate the filled ISITCOM cover page for the PFE report.
Student: Asma Daoussi
Academic Supervisor: M. Sami BEN AMOR
Professional Supervisor: Mme Nour LTAIEF
Company: Inherited Games Studio (IGS)
Year: 2025/2026
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "cover_page_filled.pdf")
ISITCOM_LOGO = os.path.join(os.path.dirname(__file__), "images", "isitcom.jpg")
IGS_LOGO = os.path.join(os.path.dirname(__file__), "images", "logos", "igs.jpg")

W, H = A4  # 595.27 x 841.89 pts

ISI_BLUE = colors.HexColor("#1F4E79")
DARK_GRAY = colors.HexColor("#505050")
LINE_DARK = colors.HexColor("#2C2C2C")


def draw_centered_text(c, text, y, size=11, bold=False, color=colors.black):
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    c.setFillColor(color)
    c.drawCentredString(W / 2, y, text)


def draw_line(c, y, color=ISI_BLUE, thickness=2.5):
    c.setStrokeColor(color)
    c.setLineWidth(thickness)
    c.line(1.5 * cm, y, W - 1.5 * cm, y)


def main():
    c = canvas.Canvas(OUTPUT, pagesize=A4)

    # ── Header block ──────────────────────────────────────────────
    y = H - 1.4 * cm
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.black)
    header_lines = [
        "MINISTERE DE L'ENSEIGNEMENT SUPERIEUR ET DE LA RECHERCHE SCIENTIFIQUE",
        "UNIVERSITE DE SOUSSE",
        "INSTITUT SUPERIEUR D'INFORMATIQUE",
        "ET DES TECHNOLOGIES DE COMMUNICATION",
    ]
    for line in header_lines:
        c.drawCentredString(W / 2, y, line)
        y -= 0.38 * cm

    # Arabic subtitle (transliterated as plain text fallback)
    c.setFont("Helvetica", 8)
    c.setFillColor(DARK_GRAY)
    c.drawCentredString(W / 2, y, "المعهد العالي للإعلامية وتكنولوجيات الاتصال")
    y -= 0.6 * cm

    # ── ISITCOM Logo ──────────────────────────────────────────────
    logo_size = 3.0 * cm
    if os.path.exists(ISITCOM_LOGO):
        c.drawImage(ISITCOM_LOGO, (W - logo_size) / 2, y - logo_size,
                    width=logo_size, height=logo_size, preserveAspectRatio=True, mask="auto")
    y -= logo_size + 0.5 * cm

    # ── Main title ────────────────────────────────────────────────
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(colors.black)
    c.drawCentredString(W / 2, y, "Rapport de stage de fin d'études")
    y -= 0.65 * cm

    c.setFont("Helvetica", 12)
    c.setFillColor(DARK_GRAY)
    c.drawCentredString(W / 2, y, "Présenté en vue de l'obtention du Diplôme National d'Ingénieur")
    y -= 0.55 * cm

    c.setFont("Helvetica", 11)
    c.drawCentredString(W / 2, y, "Spécialité : Téléinformatique")
    y -= 0.55 * cm

    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    c.drawCentredString(W / 2, y, "Réalisé Par")
    y -= 0.5 * cm

    # ── Student name ──────────────────────────────────────────────
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(ISI_BLUE)
    c.drawCentredString(W / 2, y, "Asma Daoussi")
    y -= 0.6 * cm

    # ── Top separator bar ─────────────────────────────────────────
    draw_line(c, y, color=ISI_BLUE, thickness=3)
    y -= 0.25 * cm

    # ── Project title box ─────────────────────────────────────────
    box_x = 1.5 * cm
    box_w = W - 3 * cm
    box_h = 2.6 * cm
    c.setStrokeColor(ISI_BLUE)
    c.setFillColor(colors.white)
    c.setLineWidth(1.5)
    c.roundRect(box_x, y - box_h, box_w, box_h, 4, stroke=1, fill=1)

    # Inner box
    inner_pad = 0.25 * cm
    c.setLineWidth(0.8)
    c.roundRect(box_x + inner_pad, y - box_h + inner_pad,
                box_w - 2 * inner_pad, box_h - 2 * inner_pad, 2, stroke=1, fill=0)

    title_y = y - box_h / 2 + 0.3 * cm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(ISI_BLUE)
    c.drawCentredString(W / 2, title_y, "Development of a Digital Asset Marketplace")
    c.setFont("Helvetica", 11)
    c.setFillColor(DARK_GRAY)
    c.drawCentredString(W / 2, title_y - 0.55 * cm, "for Inherited Games Studio (IGS)")
    y -= box_h + 0.3 * cm

    # ── Bottom separator bar ──────────────────────────────────────
    draw_line(c, y, color=ISI_BLUE, thickness=3)
    y -= 0.6 * cm

    # ── Supervisors section ───────────────────────────────────────
    col_left = 2.5 * cm
    col_right = 9.5 * cm

    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(colors.black)
    c.drawString(col_left, y, "Encadrant professionnel :")
    c.setFont("Helvetica", 10.5)
    c.drawString(col_right, y, "Mme Nour LTAIEF")
    y -= 0.6 * cm

    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(col_left, y, "Encadrant académique :")
    c.setFont("Helvetica", 10.5)
    c.drawString(col_right, y, "M. Sami BEN AMOR")
    y -= 1.0 * cm

    # ── Company section ───────────────────────────────────────────
    c.setFont("Helvetica", 11)
    c.setFillColor(DARK_GRAY)
    c.drawCentredString(W / 2, y, "Réalisé au sein de")
    y -= 0.45 * cm

    if os.path.exists(IGS_LOGO):
        igs_h = 2.5 * cm
        igs_w = 2.5 * cm
        c.drawImage(IGS_LOGO, (W - igs_w) / 2, y - igs_h,
                    width=igs_w, height=igs_h, preserveAspectRatio=True, mask="auto")
        y -= igs_h + 0.3 * cm
    else:
        y -= 0.3 * cm

    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.black)
    c.drawCentredString(W / 2, y, "Inherited Games Studio")
    y -= 1.2 * cm

    # ── Academic year bar ─────────────────────────────────────────
    draw_line(c, y, color=LINE_DARK, thickness=1.5)
    y -= 0.55 * cm

    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(colors.black)
    c.drawCentredString(W / 2, y, "Année universitaire : 2025/2026")
    y -= 0.3 * cm
    draw_line(c, y, color=LINE_DARK, thickness=1.5)

    # ── Footer ────────────────────────────────────────────────────
    footer_y = 0.8 * cm
    c.setFont("Helvetica", 7.5)
    c.setFillColor(DARK_GRAY)
    c.drawCentredString(
        W / 2, footer_y + 0.3 * cm,
        "Institut Supérieur d'Informatique et des Technologies de Communication   ISITCOM"
    )
    c.drawCentredString(
        W / 2, footer_y,
        "Tél/Fax : +216 73 37 15 71 / +216 73 36 44 11"
    )

    c.save()
    print(f"Cover page saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
