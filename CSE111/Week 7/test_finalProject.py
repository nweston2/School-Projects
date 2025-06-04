"""
Author: Noah Weston
Date: 10 Dec 2022
Assignment: Final Project
Purpose: Test the functions in the final project
"""
import finalProject
import pytest

def test_final_message():
    """
    The function gather_die puts together a list of which die to roll.
    This function is designed to make sure gather_die works properly.
    """
    # Test no goal
    nwTotal = 10
    nwGoal = "no"
    nwMessage = finalProject.final_message(nwTotal,nwGoal)
    assert nwMessage == f"\nThe total of your roll is {nwTotal}!"

    # Test beat goal
    nwTotal = 10
    nwGoal = "9"
    nwMessage = finalProject.final_message(nwTotal,nwGoal)
    assert nwMessage == f"\nThe total of your roll is {nwTotal}! Congradulations! You beat your target!"

    # Test fail goal
    nwTotal = 10
    nwGoal = "11"
    nwGoalNum = 11
    nwDeficit = nwGoalNum - nwTotal
    nwMessage = finalProject.final_message(nwTotal,nwGoal)
    assert nwMessage == f"\nSorry, the total of your roll is {nwTotal}. You were {nwDeficit} short of your target."
    

def test_roll_die():
    """
    The function roll_die takes a list of dice, rolls each one, and adds 
    the result to the total. This function is designed to make sure roll_die
    works properly.
    """
    # Test on a single die
    nwList = [[20,1]]

    for _ in range(100):
        nwTotal = finalProject.roll_die(nwList)

        # Min roll
        assert nwTotal >= 1

        # Max roll
        assert nwTotal <= 20

    # Test on multiple of the same
    nwList = [[20,10]]

    for _ in range(100):
        nwTotal = finalProject.roll_die(nwList)

        # Min roll
        assert nwTotal >= 10    # 1 * 10

        # Max roll
        assert nwTotal <= 200   # 20 * 10

    # Test on many different
    nwList = [[20,2],[10,3],[4,5]]
    
    for _ in range(100):
        nwTotal = finalProject.roll_die(nwList)

        # Min roll
        assert nwTotal >= 10   # 1 * 2 + 1 * 3 + 1 * 5

        # Max roll
        assert nwTotal <= 90   # 20 * 2 + 10 * 3 + 4 * 5

pytest.main(["-v", "--tb=line", "-rN", __file__])