from pathlib import Path
import csv

print (Path.cwd() )

fp = Path.cwd() / "csv_reports" / "Overheads.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    file_reader = csv.reader(file)
    next(file_reader) # skip header

    OverheadRecords=[] 

    for row in file_reader:
        category = row[0]
        overhead_expense = float(row[1])  # Convert overhead value to a number
        OverheadRecords.append([category, overhead_expense])

print (OverheadRecords)

highest_overhead = 0
highest_category = ""

for entry in OverheadRecords:
    category, overhead_expense = entry
    if overhead_expense > highest_overhead:
        highest_overhead = overhead_expense
        highest_category = category

print (f'Highest Overhead: {highest_category} {highest_overhead}')
