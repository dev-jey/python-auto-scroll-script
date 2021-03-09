import pyautogui
import random
from time import sleep

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

hot_keys = ['ctrl', 'shift', 'esc']


def run_gui():
    pyautogui.moveTo(600, random.randint(300, 500))
    #pyautogui.moveRel(0, 10)
    # pyautogui.keyDown(random.choice(hot_keys))
    # pyautogui.keyUp(random.choice(hot_keys))
    # screen_size = pyautogui.size()
    # current_screen_position = pyautogui.position()
    pyautogui.scroll(-1)


while True:
    for i in range(1, 5):
        run_gui()
        sleep(9)
    pyautogui.scroll(random.randint(100, 200))
