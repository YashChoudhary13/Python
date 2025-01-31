# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

import random
option = input("Do you want to give a word of your own? Y or N: ").lower()
if option == 'y' :
    chosen_word = input("Write your word: ").lower()
elif option == 'n' :
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
else :
    print('Invalid Input, please answer in Y or N')

blanks = ['_ '] * len(chosen_word)
print(''.join(blanks))

while True:
    str_lives = input("Enter the number of lives you want(Max = 5): ")
    if len(str_lives) == 1 and str_lives.isalnum() and int(str_lives) in range(1,6):
        break
    else:
        print("Input is invalid, please enter a number in range of 1 - 5")
lives = int(str_lives)
while True:
    while True:
        guess = input("Guess a letter of the chosen word: ").lower()
        if len(guess) == 1 and guess.isalpha() :
            break
        else:
            print("Invalid Input! Please guess a single alphabet only.")
    if guess in chosen_word :
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess :
                blanks[i] = guess
            else:
                continue
    else :
        lives -= 1
        print(f"Remaining lives {lives}")
    print(''.join(blanks))
    if lives == 0 :
        print("Game Over, You lost all your lives")
        break
    elif ''.join(blanks).lower() == chosen_word :
        print(f"You won the game with remaining {lives} lives. Congratulations!")
        break
