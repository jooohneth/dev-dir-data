import pandas as pd

data = pd.read_csv("input.csv")
emails = data["teamEmails"]

def getBadEmails(data, emails):
    temp = data[emails.str.contains("@") == False]
    temp.to_csv("badEmails.csv")
    return temp.index

print(getBadEmails(data, emails))