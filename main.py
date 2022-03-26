import pyautogui as pg
import numpy as np
import pandas as pd
import csv
import time
import shutil
import os
import csvProcessing


# Functions
def mapscroll():
    screenWidth, screenHeight = pg.size()
    x, y = 613, 449  # Position of the map scroller
    pg.moveTo(x, y)
    pg.mouseDown()
    while y < screenHeight - 100:
        y += 100
        pg.moveTo(x, y)
        time.sleep(0.2)
    pg.mouseUp()


def openChromeBrowser():
    # Open chrome browser
    x, y = pg.locateCenterOnScreen("images/B2Cchrome.png", grayscale=True,
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
    pg.moveTo(x, y + 30)
    pg.mouseUp()
    return x, y + 30


def clickMoreBusiness():
    # Clicking on more Business
    x, y = pg.locateCenterOnScreen("images/moreBusiness.png", grayscale=False, confidence=0.9)
    pg.click(x, y)
    time.sleep(2)


def clickMapNext():
    # find map next and click
    x, y = pg.locateCenterOnScreen("images/mapnext.png", grayscale=True, confidence=0.9)
    pg.click(x, y)
    time.sleep(2)


def clickMapPrev():
    # find map previous and click
    x, y = pg.locateCenterOnScreen("images/mapprev.png", grayscale=True, confidence=0.9)
    pg.click(x, y)
    time.sleep(2)


def moveDirectory(fileName):
    shutil.move("C:/Users/Monir/Downloads/google.csv", "C:/Users/Monir/Documents/pyGuiAutomation/files/CSV Files")
    file = f"C:/Users/Monir/Documents/pyGuiAutomation/files/CSV Files/{fileName}.csv"
    os.rename("C:/Users/Monir/Documents/pyGuiAutomation/files/CSV Files/google.csv", file)
    return file


# Retrieve services from files
services = []
with open("files/Local Service.txt") as file:
    for line in file:
        line = line.strip('\n')
        line = line.strip(' ')
        services.append(line)

# Type searching on urlbox
locations = np.array(pd.read_csv('files/Locations.csv'))

for i, location in enumerate(locations):
    # Create CSV file and name it on location
    dataFrame = pd.DataFrame(
        columns=['business_name', 'service', 'rating', 'review_count', 'business_duration', 'phone_number', 'website'])
    location_name = location[1] + " ," + location[0]
    dataFramePath = f'C:/Users/Monir/Documents/pyGuiAutomation/files/campaign/{location_name}.csv'
    dataFrame.to_csv(dataFramePath, index=False)

    for j, service in enumerate(services):
        searchTag = service + " in " + location[1] + " ," + location[0]

        openChromeBrowser()
        urlWrite()

        pg.write(searchTag, interval=0.02)
        pg.press('enter')
        time.sleep(2)

        # Scroll Gradually and hit more business button
        X, Y = 1906, 260
        while True:
            X, Y = scrollDownSERP(X, Y)
            try:
                clickMoreBusiness()
                break
            except TypeError:
                pass

        mapscroll()
        clickMapNext()
        mapscroll()
        clickMapPrev()

        # Clicking on hunter scrapper
        pg.click(x=1643, y=80)

        # "crawl" button
        time.sleep(3)
        pg.click(x=236, y=160)

        # Total scrapping time delay
        time.sleep(45)

        # Download CSV
        pg.click(580, 99)
        time.sleep(2)

        # Rename move to Project files
        filePath = moveDirectory(searchTag)

        # Data Preprocessing
        df = csvProcessing.processedDataframe(filePath)
        df.to_csv(dataFramePath, mode='a', index=False, header=False)












