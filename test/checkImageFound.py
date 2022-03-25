import pyautogui as pg
import time


def openChromeBrowser():
    # Open chrome browser
    x, y = pg.locateCenterOnScreen("../images/B2Cchrome.png", grayscale=True,
                                   confidence=0.9)  # This image won't work if photo of B2Cserver email changes
    pg.click(x, y)


def urlWrite():
    # Write on URL for search
    x, y = 800, 80
    pg.click(x, y)


def scrollDownSERP(x, y):
    # Scrolling down the page
    pg.moveTo(x, y)
    pg.mouseDown()
    pg.moveTo(x, y+40)
    pg.mouseUp()
    return x, y+40


def clickMoreBusiness():
    # Clicking on more Business
    time.sleep(0.5)
    x, y = pg.locateCenterOnScreen("../images/moreBusiness.png", grayscale=False, confidence=0.9)
    pg.click(x, y)
    time.sleep(2)


openChromeBrowser()
urlWrite()
pg.write("Locksmith in alberta ,canada", interval=0.02)
pg.press('enter')
time.sleep(2)

x, y = 1906, 260
counter = 0
while True:
    x, y = scrollDownSERP(x, y)
    try:
        clickMoreBusiness()
        break
    except TypeError:
        counter += 1
print(counter)








