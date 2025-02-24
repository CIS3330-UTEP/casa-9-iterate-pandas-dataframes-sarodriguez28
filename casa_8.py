# Using iterrrows
import pandas as pd

data = {'Item': ['Apple', 'Banana', 'Orange'], 'Quantity': [10, 20, 30], 'Price': [0.5, 0.3, 0.7]}
df = pd.DataFrame(data)

#Iterating over rows
for index, row in df.iterrows():
    total_sales = row['Quantity'] * row['Price']
    print(f"{row['Item']} Total Sales: ${total_sales}")

# Using apply()
data = {'Item': ['Apple', 'Banana', 'Orange'], 'Quantity': [10, 20, 30], 'Price': [0.5, 0.3, 0.7]}
df = pd.DataFrame(data)

#Defining a function to calculate total sales for each row
def calculate_total_sales(row):
    return f"{row['Item']} Total Sales: ${row['Quantity'] * row['Price']}"

#Applying the function row-wise
result = df.apply(calculate_total_sales, axis=1)
for res in result:
    print(res)
