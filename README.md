# Inventory Management API

A simple REST API for managing products using Python, FastAPI, and SQLAlchemy.

This project supports basic product CRUD operations and allows the database configuration to be changed using environment variables.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- MySQL
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
│   └── database.py
│
├── tests/
│   └── test_products.py
│
├── .env.example
├── .gitignore
├── main.py
├── pytest.ini
└── README.md
```

## Setup

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

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Database Configuration

The project can run with SQLite or MySQL.

Create a `.env` file in the project root.

### SQLite

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

```env
DATABASE_TYPE=mysql
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=inventory
DATABASE_USER=root
DATABASE_PASSWORD=your_password
DATABASE_DRIVER=pymysql
```

The database connection is configured through the `.env` file, so the application code does not need to be changed when switching between supported databases.

## Run the API

Start the application:

```powershell
uvicorn main:app --reload --port 8080
```

The API will run at:

```text
http://127.0.0.1:8080
```

## API Documentation

Swagger UI is available at:

```text
http://127.0.0.1:8080/docs
```

You can use Swagger to test the APIs directly from the browser.

## API Endpoints

 Method       Endpoint                   Description 
  
 POST        /products                   Create a product 
 GET         /products                   Get all products 
 GET         /products/{product_id}      Get a product 
 PUT         /products/{product_id}      Update a product 
 DELETE      /products/{product_id}      Delete a product 

### Example Request

```json
{
    "name": "Dell Laptop",
    "price": 55000,
    "quantity": 5,
    "sku": "DELL-001"
}
```

## Testing

Run the tests with:

```powershell
pytest
```

The tests use an in-memory SQLite database.

## Code Structure

The code is separated into different layers:

```text
Route
  ↓
Service
  ↓
Repository
  ↓
Database
```

- **Routes** handle the API endpoints.
- **Services** handle the application logic.
- **Repositories** handle database operations.
- **Models** define the database tables.
- **Schemas** handle request and response validation.

Dependency injection is used for the database session and service layer to keep the code easier to test and maintain.