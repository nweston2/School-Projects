"""
Author: Noah Weston
Date: 10 Dec 2022
Assignment: Final Project
Purpose: Prove I know what I'm doing
"""
import random

def debug(string):
    """
    Catch the pesky bug
    """
    nwFlag = False
    #nwFlag = True
    if nwFlag:
        print(string)

def get_goal():
    """
    Is there a number the user is trying to beat? If so, what is it?
    """
    # Is there a number to beat?
    nwGoal = input("Is there a number you are trying to beat?(type \"yes\" or \"no\") ")

    if nwGoal.lower() == "yes":
        # What is the number?
        nwGoal = input("What is the number you are trying to beat? ")
    
    print()

    return nwGoal


def get_sides():
    """
    Prompt the user for the number of sides on the dice being rolled
    """
    nwSides = input("How many sides on the die?(Type 'quit' when finished) ")
    return nwSides


def get_volume():
    """
    Prompt the user for the number of dice to be rolled
    """
    nwAmount = input("How many dice with this number of sides would you like to roll? ")
    nwAmount = int(nwAmount)
    print()
    return nwAmount


def gather_die():
    """
    Create a list of all die being rolled
    """
    nwBag = []
    nwSides = ""
    nwAmount = 0

    # Allow the user to create a list of dice to be rolled
    while nwSides != "quit":

        # Ask the user how many sides on the die
        nwSides = get_sides()
        nwDie = []
        
        # As long as the user hasn't quit on us, ask how many of that type of dice to roll
        if nwSides != "quit":
            nwSides = int(nwSides)
            
            # Make sure they aren't being tricksy
            if nwSides < 2:
                print("Nice try. Try again.")

            else:
                # Throw these dice in the bag
                nwAmount = get_volume()
                nwDie = [nwSides, nwAmount]
                nwBag.append(nwDie)

    debug(nwBag)
    return nwBag


def roll_die(diceList):
    """
    Get the value of rolled dice
    """
    nwTotal = 0

    # Go through the list of dice and roll each one, then add to total
    for set in diceList:
        nwSides = set[0]
        nwAmount = set[1]
        while nwAmount > 0:
            nwValue = random.randint(1,nwSides)
            nwTotal += nwValue
            nwAmount -= 1

    return nwTotal


def final_message(total,goal):
    """
    Tell the user what they rolled
    """
    # If they had a number to beat, let them know if they succeeded
    if goal != "no":
        nwGoal = int(goal)

        # Sad day message
        if nwGoal > total:
            nwDeficit = nwGoal - total
            nwMessage = f"\nSorry, the total of your roll is {total}. You were {nwDeficit} short of your target."

        # Jubilation
        else:
            nwMessage = f"\nThe total of your roll is {total}! Congradulations! You beat your target!"

    else:
        nwMessage = f"\nThe total of your roll is {total}!"
    
    return nwMessage

def main():
    """
    Run the program
    """
    # Are you trying to beat a number? If so, what is it?
    nwGoal = get_goal()

    # Get the number of dice you are rolling
    nwBag = gather_die()

    # Roll the dice
    nwTotal = roll_die(nwBag)

    # Display the results
    nwFinalMessage = final_message(nwTotal,nwGoal)
    print(nwFinalMessage)


if __name__ == "__main__":
    main()