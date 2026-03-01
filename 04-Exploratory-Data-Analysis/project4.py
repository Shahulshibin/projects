import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("week 4/weather.csv")
print("-----Initial Data-----")
print(df.head())
print(df.info())

# data cleaning
print("\n Missing values:")
print(df.isnull().sum)

df['AvgTemp'].fillna(df["AvgTemp"].mean(), inplace= True)
df['Humidity'].fillna(df['Humidity'].mean(), inplace=True)
df['Rainfall'].fillna(df['Rainfall'].mean(), inplace=True)

print("\nCleaned Data:")
print(df)
print("\nBasic Statistics:")
print(df.describe())

# line chart

plt.figure(figsize=(10,5))
plt.plot(df['Month'], df['AvgTemp'], marker='o')
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(10,5))
plt.bar(df['Month'], df['Rainfall'])
plt.title("Monthly Rainfall (mm)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df['Month'], df['Humidity'], marker='o', linestyle='--')
plt.title("Monthly Humidity Levels")
plt.xlabel("Month")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.show()


print("\n WEATHER INSIGHTS:")

hottest = df.loc[df['AvgTemp'].idxmax(), 'Month']
print(f"- Hottest Month: {hottest}")

coldest = df.loc[df['AvgTemp'].idxmin(), 'Month']
print(f"- Coldest Month: {coldest}")

rainiest = df.loc[df['Rainfall'].idxmax(), 'Month']
print(f"- Rainiest Month: {rainiest}")

dry = df.loc[df['Rainfall'].idxmin(), 'Month']
print(f"- Driest Month: {dry}")

print("\nAverage humidity across the year:", round(df['Humidity'].mean(), 2))
