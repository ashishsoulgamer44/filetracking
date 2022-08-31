import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Ashish Antony/Downloads"

# Event Handler Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self,event):
       print(f"Hey,{event.src_paths} has been canceled")
    #2_on_deleted
    def on_deleted(self,event):
       print(f"Oops! someone deleted {event.src_paths}!")
    #3_on_modified
    def on_modified(self,event):
       print(f"Hey there!,{event.src_paths} has been modified")
    #4_on_moved
    def on_moved(self,event):
        print(f"Someone removed,{event.src_paths} to {event.dest_paths}")


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

try:
    while True:
       time.sleep(2)
       print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()






