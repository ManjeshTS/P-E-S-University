list=[]
n=int(input("Enter the Number of elements : "))
for i in range(1,n+1):
    n=int(input(f"Enter the item no {i}: "))
    list.append(n)

count=0
min=float('inf')
for i in list:
    count=list.count(i)
    if count < min:
        ans=i
        min=count
    
if n==0:
    print("The List is Empty")
else:
    print("The least Frequent is of ", ans, "and it occurs", min,"time")
