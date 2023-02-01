#Import Overheads CSV file
from pathlib import Path
import csv

#Create a file to the Overheads CSV file.
COH_fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv"

#Read the Overheads CSV file
with COH_fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader) #Skip the header

#Create an empty list that will be used to store calculated deficits if detected
Cash_on_Hand = []
Cash_Defecit = []

#Create a loop
for row in reader:

    #Bring over the values from the CSV files into the, Cash_on_Hand, empty list
    Cash_on_Hand.append([row(0), row[1]])
    #Create a condition that will calculate cash deficit if found.


print (Cash_on_Hand)