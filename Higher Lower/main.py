import random
import os
import art


data = [("Kylie Jenner 🇺🇸 Model, Businesswoman (USA)",400), ("Lionel Messi 🇦🇷 Footballer (Argentina)",485), ("Dwayne “The Rock” Johnson 🇺🇸 Actor, Wrestler, Businessman (USA)",395),("Selena Gomes 🇺🇸 Singer, Actress (USA)",429),("Kim Kardashian followers 🇺🇸 TV Personality, Businesswoman (USA)",364),("Virat Kohli followers 🇮🇳 Cricketer (India)",264),("Zendaya followers 🇺🇸 Actress, Singer (USA)",185),("MrBeast (Jimmy Donaldson) followers 🇺🇸 YouTuber, Philanthropist (USA)",50),("NASA followers 🇺🇸 Space Agency (USA)",98)]

personality_A = random.choice(data)

while True:
    A = personality_A[0]
    print(art.logo)
    print("Compare A:", A)
    print(art.vs)
    personality_B = random.choice(data)
    B = personality_B[0]
    print("Against B:", B)
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    os.system("clear")
    current_score = 0
    if personality_A[1] > personality_B[1] and guess == 'A':
        current_score += 1
        print(f"You're right! Current score: {current_score}")
    elif personality_A[1] < personality_B[1] and guess == 'B' :
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        personality_A = personality_B
    else :
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {current_score}")
        break
