"""
Author: Noah Weston
Date: 26 Oct 22
Assignment: 01 Checkpoint: Review Python
Purpose: Assess knowledge of python
"""
#Get input
userAge = float(input("Please enter your age: "))

#Calculate heart rate max
maxHeartRate = 220 - userAge

#Calculate exercise range
maxRate = 0.85*maxHeartRate
minRate = 0.65*maxHeartRate

#Display info
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {minRate:.0f} and {maxRate:.0f} beats per minute.")