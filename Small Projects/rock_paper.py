import random
rock = '''
_______
---'   ____)
      (_____)``
      (_____)
      (____)
---.__(___)
'''

paper = '''
_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
rps = int(rps)
if rps == 0 :
    print(rock)
elif rps == 1 :
    print(paper)
elif rps == 2 :
    print(scissors)
else :
    print("Invalid Input")

print("Computer chose: ")
random_rps = random.randint(0,2)
random_rps = int(random_rps)
if random_rps == 0 :
    print(rock)
    if rps == 0 :
        print ("DRAW")
    elif rps == 1 :
        print ("You Win")
    elif rps == 2 :
        print ("You Lose")
    else :
        print('Invalid Input')
elif random_rps == 1 :
    print(paper)
    if rps == 0 :
        print ("You Lose")
    elif rps == 1 :
        print ("DRAW")
    elif rps == 2 :
        print ("You win")
    else :
        print('Invalid Input')
elif random_rps == 2 :
    print(scissors)
    if rps == 0 :
        print ("You Win")
    elif rps == 1 :
        print ("You Lose")
    elif rps == 2 :
        print ("DRAW")
    else :
        print('Invalid Input')
else :
    print("Invalid Input")
