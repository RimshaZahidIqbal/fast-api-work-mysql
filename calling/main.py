from .task import Start_task
import schedule
import time


schedule.every(5).minutes.do(Start_task)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
