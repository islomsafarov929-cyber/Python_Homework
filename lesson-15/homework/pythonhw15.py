# Task 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field

import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

query = "CREATE TABLE Roster (Name VARCHAR(50), Species VARCHAR(50), Age INT)"

cursor.execute(query)

connection.commit()
connection.close()


# Task 2. Populate your new table with the following values:

# Name	         | Species	|   Age
# Benjamin Sisko |  Human	|    40
# Jadzia Dax	 |  Trill	|   300
# Kira Nerys	 |  Bajoran	|    29

import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

query1 = "INSERT INTO Roster VALUES ('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)"

cursor.execute(query1)

connection.commit()
connection.close()


# Task 3. Update the Name of Jadzia Dax to be Ezri Dax

import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

query2 = "UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'"

cursor.execute(query2)

connection.commit()
connection.close()


# Task 4. Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

query2 = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran' "

result = cursor.execute(query2)

print(result.fetchall())

connection.close()
