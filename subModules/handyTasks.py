import os
import glob
import pyautogui as pg
import time


# Get all file names of a directory
def getFileList(path):
    # Parameters: takes paths and return file names
    # Task : extracts all file names from given directory
    # using : glob

    path = path + "/*"  # extract all file names
    temp = glob.glob(path)
    files = []
    for file in temp:
        f = file.split('\\')
        files.append(f[1])
    return files


def urlWrite(searchTag):
    # Write on URL for search
    x, y = 800, 80
    pg.click(x, y)

    pg.write(searchTag, interval=0.02)
    pg.press('enter')
    time.sleep(2)


def clickViewAll():
    # Clicking on more Business
    x, y = pg.locateCenterOnScreen("images/viewAll.png", grayscale=False, confidence=0.9)
    pg.click(x, y)
    time.sleep(2)


def openNewChromeTab():
    pg.keyDown('ctrl')
    pg.press('t')
    pg.keyUp('ctrl')


def closeChromeTab():
    pg.keyDown('ctrl')
    pg.press('w')
    pg.keyUp('ctrl')

