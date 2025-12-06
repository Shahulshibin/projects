# bar chart sales by product category

import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing','Groceries','toys']
sales = [50000,30000,20000,15000]
plt.bar(categories, sales, color=['blue', 'green', 'orange', 'red'])
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales in Rs:')
plt.show()

    #    MONTHLY TEMPATURE VARIATION
    
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temp = [20, 22, 27, 30, 35, 33]

plt.plot(months, temp, marker='o')
plt.title("Monthly Temperature Change")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()


    #    Expense Distribution
    
import matplotlib.pyplot as plt

labels = ['Rent', 'Food', 'Travel', 'Shopping', 'Savings']
expenses = [40, 20, 10, 15, 15]

plt.pie(expenses, labels=labels, autopct='%1.1f%%')
plt.title("Monthly Expense Distribution")
plt.show()


# Combine data loading, cleaning, analysis and visualization

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df.dropna(inplace=True)

# Example chart
plt.bar(df['Product'], df['Sales'])
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
    