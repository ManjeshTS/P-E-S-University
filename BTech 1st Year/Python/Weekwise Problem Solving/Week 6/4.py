num = [1,2,3,4,5,6,7,8,4,3,2,1,2,3,5,5]
num2=list()

stnum= set(num)
n = 0
for i in stnum:
    count = num.count(i)
    if count > n :
        for j in range(1,count+1):
            num2.insert(0,i)
    else:
        for k in range(1,count+1):
            num2.append(i)
    if n < count:
        n = count
    else:
        n = n
    
print(num2)