print(type("Hello, World!"))
print(type(17))
print(type(3.2))
print(type(True))

#Make this line of code work:
# print("Number of letters in your name: " + len(input("What is your name? ")))
#SOLUTION:
print("Number of letters in your name: " + str(len(input("What is your name? "))) )