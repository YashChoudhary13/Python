import random

#random_integer = random.randint(1,2)
#if random_integer == 1 :
#    print("Heads")
#if random_integer == 2 :
#    print("Tails")
#random_float = random.uniform(0,5)
#print(random_float)
#random_0to1 = random.random()
#print(random_0to1)
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#for friend in friends :
#   print(friend)
random_friend = random.randint(0,4)
print(friends[random_friend])
print(random.choice(friends))