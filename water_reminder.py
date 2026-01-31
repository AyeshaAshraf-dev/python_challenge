import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drinking Water Reminder!",
            message = "Drinking enough water is essential for optimal health, helping to regulate body temperature, cushion joints, and transport nutrients.",
            app_name = "WaterReminder",
            timeout = 5
    )
        time.sleep(60*60)