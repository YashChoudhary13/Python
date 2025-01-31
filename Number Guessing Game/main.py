import random
print("Welcome to the Number Guessing Game!")
def attempts():
    
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print("Invalid Input")
    
def play():
    random_number = random.choice(range(1, 101))
    print("I am thinking of a number between 1 and 100")
    attempts_left = attempts()
    while attempts_left > 0:
        print(f'You have {attempts_left} attempts remaining to guess the number')
        guess = int(input("Make a guess: "))
        if guess > random_number :
            print("Too high")
            
        elif guess < random_number :
            print("Too Low")
        elif guess == random_number:
            print("You have guessed it right!")
            break
        attempts_left -= 1
    if attempts_left == 0:
        print("You lost, Better luck next time. ")
while True:
    start = input("Start game, Y or N: ").lower()
    if start == 'y' :
        play()
    else:
        break
    

