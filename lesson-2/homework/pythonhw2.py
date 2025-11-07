#Task 1.Python program to ask for a user's name and year of birth, then calculate and display their age.
#Foydalanuvchidan tug;ilgan yilini so'rovchi, va shunga qarab yoshni hisoblovchi python code.

from datetime import datetime

current_year = datetime.now().year

current_year

name = input("Enter your name:").strip().capitalize()
year_of_birth = int(input("Enter your year of birth:").strip())

print("Name:" ,name,"\nAge:" ,current_year - year_of_birth)

#Task 2.Extract car names.
#Avtomobil nomlarini ajratib olish.

txt = 'LMaasleitbtui'

car1 = txt[::2]
car2 = txt[1::2]

print(car1)
print(car2)

#Task 3.Extract car names.
#Avtomobil nomlarinin ajratib olish.

txt = 'MsaatmiazD'

car1 = txt[::2]
car2 = txt[::-2]

print(car1)
print(car2)

#Task 4.Extract the residence area. 
#Turarjoyni ahratib olish.

txt = "I'am John. I am from London"

txt.split("from")[1].strip()

#Task 5.Python program that takes a user input string and prints it in reverse order.
#Foydalanuvchidan yozuv so'rab uni teskari tartibda yozuvchu python code.

string = input("Enter random string:").strip()

string[::-1]

#Task 6.Python program that counts the number of vowels in a given string.
#Berilgan yozuvdagi unli harflarni sanovchi python code.

my_str = "Hello, don't to tell me what to do"
 
vowels = "aeiou"

total_of_vowels = sum(1 for v in my_str.lower() if v in vowels)

total_of_vowels

#Task 7.Python program that takes a list of numbers as input and prints the maximum value.
#Berilgan sonlarning olib, ularning eng kattasini chiqaruvchi python code.

nums = input("Enter list of random numbers splitted with comma:").strip().strip(",")

max_number = [int(num) for num in nums.split(",")]

max(max_number)

#Task 8.Python program that checks if a given word is a palindrome.
# Berilgan so'z palindrom yoki yo'qligini tekshiruvchi python code.

my_str = 'Anna'

if my_str.lower() == my_str[::-1].lower():
    print('Palindrome')
else:
    print('Not Palindrome')

#Task 9. Python program that extracts and prints the domain from an email address provided by the user.
#Emailning domain qismini kesib olib uni chqaruvchi python code.

email = "safarovdev3489@outlook.com"

email.split("@")[1]

#Task 10.Python program to generate a random password containing letters, digits, and special characters.
#Raqamlar, harflar va maxsus belgilardan tashkil topgan parol yaratuvchi python code.

import random
import string

length = int(input("Enter length of password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range(length))

print("Your password:", password)
