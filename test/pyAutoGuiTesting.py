# This file is for testing chunks of codes and practise

import pyautogui
import time

### Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

### Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()
#print(currentMouseX, currentMouseY)

### Move the mouse to XY coordinates.
#pyautogui.moveTo(100, 150)


### Click the mouse.
#pyautogui.click()


### Move the mouse to XY coordinates and click it.
#pyautogui.click(67, 21)


### Find where button.png appears on the screen and click it.
#pyautogui.click('notion.png')

### Move the mouse 400 pixels to the right of its current position.
#pyautogui.move(400, 0)

### Double click the mouse.
#pyautogui.doubleClick()

### Use tweening/easing function to move mouse over 2 seconds.
#pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

### type with quarter-second pause in between each key for the corsor
#pyautogui.write('Hello world!', interval=0.25)

### Press the Esc key. All key names are in pyautogui.KEY_NAMES
#pyautogui.press('esc')


### Shift key functionalities
#with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#    pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# Shift key is released automatically.


### Press the Ctrl-C hotkey combination.
#pyautogui.hotkey('ctrl', 'a')


### Make an alert box appear and pause the program until OK is clicked.
#pyautogui.alert('This is the message to display.')


# Checking
def getCordinates():
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        print(currentMouseX, currentMouseY)
        time.sleep(3)










