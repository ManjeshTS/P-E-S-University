# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:02:17 2024

@author: manjesh
"""

n=input("Enter the number : ")
sum=0
for i in n:
    i=int(i)
    sum=sum+i
    
print(f"Sum of all the digits of the number {n} = {sum}")