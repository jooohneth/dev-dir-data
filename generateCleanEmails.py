import pandas as pd

data = pd.read_csv("input.csv")
emails = data["teamEmails"]

def getBadEmails(data, emails):
    temp = data[emails.str.contains("@", na=False) == False]
    # temp.to_csv("output/badEmails.csv")
    return temp.index

def getMantleLearnRecords(data, emails):
    temp = data[emails.str.contains("Mantle") == True]
    # temp.to_csv("output/mantleLearnRecords.csv")
    return temp.index

def getRecordsWtihMultipleEmails(data):
    temp = data[data['teamEmails'].str.contains(",", na=False) == True]
    # temp.to_csv("output/recordsWithMultipleEmails.csv")
    return temp.index

def swapColumns(data, indexes, colOne, colTwo):
    data.loc[indexes, [colOne, colTwo]] = data.loc[indexes, [colTwo, colOne]].values

mantleLearnIndexes = getMantleLearnRecords(data, emails)
swapColumns(data, mantleLearnIndexes, 'Project Name', 'teamEmails')

badIndexes = getBadEmails(data, emails)
cleanedData = data.drop(badIndexes)

multipleEmailsIndexes = getRecordsWtihMultipleEmails(cleanedData, emails)
cleanedData.loc[multipleEmailsIndexes, 'teamEmails'] = cleanedData.loc[multipleEmailsIndexes, 'teamEmails'].str.split(',')

explodedData = cleanedData.explode('teamEmails')

uniqueData = explodedData.drop_duplicates(subset='teamEmails', keep='first')

uniqueData['teamEmails'].to_csv("output/cleaned_emails.csv", index=False, header=True)