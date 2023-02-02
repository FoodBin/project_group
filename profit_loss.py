#Create a function for profit_loss
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
        Day_Net_Profit = []
        Difference = []

        # Create a "for" loop to store Day and Net profits
        for row in reader:
            Day_Net_Profit.append([row[0], row[4]])

        #Create another "for" loop with a condition that calculates whther there is a profit deficit
        for Calculation in range(1, len(Day_Net_Profit)): #Turn Day_Net_Profit into a range.

        #Turn 'str' into a 'int' for Net Profit, turn 'str' to 'float' for Day
            if int(Day_Net_Profit[Calculation][1]) < int(Day_Net_Profit[Calculation - 1][1]): #If the value of the current day is lesser than the previous day
                Difference.append([float(Day_Net_Profit[Calculation][0]), int(Day_Net_Profit[Calculation - 1][1]) - int(Day_Net_Profit[Calculation][1])]) #Append Day of deficit and difference between Previous day net profit and Current day net profit
        
        #Create a file path which the days and values will be entered into
        Profit_Loss_Filepath = Path.cwd()/"Summary_report.txt"
        with Profit_Loss_Filepath.open(mode = "a", encoding= "UTF-8") as file: #Mode will be "a"

            #Create an "if" function
            if Difference == []: #If the Difference list is empty, the string below will be written into Summary_report.txt
                file.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            else:
                for Deficit in Difference: #If there are values in the Difference, the string below will be written into Summary_report.txt
                    file.write(f"[PROFIT DEFICIT] DAY: {Deficit[0]}, AMOUNT: USD{Deficit[1]}\n")