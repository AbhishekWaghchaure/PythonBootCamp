import pandas as py
data = py.read_csv("googleplaystore.csv")
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

#second method to fill any random value in place of null
#we can use data.fillna() method
