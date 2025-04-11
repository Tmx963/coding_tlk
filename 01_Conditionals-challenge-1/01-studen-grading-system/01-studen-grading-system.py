#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:       Faysal
# Created:     26-Feb-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------

# Using 'elif' in a conditional
if x > 1:
    print("It's not supposed to be!")
elif y == 2:
    print('Yup!')
else:
    print('Nope!')

#Student grading system
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif  score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")