# Task 1.List containing five different fruits and print the third fruit.
# 5 ta mevani jamlagan ro'yxat yaratish, va 3 chisini chiqarish.
# Solution 1. Just creating a list and printing thisd.
fruit_list = ["Apple", "Banana", "Grape", "Pear", "Orange"]

print("The third fruit:", fruit_list[2])

# Solution 2. We can ask user to enter names of fruits and printing third.
fruits = input("Enter 5 fruit names, split them with comma:").strip().strip(",")

fruit_list = [str(fruit) for fruit in fruits.split(",")]

print("The third fruit:", fruit_list[2])


# Task 2.Two lists of numbers and concatenate them into a single list.
# 2 at ro'yxatni bittaga qo'shish.
my_list = [1, 2, 3, 6, 9, 15,]

new_list = [10, 46, 78, 90, 88]

my_list.extend(new_list)

print("Concatenation of two lists:", my_list)

# Task 3.List of numbers, extract the first, middle, and last elements and store them in a new list.
# Sonlar ro'yxati, undan birinchi, o'rtadagi va oxirgi elementlarni ojartib ularni boshqa ro'yxatga olish.
# solution 1. Basic and unreliable way.
numbers = input("Enter list of numbers, split them with comma:").strip().strip(",")

number_list = [int(num) for num in numbers.split(",")]

first, *middle, last = number_list

print("First:",first)

middle = middle[len(middle)//2]

print("Middle:",middle)
print("Last:", last)

# Solution 2. Reliable and bit harder way.
numbers = input("Enter list of numbers, split them with comma:").strip().strip(",")
number_list = [int(num) for num in numbers.split(",")]

if len(number_list) < 3:
    print("Listda kamida 3 ta element bo'lishi kerak.")
else:
    first, *middle, last = number_list
    print("First:", first)
    middle_value = middle[len(middle) // 2]
    print("Middle:", middle_value)
    print("Last:", last)

# Task 4.List of your five favorite movies and convert it into a tuple.
# 5 ta yoqtirgan filmlar ro'yxatini (tuple)ga o'tlkazish
movies = input("Enter your 5 favorite movies' name, splitted with comma:").strip().strip(",")
# The input() function is easier and convenient to me than entering tha names one-by-one.

movie_list = [str(mov) for mov in movies.split(",")]

tupled_movie_list = tuple(movie_list)

print("Movie names:", tupled_movie_list)

# Task 5.List of cities, check if "Paris" is in the list and print the result.
# Shaharlar ro'yxatida "Paris" bor yoki yo'qligini tekshirish.
city_list = ["Paris", "London", "Toshkent", "Samarqand", "Washington", "Istanbul", "Anqara", "Dushanbe"]

city = input("Enter a city name:").strip().capitalize()
# I asked user to enter a city name, like searching it.

if city in city_list:
    print(f"{city} ro'yxatda mavjud.")
else:
    print(f"{city} ro'yxatda mavjud emas.")

# Task 6.List of numbers and duplicate it without using loops.
# Sonlar ro'yxatini halqa ishlatmasdan nusxalash.
my_list = [3,7,3,9,1,8]

new_my_list = my_list.copy()

print("Old list:",my_list)
print("Duplecated list:",new_my_list)

# Task 7.List of numbers, swap the first and last elements.
# Sonlar ro'yxatidagi birinchi va oxirgi element joyini almashtirish.
number_list = [12,23,45,56,67,78]

number_list[0], number_list[-1] = number_list[-1], number_list[0]

print("First and last elements swapped from the list:",number_list)

# Task 8.Tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
# Sonlar (tuple)sidan 3 dan 7 gacha o'rindagi elementlarni kesib olish.
my_tuple = (1,2,3,4,5,6,7,8,9,10)

sliced_tuple = my_tuple[3:8]

print("Sliced part of tuple:", sliced_tuple)

# Task 9.List of colors and count how many times "blue" appears in the list.
# Ranglar ro'yxatida necha marta blue qayd etilganini ko'rish.
# Solution 1. Counts blue from list which asked in the task.
list_of_colors = ["blue", "red", "black", "white", "yellow", "green", "blue", "black", "green", "brown", "porple"]

total_color = list_of_colors.count("blue")

print("Total of blue in the list:" ,total_color)

# Solution 2.Counts color from list which user entered, like search.
list_of_colors = ["blue", "red", "black", "white", "yellow", "green", "blue", "black", "green", "brown", "porple"]

color = input("Enter name of a color:").strip().lower()

total_color = list_of_colors.count(color)

print(f"Total of {color} in the list:" ,total_color)

# Task 10.Tuple of animals, find the index of "lion".
# Hayvonlar (tuple)sidan, element joylashuvini topish.
# Solution 1. Finds the index of lion from tuple which asked in the task.
animals_tuple = ("snake", "tiger", "bear", "lion", "hippopatamus", "alligator")

ind_of_animal = animals_tuple.index("lion")

print("The index of lion in the list:", ind_of_animal)

# Solution 2.Finds the index of animal from tuple which user entered, like search.
animals_tuple = ("snake", "tiger", "bear", "lion", "hippopatamus", "alligator")

animal = input("Enter  name of animal:").strip().lower()

if animal in animals_tuple:
    print(f"The index of {animal} in the list:", animals_tuple.index(animal))
else:
    print(f"{animal} not found in the tuple.")
 
# Task 11.Two tuples of numbers and merge them into a single tuple.
# 2 ta (tuple)ni qo'shish.
my_tuple = (10,20,30,40,50)
your_tuple = (60,70,80,90,100)

my_tuple += your_tuple
# I used augmented assignment to copy elements from tuple to tuple.

print("Merged two tuples:",my_tuple)

# Task 12.List and a tuple, find and print their lengths.
# Ro'yxat va (tuple)ning uzinligi.
elements = input("Enter anything for list, split them with comma:").strip().strip(",")

my_list = [str(elem) for elem in elements.split(",")]

print("Length of list:", len(my_list))

elements2 = input("Enter anything for tuple, split them with comma:").strip().strip(",")

my_tuple =tuple(str(elem2) for elem2 in elements2.split(","))

print("Length of tuple:", len(my_tuple))

# Task 13.Tuple of five numbers and convert it into a list.
# 5 ta sonni jamlagan (tuple)ni ro'yxayga o'tkazish.
numbers_tuple = (40,45,50,55,60)

number_list = list(numbers_tuple)

print("Tuple converted into list:", number_list)

# Task 14.Tuple of numbers, find and print the maximum and minimum values.
# Sonlar (tuple)sidan eng katta va eng kichik sonni topish.
numbers = input("Enter numbers, split them with comma:").strip().strip(",")

numbers_tuple = tuple(int(n) for n in numbers.split(","))

print("Highest number in the tuple:" ,max(numbers_tuple))
print("Lowest number in the tuple:", min(numbers_tuple))

# Task 15.Tuple of words and print it in reverse order.
# So'zlar (tuple)sini teskari qilish.
word_tuple = ("Hello", "Pen", "Smartphone", "Ball", "shelf")

reversed_tuple = tuple(reversed(word_tuple))

print("Reversed tuple:", reversed_tuple)

