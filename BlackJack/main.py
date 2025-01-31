import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while True:
    start = input("START GAME | Y or N: ").lower()


    while start == 'y' :
        money = int(input("How much money should the game start with? Enter amount within range of 100-1000: "))
        if money in range(100, 1001):
            while money in range(1,1501) :
                computer = []
                player = []
                player_sum = 0
                computer_sum = 0
                for i in range(2):
                    computer.append(random.choice(cards))
                    player.append(random.choice(cards))
                    player_sum += player[i]
                    computer_sum += computer[i]
                bet = int(input(f"You have {money} left. Enter the bet amount for this round: "))
                print("Your cards are:", *player)
                print("Computer's first card is", computer[0])
                while True:
                    if player_sum == 21:
                        print("Black Jack")
                        choice = "stand"
                    else:
                        choice = input("STAND or HIT: ").lower()
                    computer_inputs = ["stand","hit"]
                    if choice == "stand":
                        print(*computer)
                        if computer_sum == 21:
                            print("Black Jack")
                            computer_choice = "stand"
                        else:
                            computer_choice = random.choice(computer_inputs)
                        if computer_choice == "stand":
                            if player_sum > computer_sum:
                                print("Player Wins")
                                money += bet
                                break
                            elif player_sum == computer_sum:
                                print("Draw")
                                break
                            else:
                                print("Dealer Wins")
                                money -= bet
                                break
                        elif computer_choice == "hit":
                            if computer_sum < 21:
                                new_card = random.choice(cards)
                                computer.append(new_card)
                                computer_sum += new_card
                            elif computer_sum > 21:
                                print("Busted")
                                print("Player Wins")
                                money += bet
                                break
                    if choice == "hit":
                        new_card_p = random.choice(cards)
                        player.append(new_card_p)
                        player_sum += new_card_p
                        print(*player)
                        if player_sum > 21:
                            print("Busted")
                            print("Dealer Wins")
                            money -= bet
                            break
                if money == 0 :
                    print("BANKRUPT! You have no money left")
                    break
                elif money > 1500 :
                    print("You have reached the maximum limit of winnings, Congratulations!")
                    break
            break
        else:
            print("Invalid amount, please enter again")

    if start == 'n' :
        print("\n" * 5)
