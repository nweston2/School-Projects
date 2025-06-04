"""
Author: Noah Weston
Date: 
Assignment: 10 Prove Assignment: Handling Exceptions
Purpose: Prove that you can write a Python program that reads CSV files and creates, populates, and uses a dictionary.
"""
import csv
from datetime import datetime

def debug(string):
    """
    If you aren't sure something works right, comment out the false debug flag and use debug as an optional print statement
    """
    nwDebug = True
    #nwDebug = False
    if nwDebug:
        print(string)

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary
    dictionary = {}

    try:
        # Open file
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            
            # Skip the headers
            next(reader)

            # Read the product list into a dictionary one line at a time
            for line in reader:
                # Skip blank lines
                if len(line) > 0:
                    # Set the key for the dictionary
                    key = line[key_column_index]

                    # Set values for given key
                    dictionary[key] = line

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                " because you don't have permission.")

    return dictionary

def get_request(filename):
    """
    Get a shopping list
    """
    # Create a list
    #nwdictionary = {} #Creates a dictionary that doesn't help. See note below
    nwlist = []
    try:
        # Open file
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)

            # Skip the headers
            next(reader)

            # Read the shopping list one line at a time
            for line in reader:
                # Skip blank lines
                if len(line) > 0:
                    # Read in the lists
                    nwlist.append(line)

                    #The following lines create a list that adds multiples of the same thing together. I'm proud of it so it stays
                    #key = line[0]
                    #nwAmount = int(line[1])
                    #if key in nwdictionary:
                        #nwdictionary[key] += nwAmount
                    
                    #else:
                        #nwdictionary[key] = nwAmount


        # Test exception of unknown item number
        #nwlist.append(["R002",5])

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                " because you don't have permission.")
        
    return nwlist

def main():
    try:
        #Create product dictionary
        nwProductIndex = 0
        nwProductFile = "products.csv"
        nwproduct_dict = read_dict(nwProductFile, nwProductIndex)

        # Make sure dictionary was created properly
        debug(nwproduct_dict)

        # Get a shopping list
        nwShoppingFile = "request.csv"
        nwShoppingList = get_request(nwShoppingFile)

        # Check it twice
        debug(nwShoppingList)

        # Name the store
        print("Welcome to Inkom Imporium\n\nYour shopping list:")

        # Print list of items
        nwTotal = 0
        nwItemCount = 0
        for item in nwShoppingList:
            # Get needed from shopping list
            nwKey = item[0]
            nwQuantity = item[1]
            nwQuantity = int(nwQuantity)
            nwItemCount += nwQuantity

            # Get needed info from dictionary
            nwValues = nwproduct_dict[nwKey]
            nwProductName = nwValues[1]
            nwItemPrice = nwValues[2]
            nwItemPrice = float(nwItemPrice)

            # Compute costs
            nwPrice = nwItemPrice * nwQuantity
            nwTotal += nwPrice

            # Print item info
            print(f"{nwProductName}: {nwQuantity} @ ${nwItemPrice}")

        # Compute tax
        nwTax = 0.06 * nwTotal
        nwFinalPrice = nwTotal + nwTax

        # Print totals
        print(f"\nNumber of items: {nwItemCount}")
        print(f"Subtotal: ${nwTotal:.2f}")
        print(f"Sales Tax: ${nwTax:.2f}")
        print(f"Total: ${nwFinalPrice:.2f}")

        # Say your goodbyes
        print("\nThank you for shopping at Inkom Imporuim")
        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%A %B  %d, %Y %I:%M %p}")

    except KeyError as key_err:
        print("unknown product ID in the request.csv file")

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {nwProductFile}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from {nwProductFile}"
                " because you don't have permission.")

if __name__ == "__main__":
    main()