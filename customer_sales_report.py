import pandas as pd
import csv

df = pd.read_csv("sales.csv")

print(df.head())

"""
# Long version
Customer_ID = df["CustomerID"]
print(Customer_ID.head())

SubT = df["SubTotal"]
TaxAmt = df["TaxAmt"]
Freight = df["Freight"]


Total = SubT+TaxAmt+Freight
print(Total.head())

CuSaRe = pd.concat([Customer_ID, Total], axis=1)
print(CuSaRe)
"""

# Short version

output = print(pd.concat([df["CustomerID"], df["SubTotal"] +
                          df["TaxAmt"]+df["Freight"]], axis=1))

df = pd.DataFrame(output)

df.to_csv("salesreport.csv", index=False)
