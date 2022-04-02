import time
import numpy as np
import pandas as pd
from subModules import handyTasks
from subModules import csvProcessing
import pyautogui as pg
import pyperclip
import math
import re

SEMRUSH_URL = 'https://www.semrush.com/analytics/overview/?searchType=domain'
LOG_URL = 'https://www.semrush.com/projects/'


# this code chunk is for dataframe all column visualization
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


def openChromeBrowser():
    # Open chrome browser
    x, y = pg.locateCenterOnScreen("images/B2Cchrome.png", grayscale=True,
                                   confidence=0.9)  # This image won't work if photo of B2Cserver email changes
    pg.click(x, y)


def semrushDomainOverview(row, coutnryName):
    # go to semrush page
    handyTasks.urlWrite(SEMRUSH_URL)
    time.sleep(1)  # take 2 second delay
    pg.write(row['website'])
    X, Y = worldWide(0.7)
    time.sleep(1)  # delay for starting the writing
    pg.write(coutnryName)
    time.sleep(0.5)
    pg.click(1362, 596)  # select country
    pg.click(X + 150, Y)  # click search button


def worldWide(conf):
    while True:
        # Parameters : takes confidence
        try:
            x, y = pg.locateCenterOnScreen("images/worldwide.png", grayscale=True,
                                           confidence=conf)  # This image won't work if photo of B2Cserver email changes
            pg.click(x, y)
            return x, y
        except TypeError:
            conf += 0.05
            time.sleep(0.5)  # delay for loading
        if conf >= 0.95:
            pg.click(1384, 477)     # position of worldwide button
            return 1384, 477


def getNewEmail(email):
    tempMails = []
    with open("storage/tempMail.txt") as file:
        for line in file:
            line = line.strip('\n')
            line = line.strip(' ')
            tempMails.append(line)

    index = tempMails.index(email)
    if index == (len(tempMails) - 1):
        return tempMails[0]
    else:
        return tempMails[index + 1]


def logInSemrush():
    # open another chrome tab
    handyTasks.openNewChromeTab()
    handyTasks.urlWrite(LOG_URL)
    time.sleep(2)

    # click on profile
    try:
        x, y = pg.locateCenterOnScreen("images/semrushProfile.png", grayscale=True, confidence=0.85)
        pg.click(x, y)
        time.sleep(1)
        try:
            x, y = pg.locateCenterOnScreen("images/semrushLogOut.png", grayscale=True, confidence=0.85)
            pg.click(x, y)

        except TypeError:
            print('Log out button not found!')

    except TypeError:
        print('Semrush Profile image not found!')

    # go to log in page
    time.sleep(3)
    try:
        x, y = pg.locateCenterOnScreen("images/semRushLogIn.png", grayscale=True, confidence=0.85)
        pg.click(x, y)
        time.sleep(5)
    except TypeError:
        print('Log in button not found!')

    # select email
    handyTasks.selectAll()
    # copy email to clipboard
    handyTasks.copyAll()
    time.sleep(0.5)
    email = pyperclip.paste()
    # clear email field
    pg.press('backspace')

    newEmail = getNewEmail(email)
    pg.write(newEmail)
    time.sleep(0.5)
    pg.press('tab')
    pg.write(newEmail)
    time.sleep(0.5)

    try:
        x, y = pg.locateCenterOnScreen("images/LOGIN.png", grayscale=True, confidence=0.85)
        pg.click(x, y)
        time.sleep(5)
    except TypeError:
        print('not found!')

    handyTasks.closeChromeTab()


def checkSemrushLogin():
    try:
        x, y = pg.locateCenterOnScreen("images/getFreeTrial.png", grayscale=True, confidence=0.9)
        # Need to log in
        return False
    except TypeError:
        return True  # Logged in


def semrush():
    # Get all file names of a directory
    folder_path = "files/campaign"
    fileNames = handyTasks.getFileList(folder_path)
    print(fileNames)

    # Do for every dataset
    for fileName in fileNames:
        # create file path
        filePath = folder_path + '/' + fileName
        # load dataset from the path
        df = csvProcessing.dataLoad(filePath)

        # get country name from filename
        coutnryName = fileName[fileName.find(',') + 1: fileName.rfind('.csv')]

        # Do for each Business
        for index, row in df.iterrows():
            # open chrome browser
            openChromeBrowser()
            # open new tab
            handyTasks.openNewChromeTab()

            # check Website exists or not
            if isinstance(row['website'], float):
                handyTasks.closeChromeTab()
                openChromeBrowser()  # This is necessary
                continue

            # if website exists
            # take screenshot
            # handyTasks.urlWrite(row['website'])
            # time.sleep(5)
            # im = pg.screenshot(region=(8, 222, 1880, 780))     # region(left, top, width, height)
            # im.show()

            # go to semrush page
            semrushDomainOverview(row, coutnryName)
            time.sleep(5)
            check = checkSemrushLogin()

            if check:
                print("Already logged in")
            else:
                print('New log in')
                logInSemrush()
                pg.press('f5')
                time.sleep(3)
            handyTasks.closeChromeTab()
            openChromeBrowser()
            if index == 30:
                break
        break


semrush()
