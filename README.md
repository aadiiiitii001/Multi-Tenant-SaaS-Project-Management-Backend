# Multi-Tenant SaaS Project Management Backend

A production-style backend system built using FastAPI that demonstrates how modern SaaS platforms manage multiple organizations on a single infrastructure while keeping their data isolated.

This project showcases backend architecture patterns used in real-world SaaS applications including layered architecture, JWT authentication, background workers, request middleware, and database migrations.

---

## Tech Stack

Framework: FastAPI  
Language: Python  
Database: PostgreSQL  
ORM: SQLAlchemy  
Migrations: Alembic  
Queue: Redis  
Background Workers: Celery  
Testing: Pytest  
Containerization: Docker  

---

## Key Features

Multi-tenant architecture with organization-based data isolation  
REST API with clean layered architecture  
JWT authentication system  
Background tasks using Celery workers  
Redis integration for async processing  
Database migrations with Alembic  
Request logging middleware  
Rate limiting middleware  
Pagination utilities for scalable APIs  
Automated API testing with Pytest  

---

## Project Architecture
