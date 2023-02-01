def profitloss_function():
    """
    - This function will display on the notepad whether there is a profit deficit or surplus
    - This function does not require any parameter
    """

#Import Profit and Loss CSV file
from pathlib import Path
import csv

#Create a file to the Profit and Loss CSV file.
PL_fp = Path.cwd()/"csv_reports"/"Profit and Loss.csv"

#Read the Profit and Loss CSV file
with PL_fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader) #Skip the header
    
    #Create empty lists for the Day and Net Profit, and Difference
    Day_Net_Profit= []
    Difference = []

    #Net profits and Difference and days will be appended into the respective empty lists 
    for row in reader:
        Day_Net_Profit.append([float(row[0]), float(row[4])]) #Convert Net profit values into a float

    #Create another loop and acondition that will identify whether there is a net profit deficit or surplus between the neighbouring days
    for net_profit in Day_Net_Profit:
        Difference -= net_profit[1]


print(Difference)




    #Create a file path which the text and numbers will be entered into
    #ProfitLoss_Filepath = Path.cwd()/"Summary_report.txt"
    #with ProfitLoss_Filepath.open(mode = "a", encoding= "UTF-8") as file: #Use mode "a" as we are adding to the text file

    #Use "f-string" to write out the results, day of effect with text
        #file.write(f"""
#{Result}
#""")
