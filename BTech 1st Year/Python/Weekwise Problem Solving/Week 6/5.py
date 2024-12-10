list1=["shoe","bag","bottle"]
list2=["bag","paper", "car"]
list3=["Note","belt"]

set1=set(list1)
set2=set(list2)
set3=set(list3)

print("The final list will be ", list(set1 | set2 | set3))