#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Faysal
# Created:     25-Feb-2025
# Updated:     15-Mar-2025
#-----------------------------------------------------------------------------
# Enter the current temperature
temperature = float(input("Enter the temperature in Celsius:"))
# Conditional statements to provide advice
if temperature < 10:
    print("it's cold outside. wear a jacket!")
elif 10 <= temperature <= 25:
    print(" it's a nice ay. Wear short-sleeves!")
else:
    print("it's hot outside. Stay cool! ")


# Ask the user to enter a number
number = int(input("Enter a number: "))
# check if the number is even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd. ")

