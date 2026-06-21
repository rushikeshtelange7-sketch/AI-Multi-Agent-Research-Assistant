from fpdf import FPDF


def create_pdf(topic, report):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(
        200,
        10,
        txt="AI-Powered Multi-Agent Research Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(
        0,
        10,
        txt=f"Topic:\n{topic}"
    )

    pdf.ln(5)

    pdf.multi_cell(
        0,
        10,
        txt=report
    )

    file_name = "research_report.pdf"

    pdf.output(file_name)

    return file_name