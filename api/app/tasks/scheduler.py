from apscheduler.schedulers.background import BackgroundScheduler
from app.services.contact_service import fetch_contacts

scheduler = BackgroundScheduler()

def schedule_tasks():
    """Schedules the fetch_contacts task every 5 minutes."""
    scheduler.add_job(fetch_contacts, 'interval', minutes=0.5)
    scheduler.start()
