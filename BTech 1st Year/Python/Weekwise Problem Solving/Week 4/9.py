# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:05:18 2024

@author: manjesh
"""

# a
n=int(input("Enter the number of a power :"))
result = []
for i in range(n+1):
    result.append(2 << i)  # Left shift 1 by i positions
print(result)

#b
n1=int(input("Enter the number (n) : "))

if n1 and 1==0:
    print("Even Number")
else:
    print("Odd Numbers")

# or 
if (n1 and 1) == 0:
    print("Even Number")
else:
    print("Odd Number")
    
#c
n2=int(input("Enter the number (n) : "))
result=(n << 5) | (n << 1)

print(result)