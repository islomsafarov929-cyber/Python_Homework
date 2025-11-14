# Task 1. Finding it's leap year or not.

# should be divisable by 4
#  should not be divisable by 100
#  should be divisable by 400

year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not a leap year.")

# Task 2.Given an integer, n, perform the following conditional actions:

# constraint: 1 <= n <= 100
# if n odd number then "Weird"
# if n even and inclusive range of 2 to 5 than "Not Weird"
# if n even and inclusive range of 6 to 20 than "Weird"
# if n even and greater than 20 "Not Weird"

num = int(input("Enter a number:"))

if num in range(1,101): #constraint
    if num % 2 == 0:  #even
        if num in range(2,6): #inclusive range of 2 to 5
            print("Not Weird")
        elif num in range(6,21): #inclusive range of 6 to 20
            print("Weird")
        else: # greater than 20
            print("Not Weird")
    else: #odd
        print("Weird")   
else: #outside of constraint
    print("Number broke the constraint!")


# Task 3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

# Solution 1.With if-else

a = 7
b = 23

if a > b:
    a, b = b, a  # a har doim kichik bo'lishi uchun almashtiramiz

# Juft boshlanish nuqtasini topamiz
start = a if a % 2 == 0 else a + 1

even_numbers = list(range(start, b + 1, 2))

print(even_numbers)

# Solution 2.Without uf-else

a = 7
b = 23

start, end = sorted((a, b))

even_numbers = list(range(start + start % 2, end + 1, 2))

print(even_numbers)



