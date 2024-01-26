from pathlib import Path
import cash_on_hand
import overheads
import Profits_and_Loss

fp = Path.cwd() / "summary_report.txt"
with fp.open(mode="w", encoding="UTF-8") as file:
    file.write(overheads.read_over_and_find_highest_overhead() + "\n") 
    file.write(cash_on_hand.cash_on_hand_analysis() + "\n")
    file.write((Profits_and_Loss.PnL_analysis()))
