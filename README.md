# Django JWT Authentication API

## Endpoints

- **POST /api/auth/login/**
  - Body: `{ "username": "admin", "password": "<your_password>" }`
  - Response: `{ "token": "<jwt>", "expires": "<timestamp>" }`

- **POST /api/auth/verify/**
  - Body: `{ "token": "<jwt>" }`
  - Response: `{ "valid": true, "message": "Token is valid" }`

- **GET /api/auth/validate/**
  - Header: `Authorization: Bearer <jwt>`
  - Response: `{ "valid": true, "user": "admin", "expires": "<timestamp>" }`

## Sample User Credentials

You can use the following sample credentials for testing:

- Username: `admin`
- Password: `swayamkaushal`

- Username: `dog`
- Password: `dggcatship`

> You can log in to the Django admin at `/admin/` with the above credentials (if the user has staff/superuser rights).

## Running Locally (Docker)

## Running the Server

### With Docker (Recommended)
1. Build and run with Docker Compose:
   ```sh
   docker-compose up --build
   ```
2. The API will be available at `http://localhost:8000/`

### Without Docker (Directly on Host)
1. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # Or: source venv/bin/activate  # On Linux/Mac
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the development server:
   ```sh
   python manage.py runserver
   ```
5. The API will be available at `http://localhost:8000/`

## Deployment
- Deploy the Docker container to AWS EC2 for public access.

---


## Note

- You can log in to the Django admin at `/admin/` with the above credentials.
