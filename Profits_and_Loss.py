from pathlib import Path
import csv

print (Path.cwd() )
def PnL_analysis():
    fp = Path.cwd() / "csv_reports" / "Profit_and_Loss.csv" # Define the file path for the Profit_and_Loss csv file 

    with fp.open(mode="r", encoding="UTF-8", newline="") as file: #Open CSV file as read in UTF-8 formatting 
        file_reader = csv.reader(file)
        next(file_reader) # skip header

        PnL_Records=[] # Initialize list to store day and Net Profit records
        daily_PnL_difference = [] #Initialize list to store daily difference in Net Profit
        
        for row in file_reader: # For loop to iterate through each row and store the day and Net Profit data in PnL_Records list
            day = int(row[0]) # Convert day to integer from string
            Net_Profit = float(row[4])  # Convert overhead value to float for calculation
            PnL_Records.append([day,Net_Profit]) #append list to store day and Net Profit records       
 
        for day_index in range(1, len(PnL_Records)): # For loop to Iterate over the Net_Profit data (index 1) from the
            # PnL_Records list
            previous_day_profit = PnL_Records[day_index - 1][1] # Retrieve the Net Profit amount of the previous day using the current index minus one
            current_day_profit = PnL_Records[day_index][1] # Retrieve the Net Profit amount for the current day
            difference = current_day_profit - previous_day_profit # Calculate the difference in Net Profit between the current day and the previous day
            daily_PnL_difference.append((PnL_Records [day_index][0], difference))  # Append a tuple to the daily_coh_difference list, 
            # containing the current day and the calculated difference from the previous day
        
        is_increasing = all(diff[1] > 0 for diff in daily_PnL_difference) # Check for consistent increase in Net Profit
        is_decreasing = all(diff[1] < 0 for diff in daily_PnL_difference) #Check for consistent decrease in Net Profit
        
        def custom_sort(item): # Custom sort function to sort list data by the difference amount
            return item[1]

        if is_increasing:
            highest_increment = max (daily_PnL_difference)  #return highest Net Profit surplus difference and day if Net Profit is consistently increasing
            return f' [NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n [HIGHEST NET PROFIT SURPLUS] DAY: {highest_increment [0]}, AMOUNT: SGD{highest_increment [1]}' 
        elif is_decreasing:
            lowest_increment = min (daily_PnL_difference) #return highest Net Profit deficit difference and day if cash on hand is consistently decreasing
            return f' [NET PROFIT DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY \n [HIGHEST PROFIT DEFICIT] DAY: {lowest_increment [0]}, AMOUNT: SGD{lowest_increment [1]}' 
        else:
            deficit_days = [(day, diff) for day, diff in daily_PnL_difference if diff < 0]
            deficit_days.sort(key=custom_sort)  # Identify all days with Net Profit deficits and sort them using the custom sort created
            top_deficits = deficit_days[:3]  # Identify the top three deficits from deficit days
            # Construct output lines with the required formatting
            output_lines = [f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount):.0f}" for day, amount in deficit_days] # Construct output lines for each deficit day with correct formatting using for loop
            
            # Add the top three deficits separately with correct formatting
            output_lines.append(f"[HIGHEST NET PROFIT DEFICIT] DAY: {top_deficits[0][0]}, AMOUNT: SGD{abs(top_deficits[0][1]):.2f}")
            output_lines.append(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {top_deficits[1][0]}, AMOUNT: SGD{abs(top_deficits[1][1]):.2f}")
            output_lines.append(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {top_deficits[2][0]}, AMOUNT: SGD{abs(top_deficits[2][1]):.2f}")
        return '\n'.join(output_lines) # Return a combined the list of strings into a single string separated by a newline
