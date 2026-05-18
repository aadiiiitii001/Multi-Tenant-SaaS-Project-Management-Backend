# 🏢 Multi-Tenant SaaS Project Management Backend
 
<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-5-37814A?style=for-the-badge&logo=celery&logoColor=white)

A production-style backend where multiple organizations share one platform with strict data isolation.

[🚀 Live API Docs](https://multi-tenant-saas-project-management-kim3.onrender.com/docs) · [🌐 Portfolio Page](https://aadiiiitii001.github.io/Multi-Tenant-SaaS-Project-Management-Backend/) · [📂 Source Code](https://github.com/aadiiiitii001/Multi-Tenant-SaaS-Project-Management-Backend)
 
</div>

 
## 📌 Overview
 
This project implements a **multi-tenant SaaS backend** — the same architecture used by platforms like Jira, Notion, and Asana — where multiple organizations use a single application while their data remains completely isolated from each other.
 
Each organization independently manages its **users, projects, and tasks** through a secure REST API. The system is built with scalability, security, and clean architecture in mind.
 
> **Why multi-tenancy?** It's a core concept in enterprise SaaS. Instead of deploying separate backends for each customer, one backend serves all — with strict boundaries between tenants. This is a senior-level design pattern.
 
---
 
## ✨ Key Features
 
| Feature | Description |
|---|---|
| 🏢 **Multi-Tenancy** | Org-scoped data isolation across all entities via tenant middleware |
| 🔐 **JWT Auth** | Stateless token-based authentication with secure password hashing |
| 🧱 **Layered Architecture** | Clean separation: Routes → Services → Repositories → Models |
| ⚡ **Async Background Jobs** | Celery + Redis for non-blocking task processing |
| 🛡️ **Rate Limiting** | Middleware-level throttling to prevent API abuse |
| 📋 **DB Migrations** | Alembic for version-controlled schema management |
| 🐳 **Dockerized** | Full Docker Compose setup for local and production environments |
| 🧪 **Automated Tests** | Pytest suite covering auth, projects, and task APIs |
 
---
 
## 🛠️ Tech Stack
 
```
Backend       →  Python · FastAPI
Database      →  PostgreSQL · SQLAlchemy ORM · Alembic migrations
Async Queue   →  Celery · Redis (message broker)
Auth          →  JWT (JSON Web Tokens) · bcrypt password hashing
DevOps        →  Docker · Docker Compose · Render (deployment)
Testing       →  Pytest
```
 
---
 
## 🏗️ System Architecture
 
```
Client Request
      │
      ▼
┌─────────────────────────────────┐
│           Middleware             │
│  Rate Limiting · Logging ·      │
│  Tenant Context Detection       │
└────────────────┬────────────────┘
                 │
                 ▼
          ┌─────────────┐
          │  API Routes  │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │Service Layer │   ←── Business logic lives here
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │  Repository  │   ←── All DB queries abstracted here
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │  PostgreSQL  │
          └─────────────┘
 
Async Path:
Service Layer → Celery Worker → Redis Broker → Background Task
```
 
---
 
## 📁 Project Structure
 
```
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── auth.py            # Login, token endpoints
│   │       ├── organizations.py   # Tenant management
│   │       ├── projects.py        # Project CRUD
│   │       └── tasks.py           # Task CRUD
│   │
│   ├── core/
│   │   ├── config.py              # Settings & environment variables
│   │   ├── database.py            # DB session management
│   │   ├── dependencies.py        # Dependency injection
│   │   └── security.py            # JWT utilities
│   │
│   ├── middleware/
│   │   ├── logging.py             # Request/response logging
│   │   ├── rate_limit.py          # API rate limiting
│   │   └── tenant.py              # Org context extraction
│   │
│   ├── models/                    # SQLAlchemy ORM models
│   ├── repositories/              # Database query abstraction
│   ├── schemas/                   # Pydantic request/response schemas
│   ├── services/                  # Business logic layer
│   ├── workers/
│   │   └── celery_worker.py       # Background job definitions
│   └── main.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_projects.py
│   └── test_tasks.py
│
├── alembic/                       # DB migration scripts
├── docker-compose.yml
├── requirements.txt
└── README.md
```
 
---
 
## 🗄️ Database Design
 
```
Organization (Tenant)
│
├── Users          (belong to one organization)
│
└── Projects       (scoped to one organization)
        │
        └── Tasks  (scoped to one project)
```
 
All queries are automatically scoped to the requesting organization's ID — a user in Organization A **can never access** data from Organization B.
 
---
 
## 🔌 API Endpoints
 
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/login` | Issue JWT token |
| `POST` | `/organizations/` | Create a new organization (tenant) |
| `GET` | `/organizations/` | List all organizations |
| `POST` | `/projects/` | Create a project (scoped to org) |
| `GET` | `/projects/` | Get projects for current org |
| `POST` | `/tasks/` | Create a task |
| `GET` | `/tasks/` | Get tasks (scoped to org) |
 
> 📖 Full interactive documentation available at [`/docs`](https://multi-tenant-saas-project-management-kim3.onrender.com/docs) (Swagger UI auto-generated by FastAPI)
 
---
 
## ⚙️ Local Setup
 
### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL (or use Docker)
### 1. Clone the repository
```bash
git clone https://github.com/aadiiiitii001/Multi-Tenant-SaaS-Project-Management-Backend.git
cd Multi-Tenant-SaaS-Project-Management-Backend
```
 
### 2. Create environment file
```bash
# Create .env in project root
DATABASE_URL=postgresql://postgres:password@localhost:5432/saas_db
SECRET_KEY=your-super-secret-key-here
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
```
 
### 3. Start services with Docker
```bash
docker-compose up
```
 
### 4. Install dependencies & run migrations
```bash
pip install -r requirements.txt
alembic upgrade head
```
 
### 5. Start the API server
```bash
uvicorn app.main:app --reload
```
 
### 6. Open API docs
```
http://localhost:8000/docs
```
 
---
 
## 🔄 Running Background Workers
 
```bash
celery -A app.workers.celery_worker.celery_app worker --loglevel=info
```
 
Celery handles async operations like notifications and scheduled jobs without blocking the API response.
 
---
 
## 🧪 Running Tests
 
```bash
pytest
```
 
Tests cover authentication flows, organization creation, project and task management with proper tenant isolation assertions.
 
---
 
## 🚀 Deployment
 
This project is deployed on **Render** with:
- PostgreSQL hosted database
- Redis hosted instance
- Auto-deploy from the `main` branch
---
 
## 🔮 Future Improvements
 
- [ ] Role-Based Access Control (RBAC) — admin, member, viewer roles
- [ ] Email notification service
- [ ] Project member management & invites
- [ ] Task deadlines, priorities & reminders
- [ ] Audit logging system
- [ ] Search & filtering APIs
- [ ] Webhook support for integrations
---
 
## 🎯 What This Project Demonstrates
 
This project showcases real-world backend engineering skills:
 
- **System design** — multi-tenant SaaS architecture from scratch
- **Security** — JWT auth, password hashing, org-scoped data access
- **Clean code** — layered architecture with clear separation of concerns
- **Infrastructure** — Docker, background workers, database migrations
- **Production mindset** — rate limiting, logging middleware, error handling
- **Testing** — automated test coverage with Pytest
---
 
## 👨‍💻 Author
 
**Aditi Nayak** · Backend Engineer
 
[![GitHub](https://img.shields.io/badge/GitHub-aadiiiitii001-181717?style=flat&logo=github)](https://github.com/aadiiiitii001)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live-009688?style=flat&logo=vercel)](https://aadiiiitii001.github.io/Multi-Tenant-SaaS-Project-Management-Backend/)
 
---
 
<div align="center">
  <sub>Built with ❤️ for learning and portfolio purposes</sub>
</div>
 
