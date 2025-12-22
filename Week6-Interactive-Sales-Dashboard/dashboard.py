import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

df = pd.read_csv("sales_data.csv")

# Convert Date column (important for line chart)
df["Date"] = pd.to_datetime(df["Date"])

df.head()
print(df.info())
print(df.isnull().sum())

sns.set_theme(style="whitegrid")

plt.figure(figsize=(6,4))
sns.boxplot(x="Region", y="Price", data=df)
plt.title("Price Distribution by Region")
plt.show()
plt.figure(figsize=(6,4))
sns.violinplot(x="Region", y="Total_Sales", data=df)
plt.title("Sales Distribution by Region")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(
    df[["Price", "Quantity", "Total_Sales"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x="Region", y="Total_Sales", data=df)
plt.title("Total Sales by Region")
plt.show()

plt.figure(figsize=(6,4))
sns.lineplot(x="Date", y="Total_Sales", data=df)
plt.title("Sales Trend Over Time")
plt.show()

fig = px.bar(
    df,
    x="Product",
    y="Total_Sales",
    color="Region",
    title="Interactive Product Sales Dashboard",
    hover_data=["Price", "Quantity", "Customer_ID"]
)

fig.show()

fig, axes = plt.subplots(2, 2, figsize=(10,8))

sns.boxplot(x="Region", y="Price", data=df, ax=axes[0,0])
axes[0,0].set_title("Price Distribution")

sns.violinplot(x="Region", y="Total_Sales", data=df, ax=axes[0,1])
axes[0,1].set_title("Sales Distribution")

sns.barplot(x="Region", y="Total_Sales", data=df, ax=axes[1,0])
axes[1,0].set_title("Sales by Region")

sns.lineplot(x="Date", y="Total_Sales", data=df, ax=axes[1,1])
axes[1,1].set_title("Sales Trend")

plt.tight_layout()
plt.show()

