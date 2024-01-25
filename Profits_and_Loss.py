from pathlib import Path
import csv

print (Path.cwd() )

fp = Path.cwd() / "csv_reports" / "Profit_and_Loss.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    file_reader = csv.reader(file)
    next(file_reader) # skip header

    PnL_Records=[] 

    for row in file_reader:
        day = int(row[0])
        Net_Profit = float(row[4])
        PnL_Records.append([day, Net_Profit])


daily_net_profit_difference = []
for day_index in range(len(PnL_Records) - 1):
    current_day_profit = PnL_Records[day_index][1]    # Access the current day's net profit
    next_day_profit = PnL_Records[day_index+1][1]    # Access the next day's net profit
    difference = next_day_profit - current_day_profit     # Calculate the difference
    daily_net_profit_difference.append(difference)    # Add the difference to the list

print (daily_net_profit_difference)

is_increasing = True # Initialize variables to track if the net profit is increasing or decreasing
is_decreasing = True
deficit_days = []

# Analyze the trend of net profit and collect deficit days
for day_index, diff in enumerate(daily_net_profit_difference):
    if diff <= 0:
        is_increasing = False  # If any day's profit is not increasing, then is_increasing is set to False
    if diff >= 0:
        is_decreasing = False  # If any day's profit is not decreasing, then is_decreasing is set to False
    if diff < 0:
        actual_day = PnL_Records[day_index + 1][0] # Since day_index starts from 0, corresponding to the difference between day 1 and day 2, add 1 to get the actual day number in PnL_Records
        deficit_days.append((actual_day, diff))  # Store days with deficit

def get_deficit_amount(record):
    return record[1]

# Sort deficit_days using the custom function
deficit_days.sort(key=get_deficit_amount, reverse=True)

print(deficit_days)
