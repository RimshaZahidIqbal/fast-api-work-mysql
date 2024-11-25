from calling.api_client import APIClient
from .api_client import url_get , url_post , api_key  ,auth_header

def Start_task(base_url_get,  base_url_post):
    base_url_get = url_get
    base_url_post = url_post
    
    fetch_endpoint = "contacts"
    post_endpoint = "whisper"


    # Initialize the API client
    api_client = APIClient(base_url_get,base_post=base_url_post,api_key=api_key, auth_header=auth_header)

    try:
        # Fetch contacts
        print("Fetching contacts...")
        contacts = api_client.fetch_contacts(fetch_endpoint)
        print(f"Fetched {len(contacts)} contacts.")

        # Send contacts to Whisper
        print("Sending contacts to Whisper...")
        for contact in contacts:
            response = api_client.post_to_whisper(post_endpoint, contact.to_dict())
            print(f"Contact {contact.id} sent successfully: {response}")

    except Exception as e:
        print(f"An error occurred: {e}")

