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
            user_id INTEGER NOT NULL, 
            task TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL DEFAULT 'High',
            due_date DATE, 
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (user_id) REFERENCES users(id) 
        );
    """)
    conn.commit()
    conn.close()

# Add a task
def add_task(task, task_description, task_priority, user_id, due_date):
    conn, cursor = get_db_connection()
    cursor.execute("INSERT INTO tasks (task, description, priority, user_id, due_date) VALUES (?, ?, ?, ?, ?)",(task, task_description, task_priority, user_id, due_date))
    conn.commit()
    conn.close()

# Fetch tasks
def get_tasks(user_id):
    conn, cursor = get_db_connection()
    cursor.execute("SELECT id, task, description, priority, status, due_date FROM tasks WHERE user_id=?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Delete a task
def delete_task(task_id, user_id):
    conn, cursor = get_db_connection()
    cursor.execute("DELETE FROM tasks WHERE id = ? AND user_id=?", (task_id,user_id))
    conn.commit()
    conn.close()

# Update task status
def update_status(task_id, new_status, user_id):
    conn, cursor = get_db_connection()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ? AND user_id=?", (new_status, task_id, user_id))
    conn.commit()
    conn.close()

# Update task priority
def update_priority(task_id, new_priority, user_id): 
    conn, cursor = get_db_connection()
    cursor.execute("UPDATE tasks SET priority = ? WHERE id = ? AND user_id=?", (new_priority, task_id, user_id))
    conn.commit()
    conn.close()
    
def update_date(task_id, new_due_date, user_id): 
    conn, cursor = get_db_connection()
    cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ? AND user_id=?", (new_due_date, task_id, user_id))
    conn.commit()
    conn.close()

# Initialize database when the module is imported
init_db()