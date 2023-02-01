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
    Deficit = []

    #Create a loop
    for day, coh in reader:

        #Bring over the values from the CSV files into the, Cash_on_Hand, empty list
        Cash_on_Hand.append([day, coh])
        Cash_on_Hand.append(float(coh))
        #Create a condition that will calculate cash deficit if found.
        if coh[0] > coh[1]:
            Deficit.append[coh[0] - coh[1]]


print (Cash_on_Hand)