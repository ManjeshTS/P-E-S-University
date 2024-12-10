# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:05:15 2024

@author: manje
"""

w=int(input("Enter the Total Amount of Work : "))
n=int(input("Enter the number of workers : "))
print("The amount of work that each of the worker has to do is = ", w//n)
print("The amount of work left is = ", w-((w//n)*n))
