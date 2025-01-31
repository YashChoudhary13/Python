# def life_in_weeks(current_age):
#     remaining_time = (90*52) - (current_age*52)
#     print(f"You have {remaining_time} weeks left")
    
# current_age = int(input())
# life_in_weeks(current_age)
def calculate_love_score(name1, name2):
    name = name1 + name2
    true = "true"
    love = "love"
    count1 = sum(1 for char in name if char in true)
    count2 = sum(1 for char in name if char in love)
    print(str(count1) + str(count2))

name1 = input("Enter first name")
name2 = input("Enter second name")


