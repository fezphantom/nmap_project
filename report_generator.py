from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df, filename="nmap_report.pdf"):
    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()

    # Title
    elements.append(Paragraph("Nmap Security Scan Report", styles['Title']))

    # Summary
    total_ports = len(df)
    open_ports = len(df[df["state"] == "open"])
    high_risk = len(df[df["risk"] == "High"])

    elements.append(Paragraph(f"Total Ports: {total_ports}", styles['Normal']))
    elements.append(Paragraph(f"Open Ports: {open_ports}", styles['Normal']))
    elements.append(Paragraph(f"High Risk Ports: {high_risk}", styles['Normal']))

    # Table data
    table_data = [["Port", "State", "Service", "Risk"]]

    for _, row in df.iterrows():
        table_data.append([row["port"], row["state"], row["service"], row["risk"]])

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)