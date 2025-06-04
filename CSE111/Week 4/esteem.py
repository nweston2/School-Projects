"""
Author: Noah Weston
Date: 15 Nov 2022
Assignment: 06 Team Activity: Troubleshooting Functions
Purpose: Determine the well being of the user.
"""
def main():
    """
    Run the main program
    """
    print_info()

    #Create a list of questions
    nwquestion_list = [
        "1. I feel that I am a person of worth, at least on an equal plane with others.",
        "2. I feel that I have a number of good qualities.",
        "3. All in all, I am inclined to feel that I am a failure.",
        "4. I am able to do things as well as most other people.",
        "5. I feel I do not have much to be proud of.",
        "6. I take a positive attitude toward myself.",
        "7. On the whole, I am satisfied with myself.",
        "8. I wish I could have more respect for myself.",
        "9. I certainly feel useless at times.",
        "10. At times I think I am no good at all."
    ]

    #Get answers to questions from user
    nwanswers = get_answers(nwquestion_list)
    nwScore = calculate_score(nwanswers)

    print(f"\nYour score is {nwScore}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def get_answers(question_list):
    """
    Given a list of questions, return a list of answers from user.
    """
    nwanswer_list = []

    #Loop through the questions and create an answer list
    for question in question_list:
        print(question)
        nwanswer = input("\tEnter D, d, a, or A: ")
        nwanswer_list.append(nwanswer)
        
    return nwanswer_list

def print_info():
    """
    Literally just print the stuff out front.
    """
    print("This program is an implementation of the Rosenberg\nSelf-Esteem Scale. This program will show you ten\nstatements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the\nstatements by responding with one of these four letters:\n")
    print("D means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.\n")

def calculate_score(answers):
    """
    Given a list of answers, convert answers to a score and calculate users' well being.
    """
    nwItemNum = -1
    nwScore = 0
    #Convert answers to numbers
    for answer in answers:
        nwItemNum += 1
        nwPoints = 0

        #Get numbers for positive questions
        if nwItemNum == 0 or nwItemNum == 1 or nwItemNum == 3 or nwItemNum == 5 or nwItemNum == 6:
            if answer == "D":
                nwPoints = 0
            elif answer == "d":
                nwPoints = 1
            elif answer == "a":
                nwPoints = 2
            else:
                nwPoints = 3

        #Get numbers for negative questions
        else:
            if answer == "D":
                nwPoints = 3
            elif answer == "d":
                nwPoints = 2
            elif answer == "a":
                nwPoints = 1
            else:
                nwPoints = 0

        nwScore += nwPoints

    return nwScore

if __name__ == "__main__":
    main()