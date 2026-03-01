import pandas as pd
df = pd.read_csv(r"C:\Users\USER\Documents\Internsip\week 3\sales.csv")
print(df.head())

df["total"] = df["quantity"] * df["price"]
print(df)

total_sales = df["total"].sum()
print("Total Sales =", total_sales)

best_selling_product = df.groupby("product")["quantity"].sum().idxmax()
best_product_revenuce = df.groupby("product")["total"].sum().max()
print("Best Selling Product =", best_selling_product)
print("Best Product Revenue =", best_product_revenuce)

report = pd.DataFrame({
    'Metric': ['Total Sales', 'Best Selling Product', 'Best Product Revenue'],
    'Value': [total_sales, best_selling_product, best_product_revenuce]
})
print(report)