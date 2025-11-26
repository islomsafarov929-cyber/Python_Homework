# Exeption Handling Tasks
# Task 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    num = int()
    7 / num
except ZeroDivisionError:
    print("You can't divise a number to a 0")


# Task 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    user_number = int(input("Enter an integer:"))
except ValueError:
    print("You should give an integer!")

# Task 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    open('/Python/Lesson-8', "r")
except FileNotFoundError: 
    print("The file you gave, not found.")


# Task 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Check if both inputs are numeric (including decimals)
    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        raise TypeError("Both inputs must be numerical.")

    # Convert to int and perform operation
    num1 = int(num1)
    num2 = int(num2)
    print("Sum:", num1 + num2)

except TypeError as e:
    print("TypeError:", e)


# Task 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    # Attempt to write to a protected file (likely restricted)
    with open("/root/protected.txt", "w") as f:
        f.write("Hello World")
except PermissionError:
    print("Permission denied: you don't have access to this file.")


# Task 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    my_list = [1,2,3,4]

    my_list[5]
except IndexError:
    print("Your given index is uot of range!")


# Task 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    number = int(input("Enter a number: "))
    print(f"Square of {number} is:", number ** 2)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt caught: user stopped input.")
    

# Task 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    result = 10 / 0   # This raises ZeroDivisionError
except ArithmeticError as e:
    print(f"Arithmetic error caught: {e}")


# Task 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

text = "Привет"  # Cyrillic characters

try:
    # Writing with ASCII encoding (cannot represent Cyrillic)
    with open("output.txt", "w", encoding="ascii") as f:
        f.write(text)
except UnicodeEncodeError as e:
    print("UnicodeEncodeError caught:", e)


# Task 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    my_str = "hello"

    my_str.append("I'm John")
except AttributeError as e:
    print(f"Youre code has an error: {e}")


# File Input/Output Tasks.

# Task 1. Write a Python program to read an entire text file.

with open('output.txt', 'r') as my_file:
    print(my_file.read())
  

# Task 2.Write a Python program to read first n lines of a file.

n = int(input('Enter a number of lines you need:'))

with open('output.txt', 'r') as my_file:
    for i in range(n):

        print(my_file.readline().strip())


# Task 3.Write a Python program to append text to a file and display the text.

with open('output.txt', 'a', encoding='utf-8') as my_file:
    my_file.write('Append text\n')


with open('output.txt', 'r') as appended_file:
    print(appended_file.readlines())


# Task 4.Write a Python program to read last n lines of a file.

n = int(input('Enter number of lines you want:')) 
with open("output.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    last_lines = lines[-n:]   # slice the last n lines
    for line in last_lines:
        print(line.strip())


# Task 5.Write a Python program to read a file line by line and store it into a list.

with open('output.txt', 'r') as f:
    list_line = [line.strip() for line in f.readlines()]
    
    print(list_line)


# Task 6.Write a Python program to read a file line by line and store it into a variable.

file_path = "output.txt"   # replace with your file name

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()   # reads all lines into a list
        print("Stored lines in variable:\n", lines)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")


# Task 7.Write a Python program to read a file line by line and store it into an array.

file_path = "output.txt"   # replace with your file name

with open(file_path, "r", encoding="utf-8") as f:
    lines_array = [line.strip() for line in f]   # strip removes newline characters
print("Stored lines in array:\n", lines_array)


# Task 8. Write a Python program to find the longest words.
with open("output.txt", "r", encoding="utf-8") as f:
    words = f.read().split()   # split text into words by whitespace

# Find the maximum length
max_length = max(len(word) for word in words)

# Collect all words that have this maximum length
longest_words = [word for word in words if len(word) == max_length]

print("Longest word length:", max_length)
print("Longest words:", longest_words)



# Task 9. Write a Python program to count the number of lines in a text file.
count = 0
with open("output.txt", 'r', encoding='utf-8') as f:
    for i in f:
        count += 1

print("Number of lines in the file:", count)



#Task 10 Write a Python program to count the frequency of words in a file.
file_path = "output.txt"

word_freq = {}

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        for word in line.lower().split():
            word_freq[word] = word_freq.get(word, 0) + 1

print("Word frequencies:")
for word, count in word_freq.items():
    print(f"{word.capitalize()}: {count}")

#Task 11 Write a Python program to get the file size of a plain file.
import os

size = os.path.getsize('output.txt')   # get file size in bytes
print(f"File size of 'output.txt': {size} bytes")


#Task 12 Write a Python program to write a list to a file.
my_list = ['element1, ', 'element2, ', 'element3\n'] # or we can write it line by line with \n

with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(my_list)

#Task 13 Write a Python program to copy the contents of a file to another file.
with open('output.txt', 'r', encoding='utf-8') as source:
    content = source.read()

with open('input.txt', 'w', encoding='utf-8') as destination:
    destination.write(content)

#Task 14 Write a Python program to combine each line from the first file with the corresponding line in the second file.
# Program to combine each line from the first file with the corresponding line in the second file

file1 = "output.txt"
file2 = "input.txt"
output_file = "combined.txt"

try:
    with open(file1, "r", encoding="utf-8") as f1, \
         open(file2, "r", encoding="utf-8") as f2, \
         open(output_file, "w", encoding="utf-8") as out:

        # zip() pairs lines from both files
        for line1, line2 in zip(f1, f2):
            combined_line = line1.strip() + " " + line2.strip() + "\n"
            out.write(combined_line)

    print(f"Lines from '{file1}' and '{file2}' combined into '{output_file}'")

except FileNotFoundError:
    print("Error: One of the files was not found.")
except PermissionError:
    print("Error: Permission denied.")

#Task 15 Write a Python program to read a random line from a file.
import random

with open('output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    print(random.choice(lines))

#Task 16 Write a Python program to assess if a file is closed or not.
f = open('output.txt', 'r') 
print("Is file closed?", f.closed) # False = Opened

f.close()
print("Is file closed?", f.closed) # True = Closed

#Task 17 Write a Python program to remove newline characters from a file.
file_path = "output.txt"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read().replace("\n", "")   # remove all newline characters

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

#Task 18 Write a Python program that takes a text file as input and returns the number of words in a given text file.
#Note: Some words can be separated by a comma with no space.
# Program to count the number of words in a text file

file_path = "input.txt"   # replace with your file name

try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Replace commas with spaces to handle "word1,word2" cases
    cleaned_text = text.replace(",", " ")

    # Split into words by whitespace
    words = cleaned_text.split()

    print("Number of words in file:", len(words))

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")

#Task 19 Write a Python program to extract characters from various text files and put them into a list.
import glob

# Use glob to find all .txt files in the current directory
file_list = glob.glob("*.txt")

characters = []

try:
    for file_name in file_list:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()          # read entire file
            characters.extend(list(content))  # add each character to the list

    print("Extracted characters from all text files:")
    print(characters)

except FileNotFoundError:
    print("Error: One or more files not found.")
except PermissionError:
    print("Error: Permission denied.")

# Task 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string

# Loop through uppercase alphabet letters
for letter in string.ascii_uppercase:   # 'A' to 'Z'
    file_name = f"{letter}.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        pass # for no content in them!
    print(f"Created {file_name}")


#Task 21 Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
import string

n = int(input('Enter a number of chunks:'))

# Specify how many letters per line
letters_per_line = n
output_file = "alphabet.txt"

# Get all uppercase letters A-Z
alphabet = string.ascii_uppercase

with open(output_file, "w", encoding="utf-8") as f:
    for i in range(0, len(alphabet), letters_per_line):
        # Slice the alphabet into chunks
        line = alphabet[i:i+letters_per_line]
        f.write(line + "\n")

print(f"File '{output_file}' created successfully!")
