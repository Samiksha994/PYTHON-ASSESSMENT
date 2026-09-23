# (Program to calculate the sum of first N natural numbers using a while loop)

n = int(input("Enter a number: "))
i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1
print("Sum of first", n, "natural numbers is:", total)





