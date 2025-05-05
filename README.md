📝 FastAPI Task Manager

A simple and secure Task Management API built using FastAPI, JWT Authentication, and MySQL. <br>
🚀 Features

    User Registration & Login

    JWT-based Authentication

    CRUD operations for tasks

    MySQL Database Integration

    SQLAlchemy ORM


⚙️ Prerequisites

    Python 3.10+

    MySQL server running locally

    virtualenv (recommended)

🛠️ Setup Instructions
1. Clone the Repository

git clone https://github.com/Sadiya194112/FastAPI-CRUD.git
cd FastAPI CRUD

2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate      # On Unix/MacOS
venv\Scripts\activate         # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in the root directory and add:

secret = 8b68a6c218b450eca9621f7d96d82550
algorithm = HS256

    🔐 Keep your secret key secure in a production environment.

5. Configure MySQL

Ensure you have a MySQL server running locally and a database named first_db:

CREATE DATABASE first_db;

Update the connection string in database.py if your username or password differs:

SQLALCHEMY_DB_URL = "mysql+pymysql://<user>:<password>@localhost/first_db"

6. Run the Application

uvicorn main:app --reload

Server will run at: http://127.0.0.1:8000
🔐 Authentication Flow

    Register a user via POST /users/

    Login to get a JWT token via POST /login/

    Use the token in the Authorization header:
    Bearer <your-token> to access protected routes like:

        POST /tasks/

        PUT /tasks/{task_id}

        DELETE /tasks/{task_id}

📬 API Endpoints
Method	Endpoint	Description	Auth Required
POST	/users/	Register new user	❌
POST	/login/	Login and get token	❌
GET	/tasks/	Get all tasks	❌
POST	/tasks/	Create new task	✅
PUT	/tasks/{task_id}	Update existing task	✅
DELETE	/tasks/{task_id}	Delete a task	✅
🧪 Testing the API

You can test your API using tools like:

    Postman

    cURL

    FastAPI Docs

