# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:09:58 2024

@author: manje
"""

n=int(input("Enter the number : "))
sum=0
print(n%10)
sum+=n%10
n=n//10
print(n%10)
sum+=n%10
n=n//10
print(n%10)
sum+=n%10
n=n//10
print(n%10)
sum+=n%10
n=n//10
print("The sum of the digits = ", sum)