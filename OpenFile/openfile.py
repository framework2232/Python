import os
import time
import pyautogui

def confirm():
    time.sleep(timeBeforeEnter)
    pyautogui.typewrite(['enter']) 
    time.sleep(timeToOpen)


openURL = 'https://www.google.com.au/'
search_item = "youtube"


timeToOpen = 10
timeBeforeEnter = 1

# open google.com.au
os.startfile(openURL)
time.sleep(timeToOpen)

# type search item
pyautogui.typewrite(search_item, interval= 0.1)
confirm()



# # move mouse
# pyautogui.move(100, 100, 1, pyautogui.easeOutQuad)
# pyautogui.click()
# pyautogui.scroll(-10)