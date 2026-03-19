# Nmap Network Vulnerability Scanner

## Overview
This project scans a network using Nmap, parses results, and displays findings in a dashboard.

## Features
- Network scanning with Nmap
- XML parsing
- Detection of open ports and services
- Simple dashboard (Streamlit)

## Setup
```bash
brew install nmap
pip install python-nmap streamlit pandas
```

## Run Scan
```bash
nmap -sV -oX scan.xml 192.168.1.0/24
```

## Run App
```bash
streamlit run app.py
```
