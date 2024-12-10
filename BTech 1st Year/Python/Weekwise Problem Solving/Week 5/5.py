#1 
attendence = [("A","P"),("B","A"),("C","P"),("D","A"),("E","P"),("F","P"),("G","A"),("H","P"),("I","P"),("J","P")]
count=0
a=0
for i in range(len(attendence)):
        if attendence[i][1]=="P":
            count+=1
        elif attendence[i][1]=="A":
            a+=1
            
print("Number of Students Present : ",count)
print("Number of Students Absent : ",a)

#2
name=input("Enter the name of the student : ")
status=input("Enter the status : ")
for i in attendence:
    if name in i:
        if status not in i:
            a=list(i)
            a[1]=status
            attendence[attendence.index(i)]=(name,status)
            print("Status is Updated")
        else:
            print("The Status is Correct, No change to be done")
        break
print(attendence)

#3
n=input("Enter the Name of Student : ")
s=input("Enter the status : ")
new=(a,s)
attendence.append(new)
