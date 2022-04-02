import pytesseract as tess
import pytesseract.pytesseract
from PIL import Image
import numpy as np
import cv2
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def getText(imageUrl):
    img = Image.open(imageUrl)
    return tess.image_to_string(img)


def getDataFromText(text):
    temp = text[text.find('Organic Search Traffic') + len('Organic Search Traffic'): text.rfind('Keywords')]
    temp = re.findall(r'\d+', temp.strip())
    temp = list(map(int, temp))
    traffic = temp[0]
    percentage = temp[1]

    temp = text[text.find('Keywords ') + len('Keywords '): text.rfind('Export to PDF')]
    temp = re.findall(r'\d+', temp.strip())
    temp = list(map(int, temp))
    if len(temp) == 0:
        keyword = 0
    else:
        keyword = temp[0]
    return traffic, percentage, keyword


text = getText("C:/Users/Monir/Desktop/Screenshot_2.png")
print(text)
traffic, percentage, keyword = getDataFromText(text)
print(traffic, percentage, keyword)

# cv2.imshow('img', img)
# cv2.waitKey(0)
