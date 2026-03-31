from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=40,)
pdf.cell(120, 40, "CS50 Shirtificate", center=True)
pdf.image("shirtificate.png", x=pdf.epw/2)
pdf.output("tuto1.pdf")
