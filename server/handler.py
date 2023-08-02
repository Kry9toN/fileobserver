from watchdog.events import FileSystemEventHandler
from notification.trigger import sendMessageWA

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        else:
            new_file_path = event.src_path
            print(f'New file added: {new_file_path}')
            sendMessageWA('120363040072262224@g.us', new_file_path)

event_handler = MyHandler()