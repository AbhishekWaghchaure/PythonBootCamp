import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
data = pd.read_csv("../DataAnalysis/googleplaystore.csv")
print(data)
print(data.head())
print(data.columns)
print(data['App'].head(5))
#check null values
print(data.isnull().sum())

# 1st method to drop null features
drop = data.dropna()
print(drop)
print(drop.isnull().sum())
print(data.keys())
print(data['Price'])
print(data)

#second method to fill any random value in place of null
#we can use data.fillna() method
