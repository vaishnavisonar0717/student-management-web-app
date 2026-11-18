# Student Management Web App

A responsive student-record management app built with Python, Django, SQLite, HTML and CSS.

## Features
- Dashboard with total student count
- Create, view, update and delete student records
- Search by name, admission number, email or course
- Responsive layout and clean UI
- SQLite database for local development

## 1. Requirements
- Python 3.10+
- pip

## 2. Set up the project

```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 3. Create the database and run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

Optional admin account:

```bash
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin/

## 4. Test

```bash
python manage.py check
python manage.py test
```

## 5. Push to GitHub

Create an empty repository on GitHub (do not add a README if you already have this one).
In the project folder, run:

```bash
git init
git add .
git commit -m "Build student management web app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-management-web-app.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Before publishing
This is a learning/demo project. For real student data, add authentication and role-based permissions,
CSRF-safe deployment settings, backups, HTTPS, and a privacy/security review. Do not upload real student
personal data or your local SQLite database to GitHub.
