import time

from subModules import handyTasks
from subModules import csvProcessing
import pyautogui as pg

WHATSAPP_LINK = 'https://wa.me/'


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
            conf -= 0.05
        time.sleep(1.0)     # delay for loading
        if conf <= 0.75:
            pg.click(1127, 334)
            break


def checkInvalidWhatsapp():
    #for i in range
    pass


def openChromeBrowser():
    # Open chrome browser
    x, y = pg.locateCenterOnScreen("images/B2Cchrome.png", grayscale=True,
                                   confidence=0.9)  # This image won't work if photo of B2Cserver email changes
    pg.click(x, y)


def testing():
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

        df.info()

        # Do for each Business
        for index, row in df.iterrows():
            # open chrome browser
            openChromeBrowser()
            # open new tab
            handyTasks.openNewChromeTab()

            # write Whatsapp URL
            temp = WHATSAPP_LINK + str(int(row['phone_number']))
            handyTasks.urlWrite(WHATSAPP_LINK + '15876725625')  # 2 seconds delay here
            # Open whatsapp
            openWhatsapp(0.95)      # Pass top confidence




            time.sleep(5)
            openChromeBrowser()
            handyTasks.closeChromeTab()
            break  # break business
        break  # break dataset


testing()
