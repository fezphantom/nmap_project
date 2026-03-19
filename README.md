# 🔐 Nmap Security Analysis Dashboard

## 📌 Overview
This project implements a security-focused pipeline for analyzing Nmap scan results and identifying potential vulnerabilities.

The system parses Nmap XML output, classifies risk levels for exposed services, and visualizes findings through an interactive dashboard. It also generates automated PDF reports to support vulnerability assessment and security analysis workflows.

---

## 🎯 Objectives

- Parse Nmap scan outputs into structured data
- Identify open ports and exposed services
- Classify vulnerabilities based on risk level
- Visualize results using an interactive dashboard
- Generate security reports for analysis and documentation

---

## 🧠 Skills Demonstrated

- Log parsing and normalization
- Vulnerability assessment
- Risk classification and prioritization
- Security monitoring workflows
- Python-based data analysis
- Dashboard development (Streamlit)

---

## 🏗️ Architecture


Nmap Scan → XML Output → Parser → DataFrame → Risk Classification → Dashboard → PDF Report


---

## ⚙️ Technologies Used

- Python
- Pandas
- Streamlit
- XML Parsing (ElementTree)
- ReportLab (PDF generation)
- Nmap (network scanning) :contentReference[oaicite:0]{index=0}

---

## 📂 Project Structure


nmap_project/
│── app.py # Streamlit dashboard
│── parser.py # XML parsing logic
│── report_generator.py # PDF report generation
│── data/ # Sample scan outputs
│── README.md


---

## 🔍 Key Features

### 📥 Log Parsing
- Extracts port, state, and service from Nmap XML output

### 🚨 Risk Classification
- Flags high-risk ports (e.g., SMB, RDP, Telnet)
- Categorizes findings into Low, Medium, High risk

### 📊 Dashboard
- Interactive filtering of scan results
- Displays open ports and high-risk findings

### 📄 PDF Reporting
- Generates structured reports including:
  - Summary metrics
  - Risk analysis
  - Detailed findings table

---

## 🧪 Example Use Case

- Scan a network using Nmap:
```bash
nmap -sV -oX scan.xml scanme.nmap.org

Upload the XML file into the dashboard

Identify open ports and potential vulnerabilities

Generate a PDF report for documentation

🚀 Getting Started
1. Clone the repo
git clone https://github.com/fezphantom/nmap_project.git
cd nmap_project
2. Install dependencies
pip install -r requirements.txt
3. Run the dashboard
streamlit run app.py

📈 Results & Impact

Identified open and potentially vulnerable services

Simulated real-world vulnerability assessment workflows

Built an end-to-end security analysis pipeline

🔮 Future Improvements

CVE integration for vulnerability lookup

Real-time log ingestion

SIEM integration (Splunk / Elastic)

Automated alerting system

👤 Author

Peter Utomakili
Data Scientist | Aspiring Security Analyst
https://github.com/fezphantom