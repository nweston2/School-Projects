"""
Author: Noah Weston
Date: 27 Oct 2022
Assignment: 01 Prove Milestone: Review Python
Purpose: Calculate the volume of a car tire
"""
import math

#Prepare calculations
def volume(aspect, width, diameter):
    numeratora = math.pi * width**2 * aspect
    numeratorb = (width * aspect) + (2540 * diameter)
    v = (numeratora * numeratorb) / 10000000000
    return v

#Prompt user for tire measurements
a = int(input("What is the aspect ratio of your tire? "))
w = int(input("What is the width of your tire? "))
d = int(input("What is the diameter of your tire? "))

#Display results
print(f"\nThe approximate volume is {volume(a, w, d):.2f} liters")