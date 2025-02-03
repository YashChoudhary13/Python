#COFFEE MACHINE
from menu import MENU, resources

def report():
    resources["water"]
    resources["milk"]
    resources["coffee"]
    if resources["water"] > 0 and resources["milk"] > 0 and resources["coffee"] > 0:
        return f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {money}"

def change(requirement):
    print("Please Insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + 0.10 * dimes + 0.5 * nickles + 0.01 * pennies
    change = total - MENU[requirement]["cost"]
    return change

def resource(requirement):
    global money
    resources["water"] = resources["water"] - MENU[requirement]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[requirement]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[requirement]["ingredients"]["coffee"]
    money += MENU[requirement]["cost"]
    if resources["water"] < 0:
        return "Sorry, There is not enough water "
    elif resources["milk"] < 0:
        return "Sorry, there is not enough milk"
    elif resources["coffee"] < 0:
        return "Sorry there is not enough coffee"
money = 0
while True:
    requirement = input("What would you like? (espresso/latte/cappuccino): ")
    if requirement == 'report' :
        print(report())
    elif requirement == 'off' :
        break
    elif requirement == 'espresso' or requirement == 'latte' or requirement == 'cappuccino':
        result = resource(requirement)
        if isinstance(result, str) :
            print(result)
            continue
        changes = change(requirement)
        if changes < 0 :
            print("Sorry that's not enough money. Money refunded")
        elif changes >= 0 :
            print(f"Here is ${changes} in change ")
            print(f"Here is your {requirement} ☕️ Enjoy!")
    else:
        print("Invalid input, please try again")
     

