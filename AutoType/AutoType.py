import pyautogui
import time
import random

# time to setup (in seconds) before typing begins
time.sleep(10)



# path of donor file to read from
donorFile = 'E:/framework2232/Python/donor_html.html'

with open(donorFile, 'r') as openFile:
    
    for line in openFile:   
        pyautogui.typewrite(line, interval= 0.08) 

        i = 0
        while i < 11:
            i = i + 1
            pyautogui.typewrite(['del'])
        
        time.sleep(0.05)
        pyautogui.hotkey("shift", "alt", "f") 
        time.sleep(0.05)
        pyautogui.typewrite(['enter']) 
        time.sleep(0.5)
        

time.sleep(10)
# path of donor file to read from
donorFile = 'E:/framework2232/Python/donor_css.css'

with open(donorFile, 'r') as openFile:
    
    for line in openFile:   
        pyautogui.typewrite(line, interval= 0.08)

        i = 0
        while i < 11:
            i = i + 1
            pyautogui.typewrite(['del'])
        
        time.sleep(0.05)
       