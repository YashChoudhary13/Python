print("Welcome to the tip calculator.")
bill = input("What was the total bill> $")
tip = input("How much tip would you like to give? 10, 12 or 15? ")
split = input("How many peoeple to split the bill? ")
bill = float(bill)
tip = int(tip)
split = float(split)
if tip in [10,12,15] :
    total_bill = ((tip / 100 * bill) + bill) / split
    print("Each Person should pay:", total_bill)
else :
    print("Invalid Tip Input")