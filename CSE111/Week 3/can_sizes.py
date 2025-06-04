"""
Author: Noah Weston
Date: 8 Nov 2022
Assignment: 04 Team Activity: Writing Functions
Purpose: Calculate the efficiency of a tin can
"""
import math
def main():
    nwCans = get_list()
    print("Name, Radius, Height, Can Efficiency")
    best = 0
    bestname = ""
    for can in nwCans:
        nwname = can[0]
        nwradius = can[1]
        nwheight = can[2]
        nwefficiency = can_efficiency(nwradius, nwheight)
        print(f"{nwname}, {nwradius}, {nwheight}, {nwefficiency:.2f}")
        if nwefficiency > best:
            bestname = nwname
            best = nwefficiency
    print(f"The most efficient can is {bestname}")

def can_efficiency(radius, height):
    sa = surface_area(radius, height)
    vol = volume(radius, height)
    efficiency = vol / sa
    return efficiency

def surface_area(radius, height):
    nwsurfaceArea = 2*math.pi*radius*(radius+height)
    return nwsurfaceArea

def volume(radius, height):
    nwvolume = math.pi*(radius**2)*height
    return nwvolume

def get_list():
    nwCans = [["#1 Picnic", 6.83, 10.16],["#1 Tall", 7.78, 11.91],["#2", 8.73, 11.59],["#2.5", 10.32, 11.91],
        ["#3 Cylinder", 10.79, 17.78],["#5", 13.02, 14.29],["#6Z", 5.40, 8.89],["#8Z short", 6.83, 7.62],
        ["#10", 15.72, 17.78],["#211", 6.83, 12.38],["#300", 7.62, 11.27],["#303", 8.10, 11.11]]
    return nwCans

main()