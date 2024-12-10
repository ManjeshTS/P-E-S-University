# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:13:56 2024

@author: manje
"""

radius = float(input("Enter the radius of the circle: "))

pi_approx = 3.14159
area_circle = pi_approx * radius * radius

area_red = area_circle / 4

area_remaining = area_circle - area_red

area_blue = area_remaining / 3

area_yellow = area_remaining - area_blue

perimeter_red = (pi_approx * radius) / 2 + 2 * radius

angle_blue = (360 * area_blue) / area_circle

arc_length_blue = (angle_blue / 360) * 2 * pi_approx * radius

perimeter_blue = arc_length_blue + 2 * radius


angle_yellow = (360 * area_yellow) / area_circle

arc_length_yellow = (angle_yellow / 360) * 2 * pi_approx * radius

perimeter_yellow = arc_length_yellow + 2 * radius

print("Area of red section:", area_red)
print("Perimeter of red section:", perimeter_red)
print("Area of blue section:", area_blue)
print("Perimeter of blue section:", perimeter_blue)
print("Area of yellow section:", area_yellow)
print("Perimeter of yellow section:", perimeter_yellow)