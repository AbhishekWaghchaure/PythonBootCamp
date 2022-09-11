students = ["ram", "shyam",
            "kishan", "radha", "radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)

print(" ")

for student in students:
    if student == "shyam":
        continue;
    print(student)

i=0
while i < len(students):
    if students == "radha":
        break;
    print(students[i])
    i += 1