student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
sum = 0 
for score in student_scores :
    sum += score
print(sum)
new_sum = 0
for numbers in range(1,101) :
    new_sum += numbers
print(new_sum)
#
for number in range (1,101) :
    if number % 3 == 0 and number % 5 == 0 :
        number = "FizzBuzz"
    elif number % 3 == 0 :
        number = "Fizz"
    elif number % 5 == 0 :
        number = "Buzz"
    print (number)
    