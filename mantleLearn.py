import pandas as pd

currentEmails = pd.read_csv("./output/Q1MantleLearn.csv")['teamEmails'];
newData = pd.read_csv("./input/MantleLearnEN.csv");
newEmails = newData["email"]

def dropNARecords(emails):
    return emails.dropna()

newEmails = dropNARecords(newEmails)
mergedEmails = pd.concat([currentEmails, newEmails], ignore_index=True)
mergedEmails = mergedEmails.iloc[1:]

qTwo = mergedEmails.drop_duplicates(keep=False)
print(len(mergedEmails))
print(len(qTwo))
qTwo = pd.concat([pd.Series(['teamEmails']), qTwo], ignore_index=True)

qTwo.to_csv("output/Q2MantleLearn.csv", index=False, header=False)

result = mergedEmails.drop_duplicates(keep="first")
result = pd.concat([pd.Series(['teamEmails']), result], ignore_index=True)

result.to_csv("output/result.csv", index=False, header=False)