import requests
from calling.contact import Contact

class APIClient:

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def fetch_contacts(self, endpoint):
    
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  
        data = response.json()

        contacts = [Contact(**item) for item in data.get("contacts", [])]
        return contacts

    def post_to_whisper(self, endpoint, contact_data):
    
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=contact_data, headers=self.headers)
        response.raise_for_status()
        return response.json()
