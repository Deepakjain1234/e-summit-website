import pyautogui as p
import time

time.sleep(5)

for i in range(100):
    p.hotkey('ctrl', 'v')
    p.press('enter')