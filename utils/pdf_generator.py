from fpdf import FPDF


def create_pdf(topic, report):

    file_name = f"{topic.replace(' ', '_')}_report.pdf"

    pdf = FPDF()
    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, topic, ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", size=12)

    # Remove unsupported Unicode characters
    clean_report = (
        report.replace("•", "-")
              .replace("–", "-")
              .replace("—", "-")
              .replace("“", '"')
              .replace("”", '"')
              .replace("'", "'")
              .replace("'", "'")
    )

    # Keep only latin-1 compatible characters
    clean_report = clean_report.encode(
        "latin-1",
        "replace"
    ).decode("latin-1")

    pdf.multi_cell(0, 10, clean_report)

    pdf.output(file_name)

    return file_name