from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class RansomwareDetectionHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"Modification detected in: {event.src_path}")

folder_to_watch = "test_files"
event_handler = RansomwareDetectionHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_watch, recursive=True)
observer.start()

print(f"Monitoring {folder_to_watch} for suspicious activities...")
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
