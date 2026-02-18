# CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with FastAPI and PostgreSQL.

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Language:** Python 3.x

## Prerequisites

- Python 3.8+
- PostgreSQL installed and running
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/CRUD.git
   cd CRUD
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the database**
   
   Update the database connection string in `db.py`:
   ```python
   SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"
   ```

6. **Create the database tables**
   ```bash
   python -c "from db import create_table; create_table()"
   ```

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, access the interactive API docs:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/items` | Get all items |
| GET | `/items/{id}` | Get item by ID |
| POST | `/items` | Create new item |
| PUT | `/items/{id}` | Update item |
| DELETE | `/items/{id}` | Delete item |

## Project Structure

```
CRUD/
├── main.py          # FastAPI application entry point
├── db.py            # Database configuration
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── requirements.txt # Project dependencies
├── .gitignore       # Git ignore file
└── README.md        # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
