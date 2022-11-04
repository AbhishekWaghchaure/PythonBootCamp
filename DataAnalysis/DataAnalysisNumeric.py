import pandas as pd
df = pd.read_csv("googleplaystore.csv").dropna()
print(df.isnull().sum())
print(df['Rating'])

#finding average rating
print(float(str(int(sum(df['Rating']))/len(df['Rating']))[:4]))

#apps with particular rating
count = 0
for i in df['Rating']:
    if(i == 5.0):
        count += 1
print("There are ", count, "apps with rating 5 ")

count = 0
for i in df['Rating']:
    if(i >= 4.0 and i <= 4.5):
        count += 1
print("There are ", count, "apps with rating between 4 and 4.5")

print(df['Reviews'])
#finding average of reviews
s=0
for i in df['Reviews']:
    s += int(i)
print(int(s/len(df['Reviews'])))
