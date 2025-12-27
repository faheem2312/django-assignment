# PDF to DOCX Converter (Django)

A Django-based web application that recreates a legal mediation application form from a given PDF into an editable Microsoft Word document using Python.

---

## 📌 Overview

This project focuses on accurately replicating the structure, layout, spacing, and formatting of a legal PDF form into an MS Word document.  
Instead of using automated PDF-to-DOCX conversion tools, the PDF was manually analyzed and reconstructed using structured tables, merged cells, and controlled spacing to achieve form-level accuracy.

Django is used as the web framework to handle request flow and file generation, while `python-docx` is used for Word document creation.

---

## 🛠 Tech Stack

- Python 3.x  
- Django  
- python-docx  

---

## ✨ Features

- Recreates legal PDF form layout in Word format  
- Structured table-based document generation  
- Proper section grouping and merged cells  
- Clean, minimal user interface  
- Editable placeholders in the generated DOCX file  

---

## 📂 Project Setup

1. Clone the Repository
- git clone https://github.com/faheem2312/django-assignment.git
- cd task

2. Create and Activate Virtual Environment (Recommended)

Windows
- python -m venv venv
- venv\Scripts\activate

Linux / macOS
- python3 -m venv venv
- source venv/bin/activate

3. Install Dependencies
- pip install -r requirements.txt

4. Apply Migrations
- python manage.py migrate

5. Run the Development Server
- python manage.py runserver

6. Access the Application

- Open your browser and navigate to:
http://127.0.0.1:8000/


