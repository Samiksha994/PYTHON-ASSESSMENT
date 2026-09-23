
# (Program to print a pyramid pattern)

number_of_rows = int(input("Enter the number of rows: "))

for i in range(1, number_of_rows + 1):
    spaces = number_of_rows - i
    stars = (2 * i) - 1
    print(" " * spaces + "*" * stars)


