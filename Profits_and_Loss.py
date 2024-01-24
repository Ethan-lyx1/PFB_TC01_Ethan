from pathlib import Path
import csv

print (Path.cwd() )

fp = Path.cwd() / "csv_reports" / "Profit_and_Loss.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    file_reader = csv.reader(file)
    next(file_reader) # skip header

    PnL_Records=[] 

    for row in file_reader:
        day = float(row[0])
        sales = float(row[1])  # Convert overhead value to a number
        Trading_Profit = float(row[2])
        Operating_Expense = float(row[3])
        Net_Profit = float (row [4])
        PnL_Records.append([day,sales,Trading_Profit,Operating_Expense,Net_Profit])

print (PnL_Records)

daily_net_profit_difference = []
