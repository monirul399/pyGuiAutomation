from subModules import extractWebsiteData
from subModules import csvProcessing
from subModules import handyTasks
import numpy as np
import pandas as pd
import validators

# this code chunk is for dataframe all column visualization
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


def getDatasetEmailFacebook():
    # Parameters: takes None and returns None
    # Task: Add email and facebook link with the dataset
    # Using : `handyTasks.getFileList(folder_path)`, `csvProcessing.dataLoad(filePath)`, `extractWebsiteData.getEmailFacebook(website)`

    # Get all file names of a directory
    folder_path = "files/campaign"
    fileNames = handyTasks.getFileList(folder_path)

    # Do for every dataset
    for fileName in fileNames:
        # create file path
        filePath = folder_path + '/' + fileName
        # load dataset from the path
        df = csvProcessing.dataLoad(filePath)

        # create new columns
        df.loc[:, 'email'] = np.nan
        df.loc[:, 'facebook'] = np.nan

        i = 0
        for index, row in df.iterrows():
            website = row['website']
            emails, facebooks = {}, []
            try:
                if validators.url(website):
                    emails, facebooks = extractWebsiteData.getEmailFacebook(website)
            except TypeError:
                print("Invalid URL: ", website)

            if len(emails) >= 1:
                df.loc[[index], 'email'] = ', '.join(list(emails))
                df.loc[[index], 'facebook'] = ', '.join(facebooks)

            # observe row number
            i += 1
            print(i, website)
            print('email : ', emails)
            print('facebook : ', facebooks)


        # create new CSV file
        new_path = folder_path.replace('campaign', 'campaignEmailFacebook') + '/' + fileName
        dataFrame = pd.DataFrame(columns=df.columns)
        dataFrame.to_csv(new_path, index=False)
        df.to_csv(new_path, mode='a', index=False, header=False)

# Extra : need to remove
def testing():
    # Get all file names of a directory
    folder_path = "files/campaignEmailFacebook"
    fileNames = handyTasks.getFileList(folder_path)
    print(fileNames)
    # Do for every dataset
    for fileName in fileNames:
        # create file path
        filePath = folder_path + '/' + fileName
        # load dataset from the path
        df = csvProcessing.dataLoad(filePath)

        print(df.loc[df['email'].isnull() == False, 'email'].count())
        break


# Get Dataset with email and facebook link column
getDatasetEmailFacebook()





