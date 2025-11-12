# Dictionary tasks.

# Task 1.Write a Python script to sort (ascending and descending) a dictionary by value.

sample_dict = {
    "FirstName": "Tom",
    "LastName": "Holland",
    "NickName": "Spider-Man",
    "Job": "Actor",
    "Interest": "Comics"
}

# Ascending order by value
sorted_dict_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary by ascending value:", sorted_dict_asc)

# Descending order by value
sorted_dict_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted dictionary by descending value:", sorted_dict_desc)

# Task 2.Write a Python script to add a key to a dictionary.

number_dict = {0: 10, 1: 20}

# I used update() method to add another key to dictionary.

number_dict.update([(2, 30)])

print("Key added:", number_dict)



# Task 3.Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# I used union() method's sign ( | ) to concatenate 3 dictionaries.

dic4 = dic1 | dic2 | dic3

print("Three dicitonaries concatenated:", dic4)


# Task 4.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

square_dict = {}
for n in range(1, 6):
    square_dict[n] = n * n

# I created an empty dictionary and add keys and values with using loop.

print("The numbers between 1 and 5 have risen to the square",square_dict)


# Task 5.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

square_dict = {}
for n in range(1, 16):
    square_dict[n] = n * n

# Same thing as task 4

print("The numbers between 1 and 15 have risen to the square:",square_dict)



# Set tasks.

# Task 1.Write a Python program to create a set.

sample_set = {1, "hello", 2, "bye", "Thanks", 3}

# I created set named sample_set with adding only values into curly bracket

print("Set created:", sample_set)


# Task 2.Write a Python program to iterate over sets.

sample_set = {1, "hello", 2, "bye", "Thanks", 3}

# I used loop to iterate over the set values.
for val in sample_set:
    print("Set's value:", val)


# Task 3.Write a Python program to add member(s) to a set.

member_set = {"John", "Anna", "Tom", "Jack", "Hugo"}

# First i created set named member_set, then add another member to that set. 

member_set.add("Jhonny")

print("Member added to the set:", member_set)


# Task 4.Write a Python program to remove item(s) from a given set.

sample_set = {1, "hello", 2, "bye", "Thanks", 3}

# remove() to delete the value which needed. It returns KeyError if it can't find the value.

sample_set.remove("hello")
print("'hello' removed from the set.")

# pop() deletes first value in the set.

print(f"'{sample_set.pop()}' removed from the set.")

# discard() to delete the value which needed. It does'nt return any value even it can't find the velue.

sample_set.discard(3)
print("'3' removed from the set.")

# Final result.
print("The set we got after deleting:", sample_set)


# Task 5.Write a Python program to remove an item from a set if it is present in the set.

employee_set = {"Anna", "Tom", "Josh", "Hugo", "Dora", "John"}

element = input("Enter an employee name to delete it from the set:").strip().capitalize()

if element in employee_set:
    employee_set.discard(element)
    print(f"'{element}' removed from the set.")
else:
    print(f"'{element}' is not in the set.")

# At start i created set named employee_set, then ask from user any employee's name to remove from that set, 
# and check with if else the name which user gave is available in the set.
