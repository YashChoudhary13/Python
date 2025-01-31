def is_leap_year(year):
    if year % 4 == 0 :
        possible_leap_year = year
        if possible_leap_year % 100  == 0 and possible_leap_year % 400 == 0:
            return (True)
        elif possible_leap_year % 100 == 0 and possible_leap_year % 400 != 0 :
            return (False)
        else :
            return (True)
    else :
        return(False)
        
year = int(input())
print(is_leap_year(year))
    # Don't change the function name.