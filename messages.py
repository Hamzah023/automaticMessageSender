import os
import time
from pynput.keyboard import Key, Controller

os.system("open 'sms://+14377724191'")

time.sleep(5)

keyboard = Controller()

for i in range(101):
    keyboard.type("Bing bong")
    time.sleep(1)

    keyboard.press(Key.enter) # Presses the enter key
    keyboard.release(Key.enter) # Releases the enter key