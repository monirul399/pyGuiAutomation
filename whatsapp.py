import time
import numpy as np
import  pandas as pd
from subModules import handyTasks
from subModules import csvProcessing
import pyautogui as pg
import math

WHATSAPP_LINK = 'https://wa.me/'

# this code chunk is for dataframe all column visualization
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)



def openWhatsapp(conf):
    # Open chrome browser
    while True:
        # Parameters : takes confidence
        try:
            x, y = pg.locateCenterOnScreen("images/openWhatsapp.png", grayscale=True,
                                           confidence=conf)  # This image won't work if photo of B2Cserver email changes
            pg.click(x, y)
            break
        except TypeError:
            conf += 0.05
        time.sleep(1.0)     # delay for loading
        if conf >= 0.95:
            pg.click(1127, 334)
            break


def chceckWhatsappValidity(conf):
    # takes confidence returns true if number available on Whatsapp and returns False if not available
    # check number is not available in whatsapp or not
    while True:
        try:
            x, y = pg.locateCenterOnScreen("images/invalidWhatsapp.png", grayscale=True,
                                           confidence=conf)  # This image won't work if photo of B2Cserver email changes
            pg.click(x, y)
            return False
        except TypeError:
            conf += 0.05
            try:
                x, y = pg.locateCenterOnScreen("images/startingChat.png", grayscale=True,
                                               confidence=conf)
                time.sleep(1)
            except TypeError:
                pass
        if conf >= 0.95:
            return True





def openChromeBrowser():
    # Open chrome browser
    x, y = pg.locateCenterOnScreen("images/B2Cchrome.png", grayscale=True,
                                   confidence=0.9)  # This image won't work if photo of B2Cserver email changes
    pg.click(x, y)


def checkWhatsapp():
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

        # Do for each Business
        for index, row in df.iterrows():
            # open chrome browser
            openChromeBrowser()
            # open new tab
            handyTasks.openNewChromeTab()

            # write Whatsapp URL
            if math.isnan(row['phone_number']):
                handyTasks.closeChromeTab()
                openChromeBrowser()  # This is necessary
                continue

            temp = WHATSAPP_LINK + str(int(row['phone_number']))
            handyTasks.urlWrite(temp)  # 2 seconds delay here
            # Open whatsapp
            openWhatsapp(0.75)      # Pass lowest confidence


            time.sleep(1) #sleep 1 sec before checking validity
            check = chceckWhatsappValidity(0.75)

            #time.sleep(2)
            openChromeBrowser()
            handyTasks.closeChromeTab()
            openChromeBrowser() # This is necessary
            #break  # break business
        #break  # break dataset


checkWhatsapp()
