n=int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j , end="   ")
#     print()
a=1
b=1
for i in range(1,n+1):
    if i <= n:
        print(a*i, end=" ")
        
        
    elif i==n:
        b=b+1