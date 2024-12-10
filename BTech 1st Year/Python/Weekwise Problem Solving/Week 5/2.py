num=[3,5,2,1,4,7,9,6,8]
num2=num.copy()
num2.sort()
print(num2)
if num == num2:
    print("The list is Sorted")
else:
    print("The list is not sorted \nSorted list is : ", num2)
