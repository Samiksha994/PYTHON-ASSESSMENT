# (Program to find the largest of three numbers)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x == y == z:
    print("All three numbers are equal")

elif x == y:
    if x > z:
        print("First and second numbers are equal and largest")
    else:
        print("Third number is largest")

elif y == z:
    if y > x:
        print("Second and third numbers are equal and largest")
    else:
        print("First number is largest")

elif x == z:
    if x > y:
        print("First and third numbers are equal and largest")
    else:
        print("Second number is largest")

elif x > y and x > z:
    print("First number is largest")

elif y > x and y > z:
    print("Second number is largest")

else:
    print("Third number is largest")



