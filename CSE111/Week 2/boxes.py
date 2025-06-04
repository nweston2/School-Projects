"""
Author: Noah Weston
Date: 31 Oct 2022
Assignment: 02 Checkpoint: Calling Functions
Purpose: Calculate how many boxes are needed
"""
import math

#Define main function
def main():
    #Retrieve values from users
    items = int(input("Enter the number of items: "))
    itemsPerBox = int(input("Enter the number of items per box: "))

    #Caculate number of boxes needed
    boxes = math.ceil(items/itemsPerBox)
    print(f"\nFor {items} items, packing {itemsPerBox} items in each box, you will need {boxes} boxes.")

main()