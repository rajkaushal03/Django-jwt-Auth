# Project Process Summary

This document summarizes the steps taken to build, design, and run the Django JWT Authentication API project, with a focus on backend logic and human-understandable explanations.

---

## 1. Project Setup
- **Django project** initialized with Django and Django REST Framework (DRF).
- **Docker** and **docker-compose** configured for easy local development and deployment.
- **requirements.txt** lists all dependencies.

## 2. App Structure
- Two main Django apps:
  - `authapi`: Handles project settings, URLs, and the homepage UI.
  - `authentication`: Contains all authentication logic (login, verify, validate), models, and API endpoints.

## 3. JWT Authentication Flow
- **Login** (`/api/auth/login/`):
  - User submits username and password.
  - Backend checks credentials using Django's authentication system.
  - If valid, a JWT token is generated and returned with an expiry timestamp.
- **Verify** (`/api/auth/verify/`):
  - User submits a JWT token.
  - Backend decodes and checks the token's validity and expiry.
  - Returns whether the token is valid or not.
- **Validate** (`/api/auth/validate/`):
  - User sends a JWT token in the Authorization header.
  - Backend authenticates the token and, if valid, returns user info and expiry.

## 4. Homepage UI
- Built with Bootstrap and custom CSS for a modern, dark, split layout.
- Left: API info, endpoints, sample credentials.
- Right: Interactive forms for login, verify, and validate, with real-time results.

## 5. Sample Credentials
- Provided in both the UI and README for easy testing.
- Example users: `admin`/`swayamkaushal`, `dog`/`dggcatship`.

## 6. Admin Access
- Django admin available at `/admin/` for user and token management.

## 7. Running & Deployment
- Use `docker-compose up --build` to start the project locally.
- API available at `http://localhost:8000/`.
- Deployable to AWS EC2 or any Docker-compatible host.

---

## Backend Implementation Details
- **Views**: API endpoints are implemented as Django REST Framework views in `authentication/views.py`.
- **Models**: User model and any custom authentication models are in `authentication/models.py`.
- **URLs**: All API endpoints are routed via `authentication/urls.py` and included in the main `authapi/urls.py`.
- **JWT Handling**: Uses a Python JWT library (e.g., PyJWT) to encode/decode tokens securely.
- **Security**: Passwords are never stored or returned; only tokens are sent to the client.

---

## Summary
- The project is a clean, production-ready JWT authentication API with a professional UI and clear backend logic.
- All unnecessary files are documented for removal in `PROJECT_BLUEPRINT.md`.
- For more details, see the main [README.md](./README.md) and [PROJECT_BLUEPRINT.md](./PROJECT_BLUEPRINT.md).
