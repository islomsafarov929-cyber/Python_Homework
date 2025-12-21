import pandas as pd
import numpy as np

# --- Homework Assignment 1 ---
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 35, 40], 
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
} 
df = pd.DataFrame(data)

# Task 1: Rename columns
df = df.rename(columns={"First Name": "first_name", "Age": "age"})

# Task 2: Print first 3 rows
print("--- HW1 Task 2: First 3 Rows ---")
print(df.head(3))

# Task 3: Mean age
print(f"\nMean age: {df.age.mean()}")

# Task 4: Select specific columns
print("\n--- HW1 Task 4: Name and City ---")
print(df[["first_name", "City"]])

# Task 5: Add Salary column
df["Salary"] = np.round(np.random.uniform(4500, 10000, size=len(df)), 2)
print("\n--- HW1 Task 5: Data with Salary ---")
print(df)

# Task 6: Summary statistics
print("\n--- HW1 Task 6: Describe ---")
print(df.describe())


# --- Homework Assignment 2 ---
dicthw2 = {
    "Month": ["Jan", "Feb", "Mar", "Apr"], 
    "Sales": [5000, 6000, 7500, 8000], 
    "Expenses": [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(dicthw2)

print("\n--- HW2 Tasks: Max, Min, Mean ---")
print(f"Max Sales: {sales_and_expenses.Sales.max()} | Max Expenses: {sales_and_expenses.Expenses.max()}")
print(f"Min Sales: {sales_and_expenses.Sales.min()} | Min Expenses: {sales_and_expenses.Expenses.min()}")
print(f"Avg Sales: {sales_and_expenses.Sales.mean()} | Avg Expenses: {sales_and_expenses.Expenses.mean()}")


# --- Homework Assignment 3 ---
dicthw3 = {
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"], 
    "January": [1200, 200, 300, 150], 
    "February": [1300, 220, 320, 160], 
    "March": [1400, 240, 330, 170], 
    "April": [1500, 250, 350, 180]
}
expenses = pd.DataFrame(dicthw3).set_index('Category')

# We can use axis=1 to calculate statistics across the months (columns) for each category (row)
print("\n--- HW3 Tasks: Category Statistics (Across Months) ---")
category_stats = pd.DataFrame({
    "Max": expenses.max(axis=1),
    "Min": expenses.min(axis=1),
    "Average": expenses.mean(axis=1)
})
print(category_stats)
