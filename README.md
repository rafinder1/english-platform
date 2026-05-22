# English Learning Platform API

Backend system for an English learning platform built with Django + DRF.

---

## 🧠 Project Overview

This project is a modular learning platform backend that supports:

- Courses
- Lessons
- Structured content (tiles, sections, blocks)
- JSON-based content engine
- Future support for progress tracking, payments, notifications

---

## 🏗️ Tech Stack

- Django
- Django REST Framework
- PostgreSQL (planned)
- Redis (planned)
- Celery (planned)
- Docker (planned)

---

## 📦 Architecture

Course → Lesson → Tile → Section → ContentBlock

Each ContentBlock is a flexible JSON-based unit that supports:
- text
- images
- lists
- future: quizzes, audio, AI tasks

---

## 🚀 Run project (dev)

```bash
cd backend
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
