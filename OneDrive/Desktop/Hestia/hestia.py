import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("hello world")
# Load wildfire dataset (Replace with actual dataset)
data_path = "Alberta06-24.csv"  # Update with actual dataset path
df = pd.read_csv(data_path)
df.columns = df.columns.str.lower()


# Display basic dataset info
print("Dataset Preview:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Simple visualization: Wildfire occurrences over time
plt.figure(figsize=(10, 5))
sns.histplot(df['year'], bins=20, kde=True)
plt.title("Wildfire Occurrences by Year")
plt.xlabel("Year")
plt.ylabel("Number of Wildfires")
plt.show()