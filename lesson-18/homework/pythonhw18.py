import pandas as pd

# =======================
# Homework 2
# =======================

stackoverflow = pd.read_csv(r"C:\Users\user\OneDrive\Documents\Python\Lesson-18\stackoverflow_qa.csv")

# Ensure creationdate is datetime
stackoverflow["creationdate"] = pd.to_datetime(stackoverflow["creationdate"])

# 1. Find all questions that were created before 2014
result_1 = stackoverflow[stackoverflow["creationdate"] < "2014-01-01"]

# 2. Find all questions with a score more than 50
result_2 = stackoverflow[stackoverflow["score"] > 50]

# 3. Find all questions with a score between 50 and 100
result_3 = stackoverflow[stackoverflow["score"].between(50, 100)]

# 4. Find all questions answered by Scott Boston
result_4 = stackoverflow[stackoverflow["ans_name"] == "Scott Boston"]

# 5. Find all questions answered by the following 5 users
result_5 = stackoverflow[
    stackoverflow["ans_name"].isin(
        ["Demitri", "Mike Pennington", "unutbu", "DSM", "Jim"]
    )
]

# 6. Find all questions that were created between March 2014 and October 2014,
#    answered by Unutbu, and have a score less than 5
result_6 = stackoverflow[
    stackoverflow["creationdate"].between("2014-03-01", "2014-10-31")
    & (stackoverflow["ans_name"] == "unutbu")
    & (stackoverflow["score"] < 5)
]

# 7. Find all questions that have a score between 5 and 10 OR have a view count greater than 10,000
result_7 = stackoverflow[
    (stackoverflow["score"].between(5, 10))
    | (stackoverflow["viewcount"] > 10000)
]

# 8. Find all questions that are not answered by Scott Boston
result_8 = stackoverflow[stackoverflow["ans_name"] != "Scott Boston"]


# =======================
# Homework 3
# =======================

titanic = pd.read_csv(r"C:\Users\user\OneDrive\Documents\Python\Lesson-18\titanic.csv")

# 1. Select Female Passengers in Class 1 with Ages between 20 and 30
result_9 = titanic[
    (titanic["Sex"] == "female")
    & (titanic["Pclass"] == 1)
    & (titanic["Age"].between(20, 30))
]

# 2. Filter Passengers Who Paid More than $100
result_10 = titanic[titanic["Fare"] > 100]

# 3. Select Passengers Who Survived and Were Alone
result_11 = titanic[
    (titanic["Survived"] == 1)
    & (titanic["SibSp"] == 0)
    & (titanic["Parch"] == 0)
]

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50
result_12 = titanic[
    (titanic["Embarked"] == "C")
    & (titanic["Fare"] > 50)
]

# 5. Select Passengers with Siblings or Spouses AND Parents or Children
result_13 = titanic[
    (titanic["SibSp"] > 0)
    & (titanic["Parch"] > 0)
]

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive
result_14 = titanic[
    (titanic["Age"] <= 15)
    & (titanic["Survived"] == 0)
]

# 7. Select Passengers with Cabins and Fare Greater Than $200
result_15 = titanic[
    titanic["Cabin"].notna()
    & (titanic["Fare"] > 200)
]

# 8. Filter Passengers with Odd-Numbered Passenger IDs
result_16 = titanic[titanic["PassengerId"] % 2 == 1]

# 9. Select Passengers with Unique Ticket Numbers
ticket_counts = titanic["Ticket"].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
result_17 = titanic[titanic["Ticket"].isin(unique_tickets)]

# 10. Select Passengers with 'Miss' in Their Name and Were in Class 1
result_18 = titanic[
    titanic["Name"].str.contains("Miss", na=False)
    & (titanic["Pclass"] == 1)
]

print("\nResult 1:\n", result_1)
print("\nResult 2:\n", result_2)
print("\nResult 3:\n", result_3)
print("\nResult 4:\n", result_4)
print("\nResult 5:\n", result_5)
print("\nResult 6:\n", result_6)
print("\nResult 7:\n", result_7)
print("\nResult 8:\n", result_8)

print("\nResult 9:\n", result_9)
print("\nResult 10:\n", result_10)
print("\nResult 11:\n", result_11)
print("\nResult 12:\n", result_12)
print("\nResult 13:\n", result_13)
print("\nResult 14:\n", result_14)
print("\nResult 15:\n", result_15)
print("\nResult 16:\n", result_16)
print("\nResult 17:\n", result_17)
print("\nResult 18:\n", result_18)
