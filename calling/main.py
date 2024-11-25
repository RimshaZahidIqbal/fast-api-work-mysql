from calling.api_client import APIClient

def main():
    base_url_get = " http://0.0.0.0:8000/"
    base_url_post = "https://whisper.example.com/api"
    headers = {"Authorization": "******"}

    # Endpoints
    fetch_endpoint = "contacts"
    post_endpoint = "whisper"

    # Initialize the API client
    api_client = APIClient(base_url_get, headers)

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

if __name__ == "__main__":
    main()
