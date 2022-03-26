import numpy as np
import pandas as pd


# functions
def dataLoad(path):
    return pd.read_csv(path)


def preProcessing(df):
    # phone number filter
    columns = df.columns
    data = np.array(df)
    for i, item in enumerate(data.T[5]):
        ph_no = str(item).split('+')
        if len(ph_no) == 2:
            ph_no = ph_no[1].replace('-', '')
            ph_no = ph_no.replace(' ', '')
        else:
            ph_no = 'NULL'
        data.T[5][i] = ph_no

    # service filter
    for i, item in enumerate(data.T[1]):
        item = str(item)
        item = item.replace('.', '')
        item = item.replace('No reviews ', '')
        if item == 'nan':
            item = 'NULL'
        data.T[1][i] = item

    df = pd.DataFrame(data, columns=columns)

    # Phone number filter when phone_number == nan and business_duration got the phone number
    temp = df[df['phone_number'] == 'NULL']           # here check will be with null
    l = temp.index.tolist()
    for i in l:
        ph_no = df.loc[i, 'business_duration']
        ph_no = str(ph_no).split('+')

        if len(ph_no) == 2:
            ph_no = ph_no[1].replace('-', '')
            ph_no = ph_no.replace(' ', '')
        else:
            ph_no = 'NULL'
        df.loc[i, 'phone_number'] = ph_no
    return df


def dataFiltering(df):
    # filter unique phone number and website for preparing the final dataset
    d = df[(df['phone_number'].isnull() == True) & (df['website'].isnull() == True)]
    l = d.index.tolist()
    df = df.drop(l)
    duplicate = df[df.duplicated('phone_number')]
    l = duplicate.index.tolist()
    df = df.drop(l)
    return df


def dataCleaning(df):
    df.rename(columns={"dbg0pd": "business_name", "rllt__details": "service", "YDIN4c": "rating",
                       "HypWnf": "review_count", "rllt__details 2": "business_duration",
                       "rllt__details 3": "phone_number", "rllt__details 4": "none",
                       "rllt__details 5": "none", "yYlJEf href": "website",
                       "BSaJxc": "none", "vzRMeAg4Oi8__kl-trunc-name": "none",
                       "sBhnyP5sXkG__rtng": "none", "sBhnyP5sXkG__number-of-reviews": "none",
                       "yYlJEf href 2": "none", "UbRuwe": "none"}, inplace=True)
    df.drop('none', inplace=True, axis=1)
    df = df.reindex(columns=['business_name', 'service', 'rating', 'review_count', 'business_duration', 'phone_number', 'website'])
    return df


# This is the Final function that will be called from main
def processedDataframe(path):
    df = dataLoad(path)
    df = dataCleaning(df)
    df = preProcessing(df)
    df = dataFiltering(df)
    return df
