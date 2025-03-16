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

#Remove missing values for relevant columns
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

# Gather data of daily weather conditions in Alberta
# Wildfire data uses locations based in longitude and latitude
# Need to conver location weather data to long/lat coordinates and merge with wildfire csv
# All daily weather data is yearly to March 1st
# https://www.mapcustomizer.com/map/Hestia%20Daily%20Weather%20Probes 

# Fort McMurray A, Fort McMurray: Lat = 56.72667, Lon = -111.38083 - Data acquired for 2016 - 2025
# Rainbow Lake Auto, Rainbow Lake: Lat = 58.50444, Lon = -119.40028 - Data acquired for 2020 - 2025
# Shell Hamburg, Chinchaga Wildland Provincial Park: Lat = 57.15000, Lon = -119.56667 - Data acquired for 2016 - 2025
# Entrance Auto, Old Entrance: Lat = 53.36667, Lon = -117.71889 - Data acquired for 2016 - 2025
# Wabasca Auto, Wabasca: Lat = 55.96666, Lon = -113.85000 - Data acquired for 2016 - 2025
# Loon River Auto, Loon River Airport: Lat = 57.14200, Lon = 115.07533 - Data acquired for 2016 - 2025
# Lac La Biche Climate, Lac La Biche: Lat = 54.76690, Lon = -111.96861 - Data acquired for 2016 - 2025
# Hawk Hills Auto, Kemp River: Lat = 57.55000, Lon = -117.50000 - Data acquired 2020 - 2025
# Fort Vermillion, Fort Vermillion: Lat = 58.22500, Lon = -115.59100 - Data acquired for 2016 - 2025
# Cambrian Auto, La Butte Creek Wildlands: Lat = 59.52444, Lon = -111.46389 - Data acquired for 2019 - 2025
# Whitesands Auto, John D'Or Prairie Reserve: Lat = 58.51100, Lon = -115.12500 - Data acquired for 2016 - 2025
# Fort Macleod Auto, Fort Macleod: Lat = 49.71671, Lon = -113.41857 - Data acquired for 2016 - 2025
# Rocky Mountain House AUT, Rocky Mountain House: Lat = 52.36683, Lon = -114.91880 - Data acquired for 2016 - 2025
# Edson, Edson: Lat = 53.58345, Lon = -116.43559 - Data acquired for 2019 - 2025
# Economy Creek Auto, Grovedale: Lat = 55.02500, Lon = -118.86472 - Data acquired for 2018 - 2025
# Imperial Auto, Swan Hills: Lat = 54.71681, Lon = -115.40226 - Data acquired for 2016 - 2025
# Cleardale ADGM, Cleardale: Lat = 56.33450, Lon = -119.58616 - Data acquired for 2016 - 2025
# Edmonton Blatchford, Edmonton: Lat = 53.55014, Lon = -113.46871 - Data acquired for 2016 - 2025
# Jean Lake Auto, Jean Lake Airport: Lat = 57.45583, Lon = -113.09722 - Data acquired for 2020 - 2025
# Fort Chipewyan, Fort Chipewyan: Lat = 58.70870, Lon = -111.15500 - Data acquired for 2016 - 2025
# Vermilion AGDM, Vermilion: Lat = 53.35409, Lon = -110.85849 - Data acquired for 2016 - 2019
