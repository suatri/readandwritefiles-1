import pandas as pd

df = pd.read_csv('customers.csv')

country = df['Country']
FName = df['FirstName']

customer_name_and_country = pd.concat([FName, country], axis=1)

print(customer_name_and_country)

df = pd.DataFrame(customer_name_and_country)

df.to_csv("customer_country.csv", index=False)
