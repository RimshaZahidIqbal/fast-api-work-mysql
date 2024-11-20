import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Create and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Your database host
            database='test_db',  # Your database name
            user='user',  # Your database user
            password='password'  # Your database password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


