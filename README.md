# 🚀 Multi-Tenant SaaS Project Management Backend

> A production-style backend system for a multi-tenant SaaS project management platform built with **FastAPI**.  
> Multiple organizations share one platform while keeping their data securely isolated.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![OAS](https://img.shields.io/badge/OAS-3.1-green)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-teal)
![License](https://img.shields.io/badge/license-Educational-lightgrey)

Each organization manages its own users, projects, and tasks through a RESTful API. The architecture follows modern backend engineering patterns such as layered architecture, background workers, middleware processing, and containerized deployment.

This project demonstrates real-world backend concepts commonly used in SaaS platforms.

---

## 📌 Table of Contents

- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Database Design](#database-design)
- [API Documentation](#api-documentation)
- [Example API Endpoints](#example-api-endpoints)
- [Environment Variables](#environment-variables)
- [Running the Project Locally](#running-the-project-locally)
- [Running Background Workers](#running-background-workers)
- [Database Migrations](#database-migrations)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [Middleware Components](#middleware-components)
- [Future Improvements](#future-improvements)
- [Learning Objectives](#learning-objectives)
- [License](#license)

---

## ✨ Key Features

- ✅ Multi-tenant architecture with organization-based data isolation
- ✅ JWT-based authentication and authorization
- ✅ Layered backend architecture (API, Services, Repositories)
- ✅ Asynchronous background tasks using Celery
- ✅ Redis integration for message brokering
- ✅ Database migrations using Alembic
- ✅ Request logging middleware
- ✅ Rate limiting middleware
- ✅ Tenant context middleware
- ✅ Pagination utilities for scalable APIs
- ✅ Docker-based deployment
- ✅ Automated testing with Pytest

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|------------|
| Backend Framework | **FastAPI** |
| Language | **Python** |
| Database | **PostgreSQL** |
| ORM | **SQLAlchemy** |
| Migrations | **Alembic** |
| Queue System | **Redis** |
| Background Workers | **Celery** |
| Authentication | **JWT** |
| Testing | **Pytest** |
| Containerization | **Docker** |

---

## 🏗 System Architecture

The backend follows a **layered architecture** commonly used in scalable SaaS applications.
```
Client
  │
  ▼
API Routes
  │
  ▼
Service Layer
  │
  ▼
Repository Layer
  │
  ▼
Database Models
  │
  ▼
PostgreSQL
```

| Layer | Responsibility |
|-------|----------------|
| **Schemas** | Handles request and response validation |
| **Middleware** | Processes requests globally (logging, rate limiting, tenant detection) |
| **Workers** | Processes background jobs asynchronously |

---

## 📁 Project Structure
```
saas_backend/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── auth.py
│   │       ├── organizations.py
│   │       ├── projects.py
│   │       └── tasks.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   └── security.py
│   │
│   ├── middleware/
│   │   ├── logging.py
│   │   ├── rate_limit.py
│   │   └── tenant.py
│   │
│   ├── models/
│   │   ├── organization.py
│   │   ├── project.py
│   │   ├── task.py
│   │   └── user.py
│   │
│   ├── repositories/
│   │   ├── project_repo.py
│   │   ├── task_repo.py
│   │   └── user_repo.py
│   │
│   ├── schemas/
│   │   ├── project_schema.py
│   │   ├── task_schema.py
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── project_service.py
│   │   └── task_service.py
│   │
│   ├── utils/
│   │   └── pagination.py
│   │
│   ├── workers/
│   │   └── celery_worker.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_projects.py
│   └── test_tasks.py
│
├── alembic/
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🗄 Database Design

The system contains four core entities.

### Organizations
Represents tenants using the SaaS platform.

### Users
Users belong to organizations and authenticate using JWT.

### Projects
Projects belong to organizations.

### Tasks
Tasks belong to projects.

**Relationship overview:**
```
Organization
│
├── Users
│
└── Projects
       │
       └── Tasks
```

---

## 📖 API Documentation

Once the server is running, interactive API documentation is available at:
```
http://localhost:8000/docs
```

FastAPI automatically generates OpenAPI documentation.

---
### Live Demo

🔗 **[multi-tenant-saas-project-management-kim3.onrender.com/docs](https://multi-tenant-saas-project-management-kim3.onrender.com/docs)**

![API Docs](screenshots/api_docs.png)

## 🔌 Example API Endpoints

### 🔐 Authentication

**`POST /auth/login`**
```json
{
  "email": "user@example.com",
  "password": "password"
}
```

---

### 🏢 Organizations

**`POST /organizations`** — Create organization
```json
{
  "name": "Example Organization"
}
```

---

### 📋 Projects

**`POST /projects`** — Create project
```json
{
  "name": "Backend Platform",
  "organization_id": 1
}
```

---

### ✅ Tasks

**`POST /tasks`** — Create task
```json
{
  "title": "Design database schema",
  "project_id": 1
}
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/saas_db
SECRET_KEY=supersecretkey
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
```

---

## 🚀 Running the Project Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start PostgreSQL and Redis
```bash
docker-compose up
```

### 3. Run database migrations
```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

### 4. Run FastAPI server
```bash
uvicorn app.main:app --reload
```

### 5. Access API documentation
```
http://localhost:8000/docs
```

---

## ⚡ Running Background Workers

Start the Celery worker:
```bash
celery -A app.workers.celery_worker.celery_app worker --loglevel=info
```

This processes asynchronous tasks such as notifications or scheduled jobs.

---

## 🗃 Database Migrations
```bash
# Generate a new migration
alembic revision --autogenerate -m "initial migration"

# Apply migrations
alembic upgrade head
```

---

## 🧪 Running Tests
```bash
pytest
```

Tests cover authentication, project management, and task APIs.

---

## 🐳 Deployment

The project can be deployed using Docker on platforms such as **Render**.
```bash
docker-compose up --build
```

---

## 🔧 Middleware Components

### Logging Middleware
Logs request path, response time, and status codes.

### Rate Limiting Middleware
Prevents API abuse by limiting requests.

### Tenant Middleware
Extracts organization context from request headers or tokens.

---

## 🔮 Future Improvements

- [ ] Role-Based Access Control (RBAC)
- [ ] Email notification service
- [ ] Project member management
- [ ] Task deadlines and reminders
- [ ] Audit logging system
- [ ] Search and filtering APIs

---

## 🎯 Learning Objectives

This project demonstrates how to design and implement backend systems with:

- Multi-tenant data isolation
- REST API architecture
- Background job processing
- Database migrations
- Secure authentication
- Scalable backend structure

---

## 📄 License

This project is provided for **educational and portfolio purposes**.

---
