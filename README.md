# FlyRank Capstone – Embeddable Widget & Lead-Capture Platform

A production-inspired backend application that enables businesses to create embeddable widgets (contact forms, signup forms, popups) and collect leads securely from any website.

The platform generates a single JavaScript embed snippet that customers can place on their websites. Visitors interact with the widget, and submissions are validated, protected against abuse, enriched with geolocation data, stored securely, and displayed through an authenticated dashboard.

---

## Features

### Widget Management
- Tenant authentication
- Create, Read, Update, Delete widgets
- Multiple widget types
- Custom form fields
- Embed script generation
- Tenant isolation

### Public Widget Delivery
- Public widget configuration endpoint
- JavaScript widget loader
- Versioned widget bundle
- HTTP caching
- CORS enabled

### Lead Submission API
- Public API
- Request validation
- Spam detection
- Rate limiting
- Secure data storage
- Cross-origin requests

### Geo Enrichment
- IP Geolocation
- Primary provider
- Automatic fallback provider
- Graceful degradation if providers fail

### Dashboard
- Submission history
- Widget analytics
- Total submissions
- Per-widget statistics
- Geo statistics

### Security
- JWT Authentication
- Multi-tenant authorization
- Input validation
- Rate limiting
- Honeypot spam protection
- Environment-based secrets

---

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

## Database

- PostgreSQL
- Alembic Migrations

## Infrastructure

- Docker
- Docker Compose

## Security

- JWT Authentication
- SlowAPI Rate Limiting
- CORS Middleware

## Testing

- Pytest
- HTTPX

---

# Project Structure

```
flyrank-capstone-widget-platform/

│
├── app/
│   ├── api/
│   ├── auth/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── middleware/
│   ├── utils/
│   └── main.py
│
├── static/
│   └── widget.js
│
├── customer-site/
│   └── index.html
│
├── tests/
│
├── alembic/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
├── BUILDLOG.md
├── EVIDENCE.md
└── capstone.yaml
```

---

# Architecture

```
                    +----------------------+
                    |  Widget Owner        |
                    +----------+-----------+
                               |
                               |
                        Authenticated API
                               |
                               ▼
                 +----------------------------+
                 | Widget Management Service  |
                 +----------------------------+
                               |
                               ▼
                        PostgreSQL Database
                               |
      ------------------------------------------------
      |                                              |
      ▼                                              ▼

 Public Config API                         Dashboard API
      |                                              |
      ▼                                              ▼

 Widget.js                              Analytics & Leads

      ▲
      |
Customer Website
      |
      ▼

Visitor submits form

      |
      ▼

Submission API
      |
      ├── Validation
      ├── Spam Filter
      ├── Rate Limiter
      ├── Geo Enrichment
      ├── Store Submission
      └── Email/Webhook
```

---

# API Endpoints

## Authentication

```
POST   /auth/register
POST   /auth/login
```

---

## Widgets

```
GET     /widgets
GET     /widgets/{id}
POST    /widgets
PUT     /widgets/{id}
DELETE  /widgets/{id}
```

---

## Public

```
GET   /public/widgets/{id}/config
GET   /widget.js
POST  /submissions
```

---

## Dashboard

```
GET /dashboard/summary
GET /dashboard/submissions
GET /dashboard/widgets
GET /dashboard/analytics
```

---

# Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/flyrank-capstone-widget-platform.git

cd flyrank-capstone-widget-platform
```

---

## Create Environment

```bash
python -m venv venv

source venv/bin/activate

# Windows
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost/widget_db

SECRET_KEY=your-secret

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

PRIMARY_GEO_PROVIDER=https://ip-api.com/json/

SECONDARY_GEO_PROVIDER=https://ipapi.co/

SMTP_HOST=localhost
```

---

## Start PostgreSQL

```bash
docker compose up -d
```

---

## Run Database Migrations

```bash
alembic upgrade head
```

---

## Start Server

```bash
uvicorn app.main:app --reload
```

Server:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

# Testing

Run all tests

```bash
pytest
```

---

# Example Widget Embed

```html
<script src="http://localhost:8000/widget.js?id=abc123"></script>
```

---

# Example Submission Flow

```
Customer creates widget

↓

API generates embed snippet

↓

Customer pastes snippet into website

↓

Visitor submits form

↓

Validation

↓

Rate Limiting

↓

Spam Detection

↓

Geo Enrichment

↓

Store Submission

↓

Email/Webhook

↓

Dashboard Updates
```

---

# Future Improvements

- WebSocket live dashboard
- CAPTCHA support
- Advanced analytics
- Widget themes
- Email templates
- GDPR compliance
- Webhook retries
- Export CSV

---

# Documentation

This repository also contains:

- README.md
- BUILDLOG.md
- EVIDENCE.md
- capstone.yaml
- .env.example

---

# License

MIT License

---

# Author

**Maryam Wasay**

Backend Software Engineering & AI Enthusiast

BS Computer Science Student

FlyRank Backend Engineering Internship
