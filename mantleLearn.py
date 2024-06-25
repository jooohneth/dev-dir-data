import pandas as pd

currentData = pd.read_csv("./output/cleaned_emails.csv");
newData = pd.read_csv("./input/MantleLearnEN.csv");
newEmails = newData["email"]
