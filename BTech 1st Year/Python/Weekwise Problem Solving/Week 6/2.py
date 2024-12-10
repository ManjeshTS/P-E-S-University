students = {
    "Rohan": 85,
    "Spoorthi": 90,
    "Aditi": 78,
    "Tanya": 92
}
max =0
for s,m in students.items():
    if max < m :
        max = m
        student = s
    
print("The student having Highest marks is ",s , "and the marks is ", max)

sum = 0
n=0
for i in students.values():
    sum = sum + i
    n += 1
    
print("The average marks is = ", sum /n)

students["Manjesh"] = 92

print(students)