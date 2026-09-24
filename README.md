# Python Auth & CRUD Demo

A learning project built with **Python and FastAPI** to explore REST API development, authentication, authorization, JWT, OAuth2, role-based access, database integration, and CRUD operations.

## 🚀 Features

* FastAPI REST API
* Product CRUD operations

  * Create product
  * Get all products
  * Get product by ID
  * Update product
  * Delete product
* SQLAlchemy database integration
* Automatic database table creation
* Initial product seed data
* Request validation using Pydantic
* HTTP exception handling
* CORS support for the frontend
* Authentication and authorization learning setup
* JWT / OAuth2 concepts
* Role-based access control
* Frontend integration

## 🛠️ Technologies

* Python 3
* FastAPI
* SQLAlchemy
* Pydantic
* JWT
* OAuth2
* Argon2 password hashing
* SQLite / relational database
* HTML / JavaScript frontend

## 📁 Project Structure

```text
Python_auth_and_CRUD_demo/
│
├── auth/
│   └── Authentication and authorization related code
│
├── frontend/
│   └── Frontend application
│
├── database.py
│   └── Database connection and SQLAlchemy session
│
├── database_models.py
│   └── SQLAlchemy database models
│
├── models.py
│   └── Pydantic request/response models
│
├── main.py
│   └── FastAPI application and API endpoints
│
├── requirement.txt
│   └── Python dependencies
│
└── README.md
```

The repository currently contains the `auth`, `frontend`, database/model files, `main.py`, and dependency file shown above.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/rahulrai1989/Python_auth_and_CRUD_demo.git
cd Python_auth_and_CRUD_demo
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirement.txt
```

The current dependency file includes Argon2 support through Passlib, `python-jose` for cryptographic/JWT functionality, `python-multipart`, and Pydantic email validation.

## ▶️ Run the API

Start the FastAPI application with:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## 🔗 API Endpoints

### Health / Welcome

```http
GET /
```

Returns:

```text
Hello, welcome to the Backend!
```

### Products

Get all products:

```http
GET /products
```

Get a product:

```http
GET /products/{product_id}
```

Create a product:

```http
POST /products
```

Example:

```json
{
  "id": 5,
  "name": "Product 5",
  "description": "Description of Product 5",
  "price": 25.99,
  "quantity": 100
}
```

Update a product:

```http
PUT /products/{id}
```

Delete a product:

```http
DELETE /products/{id}
```

The current `main.py` implements these product endpoints and returns appropriate HTTP status codes for create, update, and not-found cases.

## 🗄️ Database

The application uses SQLAlchemy for database access.

Database tables are created automatically when the application starts:

```python
database_models.Base.metadata.create_all(bind=engine)
```

The application also inserts sample products when the product table is empty.

## 🔐 Authentication & Authorization

This project is also used to learn authentication and authorization concepts with FastAPI, including:

* User authentication
* Password hashing
* JWT authentication
* OAuth2
* Role-based access control
* Protected API endpoints

Authentication-related code is organised under the `auth` directory.

## 🌐 CORS

The API currently allows requests from the local frontend:

```text
http://localhost:3000
```

This allows the frontend application to communicate with the FastAPI backend during local development.

## 🎯 Purpose

This is primarily a **learning and demonstration project** for understanding how to build a backend API using FastAPI and Python.

The main areas covered are:

* REST API development
* CRUD operations
* Database integration
* Data validation
* Authentication
* Authorization
* JWT
* OAuth2
* Role-based access control
* Frontend/backend integration

## 👨‍💻 Author

**Rahul**

GitHub:
https://github.com/rahulrai1989
