# import pandas as pd

# df = pd.read_csv("file.csv")


# To see first 5 rows:print(df.head())
# To see last rows:print(df.tail())

# HOW MANY COLUMNS: print(df.shape)
# TO SEE ALL COLUMNS: print(df.columns)
# TO SEE DATATYPE OF EACH COLUMN: print(df.dtypes)
# TO SEE SUMMARY STATISTICS: print(df.describe())
# TO SEE FULL SUMMARY OR INFORMATION ABOUT DATAFRAME: print(df.info())


# int64 → whole numbers

# float64 → decimals

# object → text

# datetime64 → dates

# TO FIND NULL VALUES IN DATAFRAME : print(df.isnull().sum())

# TO DROP NULL VALUES FROM DATAFRAME: df.dropna(inplace=True)

# Fix missing values (fill):
# df['column_name'].fillna(value, inplace=True)

# Fill with constant value:
# df['column_name'].fillna(0, inplace=True)

# Convert wrong data types:
# df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

                #   SIMPLE staticmethod
                
#   ✔ Average
# df["marks"].mean()

# ✔ Maximum
# df["marks"].max()

# ✔ Minimum
# df["marks"].min()

# ✔ Sum
# df["sales"].sum()     
# ✔ Count
# df["marks"].count()         


import pandas as pd

df = pd.read_excel(r"C:\Users\USER\Documents\Internsip\week 3\sales.xlsx")
print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())

df.isnull().sum()
df.dropna(inplace=True)

# Calculations
total_quantity = df["QUANTITY"].sum()
average_price = df["PRICE"].mean()
highest_price = df["PRICE"].max()

print("Total Quantity Sold =", total_quantity)
print("Average Price =", average_price)
print("Highest Price =", highest_price)

