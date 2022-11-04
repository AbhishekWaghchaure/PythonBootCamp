import pandas as pd

df = pd.read_csv("googleplaystore.csv")
print(df.head(5))
print(df['Category'])
print(df['Category'].unique())

for i in df['Category'].unique():
    print(i)
# total number of categories
print(len(df['Category'].unique()))

# total number of apps of category art and design
c = 0
for i in df['Category']:
    if i == 'ART_AND_DESIGN':
        c += 1
print("There are total of ", c, " art and design apps in db")

# ______________________________________________________________________
# exploring type feature
print(df['Type'].unique())

# finding number of paid applications
p = 0
for i in df['Type']:
    if i == 'Paid':
        p += 1
print("There are total ", p, "paid applications")

# finding number of free applications
f = 0
for i in df['Type']:
    if i == 'Free':
        f += 1
print("There are total ", f, "free applications")

print(p)
print(f)

# finding percentage of paid applications
print(int(p / (p + f) * 100), "Is the percentage of paid applications")

# finding percentage of free applications
print(int(f / (p + f) * 100), "Is the percentage of free applications")

# name all the content ratings

for i in df['Content Rating'].unique():
    print(i)
