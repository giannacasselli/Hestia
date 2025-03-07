import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#print("hello world")
#load in data set 
data_path = "Alberta06-24.csv" 
#read and convert to lowercase (pandas is case sensitive)
df = pd.read_csv(data_path)
df.columns = df.columns.str.lower()

# #check missing values
# print("\nMissing Values:")
# print(df.isnull().sum())

# #get statistical analysis
# print("\nSummary Statistics:")
# print(df.describe())

# Remove missing values for relevant columns
df = df.dropna(subset=["relative_humidity", "wind_speed", "wind_direction", "current_size"])

#Scatter Plot: Humidity vs. Fire Size
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["relative_humidity"], y=df["current_size"], alpha=0.5)
plt.xlabel("Relative Humidity (%)")
plt.ylabel("Fire Size (Hectares)")
plt.title("Effect of Humidity on Fire Size")
plt.show()

##Scatter Plot: Wind Speed vs. Fire Size
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["wind_speed"], y=df["current_size"], alpha=0.5, color="red")
plt.xlabel("Wind Speed (km/h)")
plt.ylabel("Fire Size (Hectares)")
plt.title("Effect of Wind Speed on Fire Size")
plt.show()

#Box Plot: Wind Direction vs. Fire Size
plt.figure(figsize=(10,5))
sns.boxplot(x=df["wind_direction"], y=df["current_size"])
plt.xlabel("Wind Direction (Degrees)")
plt.ylabel("Fire Size (Hectares)")
plt.title("Wind Direction vs. Fire Size")
plt.xticks(rotation=90)
plt.show()

#Correlation Heatmap
plt.figure(figsize=(6,5))
corr_matrix = df[["relative_humidity", "wind_speed", "current_size"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Weather Factors")
plt.show()

# #wildfires over time plot
# plt.figure(figsize=(10, 5))
# sns.histplot(df['year'], bins=20, kde=True)
# plt.title("Wildfire Occurrences by Year")
# plt.xlabel("Year")
# plt.ylabel("Number of Wildfires")
# plt.show()