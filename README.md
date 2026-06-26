# Healthcare Backend API

## Overview

This project is a Healthcare Backend API built using **Django**, **Django REST Framework (DRF)**, **PostgreSQL**, and **JWT Authentication**. It allows authenticated users to manage patients, doctors, and patient-doctor mappings securely.

---

## Features

* User Registration
* User Login with JWT Authentication
* Patient CRUD Operations
* Doctor CRUD Operations
* Assign Doctors to Patients
* Retrieve Doctors Assigned to a Patient
* Remove Patient-Doctor Mapping
* PostgreSQL Database
* Django ORM
* Protected APIs using JWT Authentication

---

## Technologies Used

* Python 3.x
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* psycopg2
* python-decouple (for environment variables)

---

## Project Structure

```
healthcare_backend/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── patients/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── doctors/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── mappings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── healthcare_backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/healthcare_backend.git

cd healthcare_backend
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Configuration

Create a PostgreSQL database.

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Server will run at

```
http://127.0.0.1:8000/
```

---

# API Endpoints

## Authentication

### Register

```
POST /api/auth/register/
```

Request

```json
{
    "name": "Healthcare",
    "email": "healthcare@gmail.com",
    "password": "Healthcare123"
}
```

---

### Login

```
POST /api/auth/login/
```

Request

```json
{
    "username": "healthcare@gmail.com",
    "password": "Healthcare123"
}
```

Response

```json
{
    "refresh": "...",
    "access": "..."
}
```

---

# Patient APIs

| Method | Endpoint            |
| ------ | ------------------- |
| POST   | /api/patients/      |
| GET    | /api/patients/      |
| GET    | /api/patients/<id>/ |
| PUT    | /api/patients/<id>/ |
| DELETE | /api/patients/<id>/ |

---

# Doctor APIs

| Method | Endpoint           |
| ------ | ------------------ |
| POST   | /api/doctors/      |
| GET    | /api/doctors/      |
| GET    | /api/doctors/<id>/ |
| PUT    | /api/doctors/<id>/ |
| DELETE | /api/doctors/<id>/ |

---

# Patient-Doctor Mapping APIs

| Method | Endpoint                            |
| ------ | ----------------------------------- |
| POST   | /api/mappings/                      |
| GET    | /api/mappings/                      |
| GET    | /api/mappings/patient/<patient_id>/ |
| DELETE | /api/mappings/<id>/                 |

---

## Authentication

All protected endpoints require a JWT Access Token.

Example Header

```
Authorization: Bearer <access_token>
```

---

## Validation

* JWT Authentication required
* Users can access only their own records
* Duplicate patient-doctor mappings are prevented
* Foreign key validation for patients and doctors

---

## Testing

The APIs were tested using **Postman**.

Verified operations:

* User Registration
* User Login
* Patient CRUD
* Doctor CRUD
* Patient-Doctor Mapping CRUD
* JWT Authentication
* Authorization

---

## Future Enhancements

* Pagination
* Search & Filtering
* Swagger / OpenAPI Documentation
* Docker Support
* Unit Testing
* Role-Based Access Control

---

## Author

**Shireesha Bhukya**

Healthcare Backend API Assignment
