"""DB for Homework project tracking system for projects."""

#region Imports
import sqlite3
#endregion

#region Constants
DB_NAME = "projects.db"
#endregion

#region Database Functions
def create_connection():
	conn = sqlite3.connect(DB_NAME)
	return conn
#endregion

#region Initialisation Function
def init_db():
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS projects (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						name TEXT NOT NULL,
						description TEXT,
						status TEXT)''')
	conn.commit()
	conn.close()
#endregion

#region CRUD Functions

# Create
def add_project(name, description, status):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO projects (name, description, status) VALUES (?, ?, ?)", (name, description, status))
	conn.commit()
	conn.close()

# Read
def get_project(proj_id):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM projects WHERE id=?", (proj_id,))
	result = cursor.fetchone()
	conn.close()
	return result

# Read All
def get_all_projects():
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM projects")
	results = cursor.fetchall()
	conn.close()
	return results

# Update
def update_project(proj_id, name, description, status):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("UPDATE projects SET name=?, description=?, status=? WHERE id=?", (name, description, status, proj_id))
	conn.commit()
	conn.close()

# Delete
def delete_project(proj_id):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM projects WHERE id=?", (proj_id,))
	conn.commit()
	conn.close()
#endregion