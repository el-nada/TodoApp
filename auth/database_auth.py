import sqlite3
from auth.auth_utils import hash_password, generate_salt, verify_password

def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    return conn, conn.cursor()

def create_auth_db():
    conn, cursor = get_db_connection()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_user(username, password):
    conn, cursor = get_db_connection()
    try:
        salt = generate_salt()
        password_hash = hash_password(password, salt)
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",(username, password_hash, salt))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username exists
    finally:
        conn.close()

def get_id(username):
    conn, cursor = get_db_connection()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        raise ValueError(f"User '{username}' not found in the database.")

def verify_user(username, password):
    conn, cursor = get_db_connection()
    cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?",(username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        stored_hash, salt = result
        return verify_password(stored_hash, password, salt)
    return False

def update_password(username, new_password): 
    conn, cursor = get_db_connection()
    salt = generate_salt()
    password_hash = hash_password(new_password, salt)
    cursor.execute("UPDATE users SET password_hash = ?, salt = ? WHERE username = ?", (password_hash,salt, username))
    conn.commit()
    conn.close()

# Initialize when module loads
create_auth_db()