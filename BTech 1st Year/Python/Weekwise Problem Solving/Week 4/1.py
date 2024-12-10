# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:38:38 2024

@author: manjesh
"""

n=int(input("Enter the value of n : "))
sum=0
for i in range(0,n+1,2):
    sum+=i
    
print("The sum of all even Natural numbers till", n ,"is = ", sum)