year = 2001
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
else:
    print("not a leap year")

# is_div_by_4 = year % 4 == 0
# is_div_by_100 = year % 100 == 0
# is_div_by_400 = year % 400 == 0
# is_leap_year = True if is_div_by_4 and (not is_div_by_100 or (is_div_by_100 and is_div_by_400)) else False
# print(is_leap_year)
