from pathlib import Path
import csv

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
            previous_day_coh = Cash_on_Hand_Records[day_index - 1][1]
            current_day_coh = Cash_on_Hand_Records[day_index][1]
            difference = current_day_coh - previous_day_coh
            daily_coh_difference.append((Cash_on_Hand_Records[day_index][0], difference))  # Tuple of day and difference
        
        is_increasing = all(diff[1] > 0 for diff in daily_coh_difference)
        is_decreasing = all(diff[1] < 0 for diff in daily_coh_difference)
        def custom_sort(item):
            return item[1]

        if is_increasing:
            highest_increment = max (daily_coh_difference)
            return f' [CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n [HIGHEST CASH SURPLUS] DAY: {highest_increment [0]}, AMOUNT: SGD{highest_increment [1]}' 
        elif is_decreasing:
            lowest_increment = min (daily_coh_difference)
            return f' [CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY \n [HIGHEST CASH SURPLUS] DAY: {lowest_increment [0]}, AMOUNT: SGD{lowest_increment [1]}' 
        else:
            deficit_days = [(day, diff) for day, diff in daily_coh_difference if diff < 0]
            deficit_days.sort(key=custom_sort)  # Sort by deficit amount
            # Identify top three deficits
            top_deficits = deficit_days[:3]
            # Construct output lines with the required formatting
            output_lines = [f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{abs(amount):.0f}" for day, amount in deficit_days]
            # Add the top three separately with the required labeling
            output_lines.append(f"[HIGHEST CASH DEFICIT] DAY: {top_deficits[0][0]}, AMOUNT: USD{abs(top_deficits[0][1]):.2f}")
            output_lines.append(f"[2ND HIGHEST CASH DEFICIT] DAY: {top_deficits[1][0]}, AMOUNT: USD{abs(top_deficits[1][1]):.2f}")
            output_lines.append(f"[3RD HIGHEST CASH DEFICIT] DAY: {top_deficits[2][0]}, AMOUNT: USD{abs(top_deficits[2][1]):.2f}")
        return '\n'.join(output_lines)
