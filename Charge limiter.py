import psutil
from plyer import notification
import time

def get_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    return plugged, percent

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def main():
    while True:
        plugged, percent = get_battery_status()

        if plugged and percent > 90:
            show_notification('Battery Monitor', f'Warning: Battery at {percent}% - Unplug Charger!')

        elif not plugged and percent < 30:
            show_notification('Battery Monitor', f'Emergency: Battery critically low at {percent}% - Plug in Charger!')

        time.sleep(60)  # Check every 1 minute (adjust as needed)

if __name__ == "__main__":
    main()
