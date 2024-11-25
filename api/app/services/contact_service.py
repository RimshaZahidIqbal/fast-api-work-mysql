from app.database.connection import get_db_connection

def fetch_contacts():
    """Fetch contacts from the database by calling a stored procedure."""
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.callproc('get_all_contacts')

            contacts = []
            for result in cursor.stored_results():
                contacts = result.fetchall()  
            return contacts if contacts else {"message": "No contacts found"}

        except Exception as e:
            print(f"Error fetching contacts: {e}")
            return {"error": str(e)}

        finally:
            cursor.close()
            connection.close()
    else:
        return {"error": "Database connection failed"}
