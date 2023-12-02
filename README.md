# Healthy-Laptop-Battery
Some python programmes related to keeping your laptop's battery healthy

## Overview

Battery Monitor is a Python script designed to help users manage their laptop battery health. The script monitors the battery status and displays notifications when certain thresholds are reached.

## Features

- *Overcharging Warning:* Displays a notification when the battery level exceeds 85% while the laptop is plugged in.

- *Emergency Low Battery Warning:* Provides an urgent notification when the battery level falls below 30% while unplugged, indicating a critical battery situation.

## Usage

1. *Install Dependencies:*
   - Ensure you have Python installed on your system.
   - Install required Python packages using `pip install psutil plyer`.

2. *Run the Script:*
   - Execute the `battery_monitor.py` script to start monitoring your laptop's battery.
   - You can also make it run automatically by using Task Scheduler (Built in with Windows). Steps as follows:-
     - Open Task Scheduler by search menu or by run dialog using `taskschd.msc`
     - Create a Basic Task from right-hand actions pane
     - Give a name (and description, if you wish to) and click on next
     - Select the start timing of task (preferably on startup or on user log on)
     - Select "Start a program" in actions tab
     - In "Program/Script" field, provide the path to your python executable (can be obtained by running `where python` on command prompt)
     - If you want to run the script without opening a console, just type a "w" at the end of python in executable (for example, if your path is `C:\Python39\python.exe`, change it to `C:\Python39\pythonw.exe`)
     - In "Add arguments (optional)" field, add the complete path of the `battery_monitor.py`
     - Review settings and it is set up successfully
     - From the schedule explorer, click on the name you gave and "Run" it from right-hand actions pane


3. *Notifications:*
   - You will receive notifications based on your battery status:
     - Overcharging Warning when the battery is above 85% and plugged in.
     - Emergency Low Battery Warning when the battery is below 30% and unplugged.

4. *Stop Monitoring:*
   - To stop the script, manually terminate the execution or "Stop" the schedule via Windows Scheduler.

## Additional Notes

- *Automation:*
  - Instead of Task Scheduler, you can also use 3rd party service managers like NSSM (Non Sucking Service Manager)

- *Customization:*
  - Modify the script as needed, e.g., adjusting notification timeout, checking frequency, or adding extra functionality.

- *Dependencies:*
  - The script relies on the `psutil` and `plyer` Python packages. Ensure they are installed before running the script.

## Author

- Ashish Mishra
