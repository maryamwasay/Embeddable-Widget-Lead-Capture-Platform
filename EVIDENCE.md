# EVIDENCE.md

# FlyRank Backend Development Track Capstone

## Embeddable Widget & Lead-Capture Platform

This document provides evidence that the project satisfies the core requirements of the FlyRank Backend Development Track Capstone.

---

# 1. Widget Management

## ✔ Authenticated CRUD

The application provides authenticated CRUD operations for widgets.

Implemented Endpoints

- POST `/widgets/`
- GET `/widgets/`
- GET `/widgets/{id}`
- PUT `/widgets/{id}`
- DELETE `/widgets/{id}`

Authentication is required for every endpoint using JWT.

Verified By

- tests/test_auth.py
- tests/test_widgets.py

---

# 2. Multi-Tenant Isolation

Every widget query is filtered by the authenticated user's tenant.

Example

```python
Widget.tenant_id == current_user["tenant_id"]
```

Dashboard queries also use tenant isolation.

Verified By

- tests/test_widgets.py
- tests/test_dashboard.py

---

# 3. Embed Snippet Generation

Each widget provides an embeddable JavaScript snippet.

Endpoint

```
GET /widgets/{id}/embed
```

Example Response

```html
<script src="http://localhost:8000/static/widget.js"
data-widget-id="1"></script>
```

This allows customers to install the widget on any website using a single script tag.

---

# 4. Public Widget Delivery

Widget configuration is publicly available.

Endpoint

```
GET /public/widget/{id}
```

Response includes

- Widget ID
- Title
- Description
- Button Text
- Form Fields
- Version

Cache Header

```
Cache-Control: public, max-age=300
```

---

# 5. Public Submission API

Visitors can submit forms from external websites.

Endpoint

```
POST /public/submit/{id}
```

Features

- CORS enabled
- JSON validation
- Spam filtering
- Rate limiting
- Geo enrichment
- Database storage

Verified By

- tests/test_public.py

---

# 6. CORS Support

Cross-origin requests are supported.

Implemented

- CORSMiddleware
- OPTIONS Preflight

Endpoint

```
OPTIONS /public/submit/{id}
```

Verified By

- tests/test_cors.py

---

# 7. Request Validation

Incoming requests are validated using Pydantic schemas.

Invalid requests return proper HTTP status codes.

Examples

```
400 Bad Request
404 Not Found
422 Validation Error
```

Verified By

- tests/test_public.py

---

# 8. Rate Limiting

Implemented using SlowAPI.

Limit

```
5 requests/minute
```

Exceeded requests return

```
429 Too Many Requests
```

Verified By

- tests/test_rate_limit.py

---

# 9. Spam Protection

Spam detection is implemented using honeypot fields.

Spam submissions are rejected before database storage.

Verified By

- tests/test_spam.py

---

# 10. Geo Enrichment

Each submission attempts IP geolocation.

Processing Flow

```
Visitor IP
      ↓
Geo Provider
      ↓
Country
      ↓
City
      ↓
Database
```

If geo lookup fails, the submission is still stored.

Verified By

- tests/test_geo.py

---

# 11. Dashboard API

Authenticated dashboard endpoints provide analytics.

Summary

```
GET /dashboard/summary
```

Per Widget Statistics

```
GET /dashboard/widgets
```

Country Statistics

```
GET /dashboard/countries
```

Verified By

- tests/test_dashboard.py

---

# 12. Widget JavaScript

Static widget JavaScript is served from

```
GET /widget.js
```

or

```
/static/widget.js
```

The widget is loaded using the generated embed snippet.

---

# 13. Database

Database

- PostgreSQL

ORM

- SQLAlchemy

Tables

- Users
- Tenants
- Widgets
- Submissions

---

# 14. Docker Support

The application can be started using

```bash
docker-compose up --build
```

---

# 15. Automated Testing

The project contains automated tests for

- Authentication
- Widgets
- Public API
- Dashboard
- CORS
- Rate Limiting
- Spam Detection
- Geo Service
- Health Endpoints

Current Result

```
====================================

32 TESTS PASSED

0 FAILED

====================================
```

Run Tests

```bash
python -m pytest -v
```

---

# 16. Technology Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Pydantic
- SlowAPI
- JWT Authentication

---

# 17. Project Status

## Completed Features

- JWT Authentication
- Widget CRUD
- Multi-Tenant Isolation
- Public Widget Configuration
- Public Submission API
- Dashboard Analytics
- Request Validation
- Spam Detection
- Rate Limiting
- Geo-IP Enrichment
- Static Widget JavaScript
- Docker Configuration
- Automated Testing

---

# Final Test Result

```
================================================

32 PASSED
0 FAILED

================================================
```

The FlyRank Widget Platform successfully implements the core backend functionality required for the FlyRank Backend Development Track Capstone and has been verified through automated testing.