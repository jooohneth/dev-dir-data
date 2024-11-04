import pandas as pd

data = pd.read_csv("./input/ETHPragueEmails.csv")

def getRecordsWtihMultipleEmails(data):
    temp = data[data['teamEmails'].str.contains(",", na=False) == True]
    # temp.to_csv("output/recordsWithMultipleEmails.csv")
    return temp.index

idxs = getRecordsWtihMultipleEmails(data)
data.loc[idxs, 'teamEmails'] = data.loc[idxs, 'teamEmails'].str.split(',')
explodedData = data.explode('teamEmails')

explodedData.to_csv('output/PragueClean.csv', index=False)

