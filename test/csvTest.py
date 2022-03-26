import pyautogui as pg
import numpy as np
import pandas as pd
import csv
import time
import shutil
import os


def dataLoad(path):
    return pd.read_csv(path)


# This code chunk is for showing all columns for pandas dataset
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

### CSV unique value testing based on phone number
df = dataLoad('C:/Users/Monir/Documents/pyGuiAutomation/files/campaign/alberta ,canada.csv')
#print(df.head(30))

#temp = df[df['phone_number'].isnull() == True]
#l = temp.index.tolist()
#print(temp)
#print(l)

#print(df.loc[425, 'service'])

# Filter phone number
#for i in l:
#    ph_no = df.loc[i, 'business_duration']
#    ph_no = str(ph_no).split('+')

#    if len(ph_no) == 2:
#        ph_no = ph_no[1].replace('-', '')
#        ph_no = ph_no.replace(' ', '')
#    else:
#        ph_no = 'NULL'
#    df.loc[i, 'phone_number'] = ph_no


#temp = df[df['phone_number'] == 'NULL']
#l = temp.index.tolist()
#print(temp)
#print(l)






#duplicate = df[df.duplicated('phone_number')]
#print(duplicate)
#duplicate = duplicate[(duplicate['phone_number'].isnull() == True) & (duplicate['website'].isnull() == True)]
#l = duplicate.index.tolist()
#df = df.drop(l)
#duplicate = df[df.duplicated('phone_number')]
#l = duplicate.index.tolist()
#df = df.drop(l)

d = df[(df['phone_number'].isnull() == True) & (df['website'].isnull() == True)]
l = d.index.tolist()
df = df.drop(l)
duplicate = df[df.duplicated('phone_number')]
l = duplicate.index.tolist()
df = df.drop(l)
