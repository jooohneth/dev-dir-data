import pandas as pd

data = pd.read_csv("input.csv")
emails = data["teamEmails"]

def getBadEmails(data, emails):
    temp = data[emails.str.contains("@", na=False) == False]
    # temp.to_csv("output/badEmails.csv")
    return temp.index


