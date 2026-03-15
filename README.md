# Multi-Tenant SaaS Project Management Backend

A production-style backend system for a multi-tenant SaaS project management platform built with FastAPI. The system allows multiple organizations to use the same application while keeping their data securely isolated.

Each organization manages its own users, projects, and tasks through a RESTful API. The architecture follows modern backend engineering patterns such as layered architecture, background workers, middleware processing, and containerized deployment.

This project demonstrates real-world backend concepts commonly used in SaaS platforms.

---

# Key Features

- Multi-tenant architecture with organization-based data isolation  
- JWT-based authentication and authorization  
- Layered backend architecture (API, Services, Repositories)  
- Asynchronous background tasks using Celery  
- Redis integration for message brokering  
- Database migrations using Alembic  
- Request logging middleware  
- Rate limiting middleware  
- Tenant context middleware  
- Pagination utilities for scalable APIs  
- Docker-based deployment  
- Automated testing with Pytest

---

# Technology Stack

| Component | Technology |
|----------|-------------|
| Backend Framework | FastAPI |
| Language | Python |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Queue System | Redis |
| Background Workers | Celery |
| Authentication | JWT |
| Testing | Pytest |
| Containerization | Docker |

---

# System Architecture

The backend follows a **layered architecture** commonly used in scalable SaaS applications.
