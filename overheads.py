from pathlib import Path
import csv

def read_over_and_find_highest_overhead():
    # Define file path
    fp = Path.cwd() / "csv_reports" / "Overheads.csv"

    # Read the CSV file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        file_reader = csv.reader(file)
        next(file_reader)  # Skip header

        OverheadRecords = [] 

        for row in file_reader:
            category = row[0]
            overhead_expense = float(row[1])  # Convert overhead value to a number
            OverheadRecords.append([category, overhead_expense])

    # Find the category with the highest overhead
    highest_overhead = 0
    highest_category = ""

    for entry in OverheadRecords:
        category, overhead_expense = entry
        if overhead_expense > highest_overhead:
            highest_overhead = overhead_expense
            highest_category = category

    return f'[HIGHEST OVERHEAD] {highest_category} : {highest_overhead} \n'
