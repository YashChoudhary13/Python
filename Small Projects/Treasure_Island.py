print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
First_challange = input("You're at a cross road. Where do you want to go?\nType 'left' or 'right'\n").lower()
if First_challange == 'right' :
    print("Game Over")
if First_challange == 'left' :
    Second_challange = input("You've come to a Lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if Second_challange == 'swim' :
        print("Game Over")
    elif Second_challange == 'wait' :
        Third_challange = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if Third_challange == 'yellow' :
            print("YOU WIN!")
        else :
            print("Game Over")
    else :
        print("Undefined Input")