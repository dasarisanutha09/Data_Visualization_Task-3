# Import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load dataset

df = pd.read_excel("sales_data.xlsx")


print("Dataset Loaded Successfully")

print(df.head())



# --------------------------
# GRAPH 1
# Sales by Category
# --------------------------


plt.figure(figsize=(8,5))


sns.barplot(
    x="Category",
    y="Sales",
    data=df
)


plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Sales")


plt.show()



# --------------------------
# GRAPH 2
# Profit Analysis
# --------------------------


plt.figure(figsize=(8,5))


sns.barplot(
    x="Product",
    y="Profit",
    data=df
)


plt.title("Profit by Product")

plt.xlabel("Product")

plt.ylabel("Profit")

plt.xticks(rotation=45)


plt.show()



# --------------------------
# GRAPH 3
# Region Wise Sales
# --------------------------


plt.figure(figsize=(8,5))


sns.countplot(
    x="Region",
    data=df
)


plt.title("Sales Distribution by Region")


plt.show()



# --------------------------
# GRAPH 4
# Sales Distribution
# --------------------------


plt.figure(figsize=(8,5))


sns.histplot(
    df["Sales"],
    bins=10
)


plt.title("Sales Distribution")


plt.xlabel("Sales")


plt.show()



print("Visualization Completed Successfully")