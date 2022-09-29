import pandas as pd
data = pd.read_csv("Automobile_data.csv")
print(data)
print(data.head())
print(data['engine-location'])
print(type(data['engine-location']))
print(data.columns)
print(type(data.columns))
for i in data.columns :
    print(i)