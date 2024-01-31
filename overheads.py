from pathlib import Path
import csv

def read_over_and_find_highest_overhead():
    """
    Function reads overhead data from a CSV file and identifies the category with the highest overhead expense.
    The function opens 'Overheads.csv' located in the 'csv_reports' directory relative to the current working directory. 
    It then reads the overhead data, which includes categories and their corresponding expenses, and then determines the 
    category with the highest overhead expense.
    
    Returns:
        str: A string indicating the category with the highest overhead and the amount.
    """
    fp = Path.cwd() / "csv_reports" / "Overheads.csv" # Define file path for Overheads.csv in the 'csv_reports' directory of the current working directory
    
    with fp.open(mode="r", encoding="UTF-8", newline="") as file: # Open the CSV file as read, using UTF-8 encoding
        file_reader = csv.reader(file)
        next(file_reader)  # Skip header

        OverheadRecords = []   # Initialize an empty list to store overhead records

        for row in file_reader: # For loop to iterate over each row in the CSV file
            category = row[0] # Extract the category from csv file
            overhead_expense = float(row[1])  # Convert overhead expense to a float
            OverheadRecords.append([category, overhead_expense]) # Append the category and expense to OverheadRecords list created

 # Initialize variables to track the highest overhead and its corresponding category
    highest_overhead = 0
    highest_category = ""

    for entry in OverheadRecords:  # Iterate through each entry in OverheadRecords to find the highest overhead
        category, overhead_expense = entry
        if overhead_expense > highest_overhead:  # Update the highest overhead and its category if a new maximum is found
            highest_overhead = overhead_expense
            highest_category = category

    return f'[HIGHEST OVERHEAD] {highest_category} : {highest_overhead} % \n' #Return a formatted string with the category and the highest overhead
