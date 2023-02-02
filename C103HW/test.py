import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/Vraj/Desktop/PYTHONBY/HW/C103HW/"
to_dir = "C:/Users/Vraj/Desktop/PYTHONBY/HW/C103HW/Hi"


# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print (f"Oops! Someone deleted {event.src_path}!")

# Initialize Event Handler Class
# Initialize Observer
# Schedule the Observer
# Start the Observer

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()