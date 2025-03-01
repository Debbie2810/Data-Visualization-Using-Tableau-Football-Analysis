import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/football_players_data.csv")

# Display first few rows
df.head()

# Data Cleaning & Preprocessing
# Handling missing values
df.fillna(method='ffill', inplace=True)

# Convert data types where necessary
df['Age'] = df['Age'].astype(int)
df['Overall'] = df['Overall'].astype(int)
df['Value'] = df['Value'].replace({'\u20ac': '', 'M': 'e6', 'K': 'e3'}, regex=True).astype(float)

# Feature Engineering: Categorizing age groups
df['Age Group'] = pd.cut(df['Age'], bins=[15, 20, 25, 30, 35, 40], labels=['15-20', '21-25', '26-30', '31-35', '36-40'])

# Exploratory Data Analysis
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='blue')
plt.title("Distribution of Players' Ages")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=df['Age Group'].value_counts().index, y=df['Age Group'].value_counts().values, palette='viridis')
plt.title("Players Count by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Players")
plt.show()

# Save cleaned data
df.to_csv("data/processed_data.csv", index=False)

print("Data Cleaning and EDA Completed and Saved!")
