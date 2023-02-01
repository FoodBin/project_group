#Create the function for overheads
def overheads_function():

    """
    - This function is used to filter out the highest overhead percentage
    - No parameters is required for this function
    """

    #Import Overheads CSV file
    from pathlib import Path
    import csv

    #Create a file to the Overheads CSV file.
    OH_fp = Path.cwd()/"csv_reports"/"Overheads.csv"

    #Read the Overheads CSV file
    with OH_fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader) #Skip the header

    #Create a lists to sort the values
        List = []
        Highest = []

    #Create a loop to append the new empty lists while sorting the numbers in descending order
        for row in reader:
            List.append([float(row[1]),row[0]]) #Change numerical values to a float
            List.sort(reverse=True)
 
    #Seperate the highest overhead from the rest into the "Highest" empty list
        Highest.append(List[0])

    #Create a file path which the text and numbers will be entered into
        Overheads_Filepath = Path.cwd()/"Summary_report.txt"
        with Overheads_Filepath.open(mode = "a", encoding= "UTF-8") as file:

    #Use "f-string" to write out the highest overhead with text
            file.write(f"[HIGHEST OVERHEADS] {Highest[0][1]}: {Highest[0][0]}%")

#Execute the function
overheads_function()



