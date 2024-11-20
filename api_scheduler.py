import requests
from apscheduler.schedulers.background import BackgroundScheduler
import time


class APICaller:
    def __init__(self, url: str, interval: int):
        """
        Initialize the API caller.
        
        :param url: The API URL to be called.
        :param interval: Interval in seconds between calls.
        """
        self.url = url
        self.interval = interval
        self.scheduler = BackgroundScheduler()

    def call_api(self):
        """
        Method to call the API and print the response.
        """
        try:
            print(f"Calling API: {self.url}")
            response = requests.get(self.url)
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error calling API: {e}")

    def start(self):
        """
        Start the scheduler to call the API infinitely at the specified interval.
        """
        print(f"Starting API caller with an interval of {self.interval} seconds.")
        self.scheduler.add_job(self.call_api, 'interval', seconds=self.interval)
        self.scheduler.start()

        try:
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            print("Shutting down scheduler.")
            self.scheduler.shutdown()


if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/"  # API endpoint
    interval_seconds = 5    # 5 minutes = 5*60

    caller = APICaller(api_url, interval_seconds)
    caller.start()
