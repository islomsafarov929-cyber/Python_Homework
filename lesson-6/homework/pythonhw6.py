# Task 1.Given a string txt, insert an underscore (_) after every third character.
#  If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. 
# No underscore should be added at the end.
# Task 1. Insert underscore after every 3rd character,
# but skip vowels or when the next char already has '_'.
txt = "abcabcabcdeabcdefabcdefg"
vowels = "aeiouAEIOU"

result = []
count = 0
i = 0

while i < len(txt):
    result.append(txt[i])
    count += 1

    if count == 3:
        next_pos = i + 1

        # If current character is vowel or next character is underscore → shift
        if txt[i] in vowels or (next_pos < len(txt) and txt[next_pos] == "_"):
            if next_pos < len(txt):
                result.append(txt[next_pos])
                i += 1  # Skip one extra character

        # Don't add underscore at the very end
        if i + 1 < len(txt):
            result.append("_")

        count = 0

    i += 1

print(''.join(result))



# Task 2.The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input("Enter a number: "))

if 1 <= n <= 20:
    for i in range(n):
        print(i ** 2)
else:
    print("n must be between 1 and 20.")
    

# Task 3
# Exercise 1: Print first 10 natural numbers using a while loop
num = 1

while num <= 10:
    print(num)

    num += 1

# Exercise 2: Print the following pattern

for row in range(1,6):
    for ns in range(1, row + 1):
        print(ns, end = " ")
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number

number = int(input("Enter a number:"))

result = 0

for i in range(1,number + 1):
    result += i

print(f"Up to {number}","\nSum is:", result)

# Exercise 4: Print multiplication table of a given number

number = int(input("Enter a number:"))

for i in range(1,number + 1):
    print(i+i)

# Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)


# Exercise 6: Count the total number of digits in a number

big_num = list(input("Enter any number"))

print("Count of digits in given number:", len(big_num))

# Exercise 7: Print reverse number pattern

for i in range(5, 0, -1):         # 5 dan 1 gacha kamayib boradi
    for j in range(i, 0, -1):     # har bir qatorda i dan 1 gacha kamayadi
        print(j, end=' ')
    print()                       # har bir qatordan keyin yangi qator


# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]


for i in sorted(list1, reverse=True):
    print(i)


# Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution
 
for i in range(1,8):
    print(i)
print("Done!")


# Exercise 11: Print all prime numbers within a range

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(25,50):
    if is_prime(i):
        print(i, end = " ")

# Exercise 12: Display Fibonacci series up to 10 terms
 
n = int(input("Nechta Fibonacci soni kerak: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

# Exercise 13: Find the factorial of a given number

fact_num = int(input("Enter a number for factorial:"))
fact = 1

for i in range(1,fact_num+1):
    fact *= i
print(f"{fact_num}! =",fact)

# Task4.Return the elements that are not common between two lists. The order of elements does not matter.

# input 1
list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(list(set(list1).symmetric_difference(set(list2))))

# input 2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(set(list1).symmetric_difference(set(list2))))

# input 3
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(list(set(list1).symmetric_difference(set(list2))))



 
