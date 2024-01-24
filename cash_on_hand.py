from pathlib import Path
import csv

print (Path.cwd() )

fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    file_reader = csv.reader(file)
    next(file_reader) # skip header

    Cash_on_Hand_Records=[] 

    for row in file_reader:
        day = float(row[0])
        cash_on_hand = float(row[1])  # Convert overhead value to a number
        Cash_on_Hand_Records.append([day,cash_on_hand])

print (Cash_on_Hand_Records)

