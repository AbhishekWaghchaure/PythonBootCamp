import pandas as pd
data = pd.read_csv("googleplaystore.csv")
print(data)
print(data.head())
# print(data['engine-location'])
# print(type(data['engine-location']))
print(data.columns)
for i in data.columns :
    print(i)
print(type(data.columns))