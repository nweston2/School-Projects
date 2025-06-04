"""
Author: Noah Weston
Date: 1 Nov 2022
Assignment: 02 Team Activity: Calling Functions
Purpose: Calculate sale including daily discount and tax
"""
from datetime import datetime

def main():
    #Determine the day of the week
    current_date_and_time = datetime.now()
    day_of_week = current_date_and_time.weekday()

    #Get sale amount from user
    subtotal = float(input("Please enter the subtotal: $"))

    #If applicable, determine discount
    discount = 1
    discountAmount = 0
    if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
        discount = 0.1
        discountAmount = subtotal * discount
        subtotal -= discountAmount
        print(f"Discount amount: ${discountAmount:.2f}")

    #Calculate tax
    tax = subtotal * 0.06
    print(f"Sales tax amount: ${tax:.2f}")

    #Display total
    total = subtotal + tax 
    print(f"Total: ${total:.2f}")

main()