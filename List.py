#Lists
marks = [20,45,34]
print(marks)

print(marks[-1])

print(marks[0:2])

print(marks[1:3])

for score in marks:
    print(score)
#append operations on lists

marks.append(99)
print(marks)

marks.insert(0, 99)
print(marks)

print(len(marks))
i=0
while i < len(marks):
    print(marks[i])
    i += 1
