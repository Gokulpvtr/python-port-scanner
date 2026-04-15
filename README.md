# 🔍 Advanced Python Port Scanner

## 📌 Description
This project is a multi-threaded port scanner built using Python. It performs network reconnaissance by identifying open ports and services on a target system.

## 🚀 Features
- Port range scanning
- Multi-threading for faster performance
- Service detection (HTTP, SSH, etc.)
- Banner grabbing (server information)
- JSON report generation

## 🧠 Security Insight
Open ports can expose services to potential attacks:
- Port 22 (SSH) → Brute force attack risk
- Port 80 (HTTP) → Web vulnerabilities (XSS, SQL Injection)

## ▶️ How to Run
```bash
python scanner.py
