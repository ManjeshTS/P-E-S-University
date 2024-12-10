# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:43:06 2024

@author: manjesh
"""

n=int(input("Enter the Number to which you want to Calculate Factorail : "))

# Using For Loop

fact=1
for i in range(1, n+1):
    fact*=i
    
print(f"The factorial of {n} is = {fact}")

# Using While loop
a=n
fac=1
while n>0:
    fac*=n
    n-=1
    
print(f"The factorial of {a} is = {fac}")