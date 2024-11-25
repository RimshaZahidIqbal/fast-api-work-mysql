import requests
from contact import Contact

class APIClient:
  
    def __init__(self, base_url , base_post, api_key, auth_header):
       
        self.base_url = base_url
        self.base_post_url = base_post
        self.headers = {
            "Authorization": f"Basic {auth_header}",
            "x-api-key": api_key,
            "Content-Type": "application/json",
        }

    def fetch_contacts(self, endpoint):
     
        url = f"{self.base_url}/{endpoint}"
        # response = requests.get(url, headers=self.headers)
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        contacts = [Contact(**item) for item in data.get("contacts", [])]
        return contacts

    def post_to_whisper(self, endpoint, contact_data):
        
        url = f"{self.base_post_url}/{endpoint}"
        response = requests.post(url, json=contact_data, headers=self.headers)
        response.raise_for_status()
        return response.json()
