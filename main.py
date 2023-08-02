import time
from server.handler import event_handler
from watchdog.observers import Observer

if __name__ == "__main__":
    # Ganti 'YOUR_DIRECTORY_PATH' dengan jalur (path) direktori yang ingin Anda pantau.
    path = "YOUR_DIRECTORY_PATH"

    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()