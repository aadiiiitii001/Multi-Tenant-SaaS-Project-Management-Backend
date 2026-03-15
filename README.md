# Multi-Tenant SaaS Project Management Backend

A production-style backend system built using FastAPI that demonstrates how modern SaaS platforms manage multiple organizations on a single infrastructure while keeping their data isolated.

This project showcases backend architecture patterns used in real-world SaaS applications including layered architecture, JWT authentication, background workers, request middleware, and database migrations.

---

## Tech Stack

- Framework: FastAPI  
- Language: Python  
- Database: PostgreSQL  
- ORM: SQLAlchemy  
- Migrations: Alembic  
- Queue: Redis  
- Background Workers: Celery  
- Testing: Pytest  
- Containerization: Docker  
---

## Key Features
- Multi-tenant architecture with organization-based data isolation  
- REST API with clean layered architecture  
- JWT authentication system  
- Background tasks using Celery workers  
- Redis integration for async psaas_backend
- Database migrations with Alembic  
- Request logging middleware  
- Rate limiting middleware  
- Pagination utilities for scalable APIs  
- Automated API testing with Pytest

---
## Project Architecture
```
Saas
│
├── app
│ ├── api/routes
│ ├── core
│ ├── middleware
│ ├── models
│ ├── repositories
│ ├── schemas
│ ├── services
│ ├── utils
│ ├── workers
│ └── main.py
│
├── tests
│
├── alembic
│
├── requirements.txt
│
└── docker-compose.yml
```

This structure follows a **layered backend architecture**:

API Layer → Service Layer → Repository Layer → Database Models

---

## Database Design

The system contains four main entities.

- Organizations: Represents tenants using the platform.
- Users: Belong to organizations and have specific roles.
- Projects: Projects managed by organizations.
- Tasks: Work items belonging to projects.

---

## API Endpoints

- Authentication
POST /auth/login

- Organizations
POST /organizations  
GET /organizations  

- Projects
POST /projects  
GET /projects  

- Tasks
POST /tasks  
GET /tasks  


## Running the Project

### 1 Install Dependencies
pip install -r requirements.txt
### 2 Start Database and Redis
Using Docker:
docker-compose up

## 3 Run FastAPI Server
uvicorn app.main:app --reload

API documentation will be available at:
http://localhost:8000/docs


## Running Background Workers

## Start the Celery worker:
celery -A app.workers.celery_worker.celery_app worker --loglevel=info
This enables asynchronous jobs like notifications and scheduled processing.

---

## Running Tests

pytest

Tests validate:

Authentication API  
Project management API  
Task management API  

---

## Example API Request

Create Project

POST /projects


{
"name": "Backend Platform",
"organization_id": 1
}


---

## Example API Response


{
"id": 1,
"name": "Backend Platform",
"organization_id": 1
}


---

## Background Jobs

The system uses Celery for asynchronous tasks such as:

Email notifications  
Scheduled reminders  
Data processing tasks  

---

## Middleware

The backend includes custom middleware for production readiness.

Logging Middleware  
Tracks request path, execution time, and status codes.

Rate Limiting Middleware  
Prevents API abuse by limiting requests.

Tenant Middleware  
Extracts organization ID from JWT to enforce tenant isolation.

---

## Why This Project Matters

This backend demonstrates real backend engineering practices used in SaaS platforms:

Clean architecture  
Database schema design  
Secure authentication  
Background processing  
API scalability patterns  

---

## Future Improvements

Role-Based Access Control (RBAC)  
Redis caching layer  
Search and filtering APIs  
Audit logging system  
Scheduled task reminders  

---

## License
This project is provided for educational and portfolio purposes.


