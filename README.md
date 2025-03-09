# To do list 

A todo list web application with user authentication and task management capabilities.

## Key Features
- Secure Authentication
  - User registration/login with password hashing
  - Session management with Streamlit
- Task Management
  - Add tasks with title, description, priority, and due date
  - Edit existing tasks (status, priority, due date)
  - Delete tasks with confirmation
- Smart Search
  - Full-text search across titles and descriptions
  - Case-insensitive partial matching

## Technologies Used
- **Frontend**: Streamlit (Python Web Framework) 
- **Database**: SQLite with SQLAlchemy ORM


## Prerequisites
There are detailled in requirements.txt 

## How to use 

1. Authentication: Register new account or login with existing credentials
2. Task Operations: Add Task, Edit Task, Delete Task
3. Search Functionality: Type in search bar to filter tasks in real-time. Supports partial matches (e.g., "doc" finds "Submit Documents").

## Project Structure
'''
TODOAPP/
├── auth/               # Authentication modules
│   ├── auth_utils.py
│   └── database_auth.py
├── pages/              # Streamlit page components
│   ├── auth.py         # Authentication interface
│   ├── home.pys        # Main todo interface
│   └── settings.py     # User settings
├── tasks.db            # Database
├── todo_app.py         # Main application
├── requirements.txt    # Dependencies
└── README.md           # Documentation
'''