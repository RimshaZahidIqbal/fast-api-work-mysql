from fastapi import APIRouter
from app.services.invoice_service import fetch_invoices
from app.services.contact_service import fetch_contacts

router = APIRouter()

@router.get("/")
def read_invoices():
    """GET endpoint to fetch invoices."""
    data = fetch_invoices()
    if data:
        return {"data": data}
    return {"message": "No data fetched from the database"}
@router.get("/contacts")
def read_contacts():
    """GET endpoint to fetch contacts."""
    data = fetch_contacts()
    if data:
        return {"data": data}
    return {"message": "No data fetched from the database"}