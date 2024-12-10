n=int(input("Enter the number : "))
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
if n==0 or n==1:
    print(f'[n] is neither a prime nor a composite Number')
elif count==0:
    print(f'{n} is a prime number')
else:
    print(f'{n} is a composite Number')