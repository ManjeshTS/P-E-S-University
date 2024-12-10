list=[]
n=int(input("Enter the Number of elements : "))
for i in range(1,n+1):
    n=int(input(f"Enter the item no {i}: "))
    list.append(n)
odd=[]
even=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("ODD = ", odd)
print("EVEN = ", even)