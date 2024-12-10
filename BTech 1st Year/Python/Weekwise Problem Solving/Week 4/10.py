# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:23:23 2024

@author: manjesh
"""

sum=0
for i in range(1,6):
    a=int(input(f"Enter the Marks of Subject {i} : "))
    sum=sum+a

avg=sum/5

print("Your avg score is = ", avg)
if avg >= 90:
    print("Grade A")
elif avg >= 80 and avg <90:
    print("Grade B")
elif avg >= 70 and avg <80:
    print("Grade C")
elif avg >= 60 and avg <70:
    print("Grade D")