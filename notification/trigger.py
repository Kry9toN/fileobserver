import platform
import subprocess

def sendMessageWA(id, file):
    startupinfo = None
    if platform.system() == 'Windows':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.check_output(['C:/Program Files/nodejs/npx.cmd', 'mudslide', 'send-file', id, file], shell = False, startupinfo=startupinfo).decode()
    if platform.system() == 'Linux':
        subprocess.check_output(['npx', 'mudslide', 'send-file', id, file], shell = False, startupinfo=startupinfo).decode()
    return True