from pathlib import Path 
import cash_on_hand
import overheads
import Profits_and_Loss #import other modules created

fp = Path.cwd() / "summary_report.txt" #create file path for summary_report.txt to be written in

with fp.open(mode="w", encoding="UTF-8") as file: # Open the file in write mode with UTF-8 encoding
    # Write the analysis results from each module to the file
    # Each result is written on a new line using \n
    file.write(overheads.read_over_and_find_highest_overhead() + "\n") 
    file.write(cash_on_hand.cash_on_hand_analysis() + "\n")
    file.write((Profits_and_Loss.PnL_analysis()))
