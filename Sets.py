#sets are lists which does not allow duplicates and unordered -->muttable {}
#List allows duplicates ---> muttable []
#Tuples are also list which does not allow mutation ----> immutable ()

#no indexing in sets

marks = {95, 98, 97, 97, 97}

for score in marks:
    print(score)

i = 0
while i <= len(marks):
    print(marks[i])
    i += 1

