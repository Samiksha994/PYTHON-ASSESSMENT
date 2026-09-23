# (Program to check whether a given year is a leap year or not)

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("The given year is a leap year")

elif year % 100 == 0:
    print("The given year is not a leap year")

elif year % 4 == 0:
    print("The given year is a leap year")

else:
    print("The given year is not a leap year")



