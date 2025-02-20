import sqlite3

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    return conn, conn.cursor()

# Create tasks table 
def init_db():
    conn, cursor = get_db_connection()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            description TEXT NOT NULL, 
            status TEXT DEFAULT 'Pending'
        )
    """)
    conn.commit()
    conn.close()

# Add a task
def add_task(task, task_description):
    conn, cursor = get_db_connection()
    cursor.execute("INSERT INTO tasks (task, description) VALUES ((?),(?))", (task,task_description))
    conn.commit()
    conn.close()

# Fetch tasks
def get_tasks():
    conn, cursor = get_db_connection()
    cursor.execute("SELECT id, task, description, status FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Delete a task
def delete_task(task_id):
    conn, cursor = get_db_connection()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Update task status
def update_status(task_id, new_status):
    conn, cursor = get_db_connection()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()

# Fetch the id of the lask task added
def get_last_task_id():
    conn, cursor = get_db_connection()
    cursor.execute("SELECT id FROM tasks ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
    
# Initialize database when the module is imported
init_db()