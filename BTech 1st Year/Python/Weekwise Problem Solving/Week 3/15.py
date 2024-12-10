# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:30:18 2024

@author: manjesh
"""

p=int(input("Enter the Number of Pizzas : "))
n=int(input("Enter the Number slices per Pizzas : "))
a=int(input("Enter the Number of friends  : "))
print("Number of slices each will get is = ", (p*n)//a)
print("Number of slices left is = ", (p*n)-(((p*n)//a)*a))