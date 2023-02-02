#Create a function for cash_on_hand
def coh_function():
    """
    - This function works will be used to determine whether or not there is a cash surplus or cash deficit
    - This function does not require any parameters
    """

    #Import Cash on Hand CSV file
    from pathlib import Path
    import csv

    #Create a file to the Cash on Hand CSV file.
    COH_fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv"

    #Read the Cash on Hand CSV file
    with COH_fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader) #Skip the header
        
        #Create two empty lists. One that stores the day with the cash on hand, and one that stores the respective day with its cash deficits
        Day_COH = []
        Difference = []

        #Create a "for" loop that stores the day and cash on hand
        for row in reader:
            Day_COH.append([row[0],row[1]])

        #Create another "for" loop with a condition that calculates whther there is a cash deficit
        for Calculation in range(1, len(Day_COH)): #Turn Day_COH into a range.

        #Turn 'str' into a 'int' for Cash On Hand, turn 'str' to 'float' for Day
            if int(Day_COH[Calculation][1]) < int(Day_COH[Calculation - 1][1]): #If the value of the current day is lesser than the previous day
                Difference.append([float(Day_COH[Calculation][0]), int(Day_COH[Calculation - 1][1]) - int(Day_COH[Calculation][1])]) #Append Day of deficit and difference between Previous day cash on hand and Current day cash on hand 
        
        #Create a file path which the text and numbers will be entered into
        Cash_On_Hand_Filepath = Path.cwd()/"Summary_report.txt"
        with Cash_On_Hand_Filepath.open(mode = "a", encoding= "UTF-8") as file: #Mode will be "a"

            #Create an "if" function
            if Difference == []: #If the Difference list is empty, the string below will be written into Summary_report.txt
                file.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            else:
                for Deficit in Difference: #If there are values in the Difference, the string below will be written into Summary_report.txt
                    file.write(f"[CASH DEFICIT] DAY: {Deficit[0]}, AMOUNT: USD{Deficit[1]}\n")