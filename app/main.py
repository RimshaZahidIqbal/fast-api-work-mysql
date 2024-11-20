from fastapi import FastAPI
import mysql.connector
from apscheduler.schedulers.background import BackgroundScheduler
from .database import get_db_connection  # Using relative import for 'get_db_connection'

app = FastAPI()

def fetch_data_from_db():
    """Fetch data from the database by calling a stored procedure."""
    connection = get_db_connection()  # Ensure this is fetching a valid connection
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            # Call the stored procedure (example for MySQL)
            cursor.callproc('get_all_invoices')

            # Fetch the result of the stored procedure
            data = []
            for result in cursor.stored_results():
                data = result.fetchall()
                print("Fetched Data:", data)  # Or process it as needed

            if not data:
                print("No data returned from stored procedure.")
            return data  # Optionally return or process the data further

        except mysql.connector.Error as err:
            print(f"Error executing stored procedure: {err}")
            return {"error": str(err)}  # Returning error in response
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to establish a database connection.")
        return {"error": "Failed to connect to the database."}

# Schedule the task to run every 5 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_data_from_db, 'interval', minutes=5)
scheduler.start()

@app.get("/")
def read_root():
    """GET endpoint to trigger the procedure manually."""
    data = fetch_data_from_db()
    if data:
        return {    "data": data}
    else:
        return {"message": "No data fetched from the database"}