import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")

# Using iterrows()
print("Using iterrows(): ")
for index, row in df.iterrows():
    print(index, row.to_dict())

#define print row
def print_row(row):
    print(row.name, row.to_dict())

# Using apply()
print("\nUsing apply(): ")
df.apply(print_row, axis=1)