# 🏛️ Court-Data Fetcher & Mini-Dashboard

This project is a mini web application built using **Flask**, **HTML**, and **JavaScript** that allows users to fetch case details from Indian court websites by entering:

- **Case Type**
- **Case Number**
- **Filing Year**

On submission, the app scrapes the selected court portal and displays metadata and PDF links for the most recent orders or judgments.

---

## 📌 Target Court

- [Delhi High Court](https://delhihighcourt.nic.in/app/get-case-type-status)
  
## 💡 Features

- 🔎 **Form Inputs** – Case Type, Case Number, Filing Year  
- ⚙️ **Backend (Flask)** –  
  - Automates court site access  
  - Bypasses tokens/CAPTCHA (strategy explained below)  
  - Extracts:
    - Parties' names  
    - Filing & next hearing dates  
    
- 📋 **Display** – Clean frontend to show case details   
- ❗ **Error Handling** – Friendly messages for invalid inputs or site downtime

---

## 🛠 Tech Stack

- **Backend**: Python (Flask),Selenium  
- **Frontend**: HTML, CSS, JavaScript  


---

## 🤖 CAPTCHA Strategy

This project uses Selenium WebDriver to automate interaction with the court website. CAPTCHA and view-state tokens are automatically detected and handled during form submission by simulating real user actions (e.g., clicks, input typing, waits). No manual intervention or OCR is required.

---

## Screenshort
<img width="1103" height="731" alt="image" src="https://github.com/user-attachments/assets/b9c43ba4-0fe5-44fe-beab-de6707cc192b" />
<img width="1002" height="736" alt="image" src="https://github.com/user-attachments/assets/54be9f11-13ca-46fc-b4fd-bba9aba2d48c" />

- ON SUBMIT
<img width="1339" height="900" alt="image" src="https://github.com/user-attachments/assets/73431bae-bede-4a94-9e78-2dae6ef61a78" />

 # screen recording link:
 https://drive.google.com/file/d/1lHyyJ370_tnUYEDEn1R2EOsekt5MwzXy/view?usp=sharing

