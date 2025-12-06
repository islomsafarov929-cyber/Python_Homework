# Task 1.write a Python script that reads the students.jon JSON file and prints details of each student.
import json

# File path
FILE_PATH = r"C:\Users\user\OneDrive\Documents\Python\Lesson-14\students.json"

with open(FILE_PATH, "r") as file:
    data = json.load(file)

for student in data.get("students", []):
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")
    print(f"Subjects: {', '.join(student['subjects'])}")
    print("-" * 40)


# Task 2.Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests
from bs4 import BeautifulSoup as bs

# ===================================================================
# NOTE:
# Task 2 originally required fetching weather data using OpenWeatherMap API.
# However, when this homework was created (1-2 years ago), the teacher suggested
# using https://obhavo.uz for educational purposes. 
# 
# Currently:
# - OpenWeatherMap may require API keys or may have changed their API rules.
# - Web scraping obhavo.uz is only for educational/homework purposes.
# 
# So, in this code, we scrape obhavo.uz as permitted for this homework. 
# This is not recommended for production use or public scripts.
# ===================================================================

url = "https://obhavo.uz/tashkent"
response = requests.get(url)
soup = bs(response.text, "html.parser")

block = soup.find("div", class_="padd-block")

# Extracting date, city, and weather condition
date = block.find("div", class_="current-day").text.strip()
location = block.find("h2").text.strip()
condition = block.find("div", class_="current-forecast-desc").text.strip()

# Extracting temperatures (high and low)
spans = [s.get_text(strip=True) for s in block.find_all("span") if s.get_text(strip=True)]
high_temp = spans[0]
low_temp = spans[1]

# Extracting humidity and wind
col1 = block.find("div", class_="col-1")
p_values = [p.get_text(strip=True) for p in col1.find_all("p")]
humidity, wind, *_ = p_values

# Extracting sunrise and sunset times
col2 = block.find("div", class_="col-2")
p2_values = [p.get_text(strip=True) for p in col2.find_all("p")]
*_, sun_rise, sun_set = p2_values

print("="*40)
print(f" Sana: {date}")
print(f" Joy: {location}")
print("-"*40)
print(f" Harorat: {low_temp} ... {high_temp}")
print(f" Namlik: {humidity}")
print(f" Shamol: {wind}")
print(f" {sun_rise}")
print(f" {sun_set}")
print(f" Ob-havo: {condition}")
print("="*40)


# Task 3.Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        save_books([])
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)


def validate_year(year):
    return year.isdigit() and 0 < int(year) <= 2030


def add_book():
    books = load_books()

    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter year: ").strip()

    if not title or not author or not validate_year(year):
        print("❌ Invalid input!")
        return

    books.append({"title": title, "author": author, "year": int(year)})
    save_books(books)
    print("✓ Book added.\n")


def update_book():
    books = load_books()
    title = input("Enter book title to update: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            new_title = input("New title (leave empty to keep): ").strip()
            new_author = input("New author (leave empty to keep): ").strip()
            new_year = input("New year (leave empty to keep): ").strip()

            if new_year and not validate_year(new_year):
                print("❌ Invalid year!")
                return

            book["title"] = new_title or book["title"]
            book["author"] = new_author or book["author"]
            book["year"] = int(new_year) if new_year else book["year"]

            save_books(books)
            print("✓ Book updated.\n")
            return

    print("❌ Book not found.\n")


def delete_book():
    books = load_books()
    title = input("Enter book title to delete: ").strip()

    updated = [b for b in books if b["title"].lower() != title.lower()]

    if len(updated) == len(books):
        print("❌ Book not found.\n")
        return

    save_books(updated)
    print("✓ Book deleted.\n")


def main():
    while True:
        print("""
===== BOOK MANAGER =====
1. Add a book
2. Update a book
3. Delete a book
4. Exit
""")
        choice = input("Choose (1-4): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice!\n")


if __name__ == "__main__":
    main()



# Task 4.Create a program that asks users for a movie genre and recommends a random movie from that genre.

# I asked the owners of site to give API key, then i used it

import requests
import random
import os

API_KEY = os.getenv("OMDB_KEY")  # ❗ tavsiya etilgan usul

if not API_KEY:
    API_KEY = "d7ec2d16"  # Agar .env bo'lmasa fallback


def search_movies(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"
    data = requests.get(url).json()

    if data.get("Response") == "False":
        return None

    return data.get("Search", [])


def movie_details(movie_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={movie_id}"
    return requests.get(url).json()


def recommend_movie():
    genre = input("Enter genre (Action, Comedy, Drama...): ")

    movies = search_movies(genre)
    if not movies:
        print("❌ No movies found for this genre.")
        return

    movie = random.choice(movies)
    details = movie_details(movie["imdbID"])

    print("\n🎬 Recommended Movie")
    print("="*40)
    print("Title:", details.get("Title"))
    print("Year:", details.get("Year"))
    print("Genre:", details.get("Genre"))
    print("Rating:", details.get("imdbRating"))
    print("Plot:", details.get("Plot"))
    print("="*40)


recommend_movie()
