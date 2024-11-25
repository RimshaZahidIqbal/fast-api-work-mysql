import requests
from apscheduler.schedulers.background import BackgroundScheduler
import time

class APICaller:
    def __init__(self, url: str, interval: int):
        self.url = url
        self.interval = interval
        self.scheduler = BackgroundScheduler()

    def call_api(self):
        try:
            print(f"Calling API: {self.url}")
            response = requests.get(self.url)
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error calling API: {e}")

    def start(self):
        print(f"Starting API caller with an interval of {self.interval} seconds.")
        self.scheduler.add_job(self.call_api, 'interval', seconds=self.interval)
        self.scheduler.start()

        try:
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            print("Shutting down scheduler.")
            self.scheduler.shutdown()
