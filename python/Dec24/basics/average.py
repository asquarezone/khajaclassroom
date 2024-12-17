maths = 89
physics = 72
chemistry = 67
average = (maths + physics + chemistry) / 3
print(average)

if average >= 90 and average < 100:
    print("Grade A")
elif average >= 80 and average < 90:
    print("Grade B")
elif average >= 70 and average < 80:
    print("Grade C")
elif average >= 60 and average < 70:
    print("Grade D")
elif average >= 0 and average < 60:
    print("Grade E")
else:
    print("Something went wrong, only prayers can fix this")
