from pathlib import Path
import csv

print (Path.cwd() )
def PnL_analysis():
    fp = Path.cwd() / "csv_reports" / "Profit_and_Loss.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        file_reader = csv.reader(file)
        next(file_reader) # skip header

        PnL_Records=[] 

        for row in file_reader:
            day = int(row[0])
            Net_Profit = float(row[4])  # Convert overhead value to a number
            PnL_Records.append([day,Net_Profit])
           
            daily_PnL_difference = []

        for day_index in range(1, len(PnL_Records)):
            previous_day_profit = PnL_Records[day_index - 1][1]
            current_day_profit = PnL_Records[day_index][1]
            difference = current_day_profit - previous_day_profit
            daily_PnL_difference.append((PnL_Records [day_index][0], difference))  # Tuple of day and difference
        
        is_increasing = all(diff[1] > 0 for diff in daily_PnL_difference)
        is_decreasing = all(diff[1] < 0 for diff in daily_PnL_difference)
        def custom_sort(item):
            return item[1]

        if is_increasing:
            highest_increment = max (daily_PnL_difference)
            return f' [NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n [HIGHEST NET PROFIT SURPLUS] DAY: {highest_increment [0]}, AMOUNT: SGD{highest_increment [1]}' 
        elif is_decreasing:
            lowest_increment = min (daily_PnL_difference)
            return f' [NET PROFIT DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY \n [HIGHEST PROFIT DEFICIT] DAY: {lowest_increment [0]}, AMOUNT: SGD{lowest_increment [1]}' 
        else:
            deficit_days = [(day, diff) for day, diff in daily_PnL_difference if diff < 0]
            deficit_days.sort(key=custom_sort)  # Sort by deficit amount
            # Identify top three deficits
            top_deficits = deficit_days[:3]
            # Construct output lines with the required formatting
            output_lines = [f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{abs(amount):.0f}" for day, amount in deficit_days]
            # Add the top three separately with the required labeling
            output_lines.append(f"[HIGHEST NET PROFIT DEFICIT] DAY: {top_deficits[0][0]}, AMOUNT: USD{abs(top_deficits[0][1]):.2f}")
            output_lines.append(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {top_deficits[1][0]}, AMOUNT: USD{abs(top_deficits[1][1]):.2f}")
            output_lines.append(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {top_deficits[2][0]}, AMOUNT: USD{abs(top_deficits[2][1]):.2f}")
        return '\n'.join(output_lines)
