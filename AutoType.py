import pyautogui
import time
import random

# path of donor file to read from
donorFile = 'E:/framework2232/Python/donor.html'

# time to setup (in seconds) before typing begins
time.sleep(5)

value=0.2

with open(donorFile, 'r') as openFile:
    
    for line in openFile:   
        pyautogui.typewrite(line, interval= (random.uniform(0.05, 0.15))) 

        i = 0
        while i < 11:
            i = i + 1
            pyautogui.typewrite(['del'])
        
        time.sleep(0.05)
        pyautogui.hotkey("shift", "alt", "f") 
        time.sleep(0.05)
        pyautogui.typewrite(['enter']) 
        time.sleep(0.5)
        # value = random.uniform(0.08, 0.4)
        # print(value)
        