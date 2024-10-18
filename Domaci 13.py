import subprocess
import webbrowser
import time
from win10toast import ToastNotifier
import random
import threading


toaster = ToastNotifier()
toaster.show_toast("Reminder!", "Take a break!", duration=5)

messages = [
    "Take a break!",
    "It's time to chill",
    "Vreme je za pauzu",
    "Predugo si ucio, napravi 10 mintua pauze"
]



subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2024.2.3/bin/pycharm64.exe"])

webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://itskola.net")

def notification():
    while True:
        toaster.show_toast("Reminder!", random.choice(messages), duration=5)
        time.sleep(2)

thread_notification = threading.Thread(target=notification)
thread_notification.start()

print("Prosao si beskonacnu petlju!")
