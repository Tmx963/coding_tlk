#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Faysal
# Created:     27-Feb-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------

#Ask the user to enter their age
Age = int(input("Enter your age: "))
if Age > 18:
    print("You are eligible for vote!")
# Check if the person is eligible to vote
else:
    print("Sorry, you are not eligible for vote.")
