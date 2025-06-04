"""
Author: Noah Weston
Date: 2 Nov 2022
Assignment: 02 Prove: Calling Functions
Purpose: Practice calling functions and working with files
"""
from datetime import datetime
import math

#open file
def write_to_file(date, width, ratio, diameter, volume):
    with open("volumes.txt", "at") as volumes:
        print(f"{date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=volumes)

#Prepare calculations
def volume(aspect, width, diameter):
    nwnumeratora = math.pi * width**2 * aspect
    nwnumeratorb = (width * aspect) + (2540 * diameter)
    nwv = (nwnumeratora * nwnumeratorb) / 10000000000
    return nwv

def main():
    #Get values from user
    nwdate = datetime.now()
    nwaspect = int(input("What is the aspect ratio of your tire? "))
    nwwidth = int(input("What is the width of your tire? "))
    nwdiameter = int(input("What is the diameter of your tire? "))
    nwvolume = volume(nwaspect, nwwidth, nwdiameter)

    #Write information to file
    write_to_file(nwdate, nwwidth, nwaspect, nwdiameter, nwvolume)

main()