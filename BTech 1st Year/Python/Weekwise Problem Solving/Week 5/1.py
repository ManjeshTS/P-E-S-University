list=[]
n=int(input("Enter the Number of elements : "))
for i in range(1,n+1):
    n=input(f"Enter the item no {i}: ")
    list.append(n)

for i in list:
    print(i)