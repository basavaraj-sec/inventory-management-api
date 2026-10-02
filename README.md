# Inventory Management API

A simple REST API built with Python, FastAPI, and SQLAlchemy for managing products.

This project demonstrates CRUD operations, database configuration, validation, dependency injection, and basic automated testing.

## Features

- Create, read, update, and delete products
- FastAPI REST API
- SQLAlchemy ORM
- SQLite support
- MySQL support
- PostgreSQL configuration support
- Duplicate SKU validation
- Dependency Injection
- Pytest API tests
- Swagger API documentation

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- MySQL
- PostgreSQL
- Pytest

## Project Structure

```text
inventory-management-api/
│
├── app/
│   ├── models/
│   │   └── product.py
│   ├── repositories/
│   │   └── product.py
│   ├── routes/
│   │   └── product.py
│   ├── schemas/
│   │   └── product.py
│   ├── services/
│   │   └── product.py
│   ├── config.py
│   ├── database.py
│   └── __init__.py
│
├── tests/
│   ├── test_products.py
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Requirements

Make sure you have:

- Python 3.10+
- pip

## Installation

Clone the repository:

```powershell
git clone https://github.com/basavaraj-sec/inventory-management-api.git
cd inventory-management-api
```

Create a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## Database Configuration

Database settings are read from the `.env` file.

### SQLite

For a simple local setup:

```env
DATABASE_TYPE=sqlite
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=inventory.db
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_DRIVER=
```

### MySQL

Example configuration:

```env
DATABASE_TYPE=mysql
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=inventory
DATABASE_USER=root
DATABASE_PASSWORD=your_database_password
DATABASE_DRIVER=pymysql
```

### PostgreSQL

Example configuration:

```env
DATABASE_TYPE=postgresql
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=inventory
DATABASE_USER=postgres
DATABASE_PASSWORD=your_database_password
DATABASE_DRIVER=psycopg2
```

The database can be changed through configuration without changing the application code.

## Run the Application

Start the API:

```powershell
uvicorn main:app --reload --port 8080
```

The application will be available at:

```text
http://127.0.0.1:8080
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8080/docs
```

OpenAPI specification:

```text
http://127.0.0.1:8080/openapi.json
```

## API Endpoints

Method	Endpoint	                  Purpose
POST	/products	                  Create a new product
GET	    /products	                  Get all products
GET	    /products/{product_id}	      Get one product
PUT	    /products/{product_id}	      Update a product
DELETE	/products/{product_id}	      Delete a product

### Example Request

```json
{
    "name": "Dell Laptop",
    "price": 55000,
    "quantity": 5,
    "sku": "DELL-001"
}
```

### Example Response

```json
{
    "message": "Product created successfully",
    "product": {
        "id": 1,
        "name": "Dell Laptop",
        "price": 55000,
        "quantity": 5,
        "sku": "DELL-001"
    }
}
```

## Testing

Run the tests with:

```powershell
pytest
```

The tests use an in-memory SQLite database, so test data is separate from the application's normal database.

## Architecture

The application is organized into simple layers:

```text
Client
   |
   v
Routes
   |
   v
Service
   |
   v
Repository
   |
   v
Database
```

### Routes

Handles API requests, responses, and HTTP status codes.

### Service

Handles application logic and coordinates operations.

### Repository

Handles database operations using SQLAlchemy.

### Models

Defines the database tables.

### Schemas

Defines request and response data using Pydantic.

## Design Approach

The project keeps different responsibilities separated instead of putting everything into one file.

Dependency injection is used for the database session and product service, which also makes the application easier to test.

The database connection is configuration-based so that the database can be changed without modifying the main application logic.