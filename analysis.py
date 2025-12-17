import pandas as pd

df = pd.read_csv("C:/Users/radha/OneDrive/Desktop/MarketProject/data.csv.csv")

region_orders = df["Region"].value_counts()

print(region_orders)