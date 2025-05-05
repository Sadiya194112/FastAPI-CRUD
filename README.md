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
1. Clone the Repository <br>

    git clone https://github.com/Sadiya194112/FastAPI-CRUD.git
    cd FastAPI CRUD

2. Create and Activate Virtual Environment <br>

    python -m venv venv <br>
    source venv/bin/activate      # On Unix/MacOS <br>
    venv\Scripts\activate         # On Windows <br>

3. Install Dependencies <br>

    pip install -r requirements.txt <br>

4. Set Up Environment Variables <br>
    
    Create a .env file in the root directory and add: <br>
    
    secret = 8b68a6c218b450eca9621f7d96d82550 <br>
    algorithm = HS256    <br>

    🔐 Keep your secret key secure in a production environment.

5. Configure MySQL <br>

    Ensure you have a MySQL server running locally and a database named first_db: <br>
    
    CREATE DATABASE first_db;    <br>
    
    Update the connection string in database.py if your username or password differs: <br>
    
    SQLALCHEMY_DB_URL = "mysql+pymysql://<user>:<password>@localhost/first_db" <br>

6. Run the Application

    uvicorn main:app --reload <br>
    
    Server will run at: http://127.0.0.1:8001 <br>
🔐 Authentication Flow    <br>

    Register a user via POST /users/ <br>

    Login to get a JWT token via POST /login/    <br>

    Use the token in the Authorization header:    <br>
    Bearer <your-token> to access protected routes like:    <br>

        POST /tasks/    <br>

        PUT /tasks/{task_id}     <br>

        DELETE /tasks/{task_id}    <br>

📬 API Endpoints
    Method	    Endpoint	        Description	        Auth Required <br>
    POST	    /users/	            Register new user	    ❌    <br>
    POST	    /login/	            Login and get token	    ❌    <br>
    GET	        /tasks/	            Get all tasks	        ❌    <br>
    POST	    /tasks/	            Create new task	        ✅    <br>
    PUT	        /tasks/{task_id}	Update existing task	✅    <br>
    DELETE	    /tasks/{task_id}    Delete a task	        ✅    <br>
🧪 Testing the API    <br>

You can test your API using tools like:    <br>

    Postman    <br>

    cURL    <br>

    FastAPI Docs

