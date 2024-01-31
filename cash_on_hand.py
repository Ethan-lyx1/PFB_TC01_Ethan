from pathlib import Path
import csv

def cash_on_hand_analysis():
    ''' Function analyzes the Cash on Hand (COH) data from a CSV file and reports on daily net profit changes.

    This function reads data from 'Cash_on_Hand.csv' in the 'csv_reports' directory relative to the current working directory.
    It calculates the daily differences in cash on hand and identifies trends as consistently increasing, consistently decreasing, 
    or fluctuating. Based on the trend, it reports either a cash surplus or deficit, along with the highest surplus/deficit, 
    or in the case of fluctuating trends, the top three cash deficits and every day that has a cash deficit.

    Returns:
        str: A string summarizing the cash on hand analysis results in a readable format.
    '''

    fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"  # Define the file path for the Cash_on_Hand csv file

    with fp.open(mode="r", encoding="UTF-8", newline="") as file: # Open CSV file as read in UTF-8 formatting 
        file_reader = csv.reader(file)
        next(file_reader) # skip header

        Cash_on_Hand_Records=[] # Initialize list to store day and cash on hand records
        daily_coh_difference = [] # Initialize list to store the daily difference in cash on hand

        for row in file_reader:  # For loop to iterate through each row and store the day and cash on hand in Cash_on_Hand_Records
            day = int(row[0]) # convert day to integer from string
            cash_on_hand = float(row[1])  # Convert cash on hand value to a number for calculation
            Cash_on_Hand_Records.append([day,cash_on_hand]) #append list to store day and cash on hand records
           
        for day_index in range(1, len(Cash_on_Hand_Records)): # For loop to Iterate over the cash on hand data (index 1) from the
            #Cash_on_Hand_Records list
            previous_day_coh = Cash_on_Hand_Records[day_index - 1][1]  # Retrieve the cash on hand amount of the previous day using the current index minus one
            current_day_coh = Cash_on_Hand_Records[day_index][1]  # Retrieve the cash on hand amount for the current day
            difference = current_day_coh - previous_day_coh # Calculate the difference in cash on hand between the current day and the previous day
            daily_coh_difference.append((Cash_on_Hand_Records[day_index][0], difference))    # Append a tuple to the daily_coh_difference list, 
            #containing the current day and the calculated difference from the previous day

        
        is_increasing = all(diff[1] > 0 for diff in daily_coh_difference)# Check for consistent increase in cash on hand
        is_decreasing = all(diff[1] < 0 for diff in daily_coh_difference) # Check for consistent decrease in cash on hand
        
        def custom_sort(item):  # Custom sort function to sort list data by the difference amount
            return item[1]

        if is_increasing:
            highest_increment = max (daily_coh_difference) #return highest cash surplus difference if cash on hand is consistently increasing
            return f' [CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n [HIGHEST CASH SURPLUS] DAY: {highest_increment [0]}, AMOUNT: SGD{highest_increment [1]}' 
        elif is_decreasing:
            lowest_increment = min (daily_coh_difference) #return largest cash deficit difference if cash on hand is consistently decreasing
            return f' [CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY \n [HIGHEST CASH DEFICIT] DAY: {lowest_increment [0]}, AMOUNT: SGD{lowest_increment [1]}' 
        else: # For if cash on hand is fluctuating
            deficit_days = [(day, diff) for day, diff in daily_coh_difference if diff < 0]
            deficit_days.sort(key=custom_sort)  # Identify days with cash deficits and sort them using the custom sort created
            top_deficits = deficit_days[:3]  # Identify the top three deficits from deficit days
            output_lines = [f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount):.0f}" for day, amount in deficit_days] # Construct output lines for each deficit day with correct formatting using for loop
            # Add the top three deficits separately with correct formatting
            output_lines.append(f"[HIGHEST CASH DEFICIT] DAY: {top_deficits[0][0]}, AMOUNT: SGD{abs(top_deficits[0][1]):.2f}")
            output_lines.append(f"[2ND HIGHEST CASH DEFICIT] DAY: {top_deficits[1][0]}, AMOUNT: SGD{abs(top_deficits[1][1]):.2f}")
            output_lines.append(f"[3RD HIGHEST CASH DEFICIT] DAY: {top_deficits[2][0]}, AMOUNT: SGD{abs(top_deficits[2][1]):.2f}")
        return '\n'.join(output_lines) # Combine the list of strings into a single string separated by a newline
