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
    Day_Coh = []
    Deficit = []

    #Create a "for" loop 
    for row in reader:
        Day_Coh.append([float(row[0]),float(row[1])])
    
    for difference in Day_Coh:
        Difference = Day_Coh[1][1] - Day_Coh[0][1]
        Difference += 1




print (Difference)
