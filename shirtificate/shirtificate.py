from fpdf import FPDF
from PIL import Image
import sys

def main():
    name = input("Name: ")
    if name == "":
        sys.exit()
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_auto_page_break(False, margin=0)
    # pdf.set_font("helvetica", "B", 16)
    # pdf.cell(pdf.epw/3, pdf.eph/3, align="C")
    # pdf.cell(50, 10, "CS50 Shirtificate", border=1, align="C")
    # # print(pdf.eph)
    # # print(pdf.epw)
    # # pdf.set_y(-pdf.eph/3)
    # pdf.set_x(pdf.epw/3)
    # pdf.ln(70)
    # pdf.set_font("helvetica", "B", 12)
    # pdf.set_text_color(255,255,255)
    # # img = Image.open("../shirtificate/shirtificate.png")
    # # img = img.crop((10, 10, 490, 490)).resize((100, 100), resample=Image.NEAREST)
    # pdf.image("../shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2, x=pdf.epw/4, y=pdf.eph/6 )
    # # pdf.image(img, h=pdf.eph/2, w=pdf.epw/2, x=pdf.epw/4, y=pdf.eph/6 )
    # pdf.cell(pdf.epw/3-5, pdf.eph/6, align="C")
    # pdf.cell(50, 10, name, align="C")

    # # pdf.cell(pdf.epw/4, pdf.eph/4, align="C")
    # # pdf.ln(100)
    # # pdf.cell(50, 10, "John Harvard took CS50", border=1, align="C")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(False, margin=0)
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(0, 60, "CS50 Shirtificate", border=0, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.image("shirtificate.png", w=pdf.epw)
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255,255,255)
    # pdf.text(x=47.3, y=140, txt=f"{name} took CS50")
    pdf.text(x=pdf.epw/3-16, y=140, txt=f"{name} took CS50")
    # pdf.cell(pdf.epw/3-5, pdf.eph/6, align="C")
    # pdf.cell(50, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()