import pyautogui
from time import sleep

print(">>>>>>>>>>>>>>>>> Working >>>>>>>>>>>>>>>")


def run_gui():
    pyautogui.moveTo(100, 150)
    pyautogui.moveRel(0, 10)


while True:
    run_gui()
    sleep(3)
