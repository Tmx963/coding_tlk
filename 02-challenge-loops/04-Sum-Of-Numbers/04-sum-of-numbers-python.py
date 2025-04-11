#-----------------------------------------------------------------------------
# Name:        Loops (challenges)
# Purpose:     Sum of numbers
# Author:       Faysal
# Created:     19-Mar-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------

from functools import total_ordering

n = int(input("Enter a number: ")) # Get user input
total = 0
for i in range(1, n + 1): # loop from 1-10
    total += i #Add each number to total
    print("sum =", total) # print the result
