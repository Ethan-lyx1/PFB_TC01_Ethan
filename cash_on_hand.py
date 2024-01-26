from pathlib import Path
import csv

print (Path.cwd() )
def cash_on_hand_analysis():
    fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        file_reader = csv.reader(file)
        next(file_reader) # skip header

        Cash_on_Hand_Records=[] 

        for row in file_reader:
            day = int(row[0])
            cash_on_hand = float(row[1])  # Convert overhead value to a number
            Cash_on_Hand_Records.append([day,cash_on_hand])
           
            daily_coh_difference = []

        for day_index in range(1, len(Cash_on_Hand_Records)):
            previous_day_profit = Cash_on_Hand_Records[day_index - 1][1]
            current_day_profit = Cash_on_Hand_Records[day_index][1]
            difference = current_day_profit - previous_day_profit
            daily_coh_difference.append((Cash_on_Hand_Records[day_index][0], difference))  # Tuple of day and difference
        
        is_increasing = all(diff[1] > 0 for diff in daily_coh_difference)
        is_decreasing = all(diff[1] < 0 for diff in daily_coh_difference)

        if is_increasing:
            highest_increment = max (daily_coh_difference)
            return highest_increment
        elif is_decreasing:
            lowest_increment = min (daily_coh_difference)
            return lowest_increment
        else:
            def custom_sort(item):
                return item[1]
            deficit_days = [(day, diff) for day, diff in daily_coh_difference if diff < 0]
            deficit_days.sort(key=custom_sort)  # Sort by deficit amount
            return deficit_days



