# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SOUMYA RAI

*INTERN ID*: CT06DN45

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

Project Overview:
This project focuses on automating the generation of professional, formatted PDF reports from raw data using Python. The core idea is to simplify and speed up the process of data analysis and reporting, which is often done manually and can be repetitive and error-prone. The script reads structured data from an external file (e.g., CSV), performs basic analysis such as calculating statistical metrics, and produces a clean, readable PDF report using the FPDF library.

Objective:
The goal of the project is to:

Read structured data from a file,

Analyze it to extract meaningful insights,

Generate a well-formatted PDF report,

Eliminate manual reporting tasks and save time.

This task simulates real-world scenarios in offices, education, HR departments, and data analysis jobs, where reports are often generated from spreadsheets or databases.

Tools and Technologies Used:
Python – Core programming language used for scripting and data analysis.

Pandas – To read the CSV file and perform basic data manipulation and statistics.

FPDF – A lightweight library used to generate PDF files in Python.

These tools were chosen for their simplicity, flexibility, and wide community support, making them beginner-friendly while still being powerful enough for production tasks.

Workflow:
Data Ingestion:
The project begins by reading a CSV file using the Pandas library. The sample file contains student names and their corresponding marks. The script uses pandas.read_csv() to load the data into a DataFrame for processing.

Data Analysis:
Basic statistical computations are performed:

Average Marks

Highest Marks

Lowest Marks
These insights provide a quick summary of the data and are often the first step in reporting.

PDF Report Generation:
Using the FPDF library:

A new PDF document is created.

The title is added with formatting.

Statistical insights are printed as bullet points.

A neat table is generated with names and marks for each student.

The file is saved as report.pdf.

The PDF is visually clean and readable, making it suitable for printing or sharing digitally.

Deliverables:
data.csv – Sample dataset with student information.

generate_report.py – Python script that reads, analyzes, and generates the report.

report.pdf – Final formatted output containing the summary and raw data in table form.

Future Enhancements:
Adding visual charts (bar/pie) using matplotlib or plotly.

Allowing input from Excel files or user forms.

Using reportlab for more advanced formatting and layouts.

Emailing the generated PDF automatically using smtplib.

Learning Outcome:
This project helped me understand file handling, data analysis using Pandas, and PDF creation in Python. It also demonstrated how simple scripts can automate repetitive tasks in professional workflows. I learned how to structure a Python project and gained hands-on experience with real-world tools used in data reporting and business automation.
