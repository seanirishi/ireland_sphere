"""
Program: ireland_sphere.py
Author: Sean Ireland
Date: January 30, 2022

This program calculates the diameter, circumference, surface area, and the volume of a sphere.
Input: The user enters the radius of a circle as an int
Output: The diameter, circumference, surface area, and the volume are all calculated with the supplied radius.
"""

# import the math module
import math

# import the individual resource "pi" from the math module
from math import pi

# imput statement for the user's radius value
radius = float(input('Enter the radius of your sphere: '))

# math to compute the diameter, circumference, surface_area, and volume
diameter = 2 * radius
circumference = diameter * pi
surface_area = 4 * pi * radius * radius
volume = 4/3 * pi * radius * radius * radius

# print statements
print('Diameter:', round(diameter, 2))
print('Circumference:', round(circumference, 2))
print('Surface area:', round(surface_area, 2))
print('Volume', round(volume, 2)))
