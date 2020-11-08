import pyautogui,time,sys

def autoMinimize():
    x,y = pyautogui.position()
    minX,minY,maxX,maxY = 1463,0,1507,295
    if (x >= minX and x <= maxX and y >= minY and y < maxY):
        pyautogui.click()
    else:
        pyautogui.moveTo(1500,5)
        pyautogui.click()

def autoWriteKey(kta):
    pyautogui.write(str(kta),interval=0.25)

# time.sleep(0.5)
# pyautogui.hotkey('win','s')
# time.sleep(0.25)
# autoWriteKey("firefox\n")
# time.sleep(2)
# autoWriteKey("www.1cak.com\n")
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

# hi = pyautogui.prompt(text='hallo',title='Hallo, Client :)',default='hi')
# print(hi) (x=538, y=663)