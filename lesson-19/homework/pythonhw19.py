# Homework Assignment 1: Analyzing Sales Data
import pandas as pd

# Load data
sales = pd.read_csv(r"C:\Users\user\OneDrive\Documents\Python\Lesson-19\sales_data.csv")

# Task 1: Aggregate statistics by Category
result1 = sales.groupby('Category').agg(
    total_quantity=('Quantity', 'sum'),
    avg_price_per_unit=('Price', 'mean'),
    max_quantity_single_transaction=('Quantity', 'max')
).reset_index()

# Task 2: Top-selling product in each category (by total quantity)
# First, sum quantity by Product AND Category
prod_sales = sales.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
# Then, pick the product with the max sum in each category
result2 = prod_sales.loc[prod_sales.groupby('Category')['Quantity'].idxmax()]

# Task 3: Date with highest total sales (Total = Qty * Price)
sales['Total_Sales'] = sales['Quantity'] * sales['Price']
result3 = sales.loc[sales['Total_Sales'].idxmax(), 'Date']

print("--- Task 1 ---")
print(result1)
print("\n--- Task 2 ---")
print(result2)
print("\n--- Task 3 ---")
print(f"Date with highest sales: {result3}")



# Homework Assignment 2: Examining Customer Orders
import pandas as pd

customer_orders = pd.read_csv(r"C:\Users\user\OneDrive\Documents\Python\Lesson-19\customer_orders.csv")

# Task 1: Keep customers with 20 or more orders
result4 = (
    customer_orders.groupby("CustomerID")
    .size()
    .reset_index(name="order_count")
    .query("order_count >= 20")
)

# Task 2: Customers with average price > 120
result5 = (
    customer_orders.groupby("CustomerID")
    .agg(avg_price=("Price", "mean"))
    .reset_index()
    .query("avg_price > 120")
)

# Task 3: Total qty/price per product, filter out products with total qty < 5
result6 = (
    customer_orders.groupby("Product")
    .agg(total_qty=("Quantity", "sum"),
         total_price=("Price", "sum"))
    .reset_index()
    .query("total_qty >= 5") # Keeping those with 5 or more
)

print("\n--- Task 4 (Frequent Customers) ---")
print(result4)
print("\n--- Task 5 (High-value Average) ---")
print(result5)
print("\n--- Task 6 (Product Totals) ---")
print(result6)


# Homework Assignment 3: Population Salary Analysis
import sqlite3
import pandas as pd
import numpy as np

# Task 1: SQL Selection only
connection = sqlite3.connect(r"C:\Users\user\OneDrive\Documents\Python\Lesson-19\population.db")
population = pd.read_sql_query("SELECT salary, state FROM population", connection)
connection.close()

# Define Bins
interval = [0, 200_000, 400_000, 600_000, 800_000, 1_000_000, 1_200_000, 1_400_000, 1_600_000, 1_800_000, np.inf]
bands = ["till $200,000","$200,001 - $400,000", "$400,001 - $600,000", "$600,001 - $800,000",
         "$800,001 - $1,000,000", "$1,000,001 - $1,200,000", "$1,200,001 - $1,400,000", "$1,400,001 - $1,600,000",
         "$1,600,001 - $1,800,000", "$1,800,001 and over"]

population["Salary Band"] = pd.cut(population["salary"], bins=interval, labels=bands)

def calc_measures(data, group_col):
    # Group and aggregate
    stats = data.groupby(group_col)["salary"].agg(["mean", "median", "count"]).reset_index()
    
    # Calculate percentage based on the total population of the 'data' passed
    total_count = len(data)
    stats["percentage"] = (stats["count"] / total_count) * 100
    
    # Rename for clarity
    return stats.rename(columns={
        "mean": "Average Salary",
        "median": "Median Salary",
        "count": "Population Count",
        "percentage": "% of Population"
    })

# Task 2: Overall measures per Salary Band
result7 = calc_measures(population, "Salary Band")

# Task 3: Measures per State
result8 = calc_measures(population, "state")

print("\n--- Salary Band Analysis ---")
print(result7)
print("\n--- State Analysis ---")
print(result8)
