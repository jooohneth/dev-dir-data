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

def getRecordsWtihMultipleEmails(data, emails):
    temp = data[data['teamEmails'].str.contains(",", na=False) == True]
    # temp.to_csv("output/recordsWithMultipleEmails.csv")
    return temp.index

