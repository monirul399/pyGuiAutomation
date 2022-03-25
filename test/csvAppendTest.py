import pyautogui as pg
import numpy as np
import pandas as pd
import csv
import time
import shutil
import os


def dataLoad(path):
    return pd.read_csv(path)


dataFrame = pd.DataFrame(
    columns=['business_name', 'service', 'rating', 'review_count', 'business_duration', 'phone_number', 'website'])
dataFrame.to_csv('C:/Users/Monir/Documents/pyGuiAutomation/test/t.csv')
temp = dataLoad('C:/Users/Monir/Documents/pyGuiAutomation/test/t.csv')
print(temp.columns)
dataFrame.info()
dataFrame = pd.DataFrame([[1, 2, 3, 4, 5, 6, 7], [7, 8, 9, 10, 11, 12, 14]], columns=['business_name', 'service', 'rating', 'review_count', 'business_duration', 'phone_number', 'website'])
dataFrame.to_csv('C:/Users/Monir/Documents/pyGuiAutomation/test/t.csv', mode='a', index=False, header=False)
dataFrame.info()

print(dataFrame.head())
print(dataFrame.columns)

df = dataLoad('C:/Users/Monir/Documents/pyGuiAutomation/files/campaign/alberta ,canada.csv')
df.info()
print(df.head())
print(df.columns)
