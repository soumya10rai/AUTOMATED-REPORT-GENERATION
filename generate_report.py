import pandas as pd

# Step 1: Read data
data = pd.read_csv("data.csv")

# Step 2: Basic analysis
average = data["Marks"].mean()
highest = data["Marks"].max()
lowest = data["Marks"].min()

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Student Marks Report", ln=1, align='C')

# Stats
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Average Marks: {average:.2f}", ln=2)
pdf.cell(200, 10, txt=f"Highest Marks: {highest}", ln=3)
pdf.cell(200, 10, txt=f"Lowest Marks: {lowest}", ln=4)

# Table
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(100, 10, "Name", 1)
pdf.cell(50, 10, "Marks", 1)
pdf.ln()

pdf.set_font("Arial", size=12)
for index, row in data.iterrows():
    pdf.cell(100, 10, row["Name"], 1)
    pdf.cell(50, 10, str(row["Marks"]), 1)
    pdf.ln()

# Save PDF
pdf.output("report.pdf")
