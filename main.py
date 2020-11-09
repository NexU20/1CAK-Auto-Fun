import pyautogui,time,sys

time.sleep(0.25)
try:
    while True:
        if pyautogui.locateCenterOnScreen('fullPost.PNG',confidence=0.8) != None:
            x,y = pyautogui.locateCenterOnScreen('fullPost.PNG',confidence=0.8)
            pyautogui.click(x,y)
            time.sleep(0.5)
        elif pyautogui.locateCenterOnScreen('moreFun.PNG',confidence=0.5) != None:
            x,y = pyautogui.locateCenterOnScreen('moreFun.PNG',confidence=0.5)
            pyautogui.click(x,y)
            time.sleep(0.5)
        elif pyautogui.locateCenterOnScreen('fun.PNG',confidence=0.8) != None:
            pyautogui.click(pyautogui.locateCenterOnScreen('fun.PNG',confidence=0.8)[0],pyautogui.locateCenterOnScreen('fun.PNG',confidence=0.8)[1])
            time.sleep(0.5)
        pyautogui.scroll(-600)
        time.sleep(3)
except KeyboardInterrupt:
    pass
