# TODO-1: Ask the user for input
import os
bidders = {}
while True:
    name = input("Enter your name\n").lower()
    bid = int(input("Enter your bid amount:\n$"))
    bidders[name] = bid
    ask = input("Are there any others who need to bid? Y or N: ").lower()
    os.system('clear')
    if ask == 'y' :
        continue
    elif ask == 'n' :
        break
    else :
        print("Invalid Input")

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

original_bid = 0
for bids in bidders :
    bidding_amount = bidders[bids]
    if bidding_amount > original_bid :
        original_bid = bidding_amount
        winner_bid = bids
print(f"The largest bid was ${original_bid} and the winner is =>>> {winner_bid.upper()}")