# Write a Python Pizza Delivery Program, for more details refer to 100 days of python with Dr. Angela Day 3 content.
print("Welcome to Python Pizza Delivery")
size = input("What size Pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == 'L' :
    bill += 25
    if pepperoni == 'Y' :
        bill += 3
if size == 'M' :
    bill += 20
    if pepperoni == 'Y' :
        bill += 3
if size == 'S' :
    bill += 15
    if pepperoni == 'Y' :
        bill += 2
if extra_cheese == 'Y' :
    bill += 1
print(f"Your total bill is: ${bill}")
breakdown = input("Do you want a breakdown of your bill? Y or N: ")
if breakdown == 'Y' :
    if size == 'L' :
        print("Cost of a Large Pizza is $25")
        if pepperoni == 'Y' :
            print("Cost of pepperoni is $3 in Large and Medium Pizzas")
    elif size == 'M' :
        print("Cost of the Medium Pizza is $20")
        if pepperoni == 'Y' :
            print("Cost of pepperoni is $3 in Large and Medium Pizzas")
    elif size == 'S' :
        print("Cost of a Small Pizza is $15")
        if pepperoni == 'Y' :
            print("Cost of pepperoni is $2 in Small Pizza")
    if extra_cheese == 'Y' :
        print("Cost of extra cheese is $1")
print("Thank you for Ordering Pizza from Python Pizza Delivery")
payment = input("How would you like to pay the bill? CASH or ONLINE: ")
if payment == 'CASH' :
    print("Wonderful! Please wait while we deliver your pizza to your doorstep")
if payment == 'ONLINE' :
    print("Wonderful! You can do the online payment once the pizza is delivered to you, our delivery partner will assist you in the payment process to ensure there is no inconvenience caused, Once again, Thank you for ordering from Python Pizza Delivery!")

