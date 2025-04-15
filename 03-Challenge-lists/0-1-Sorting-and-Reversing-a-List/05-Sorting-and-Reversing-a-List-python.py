#-----------------------------------------------------------------------------
# Name:     Comprehensions and Filtering    (Comprehensions.py)
# Purpose:     To provide information about how Comprehensions and Filtering (if)
#			   work in Python
#
# Author:      Faysal
# Created:     29-March-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------
# create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use list comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
# print both lists
spread_numbers = [num ** 2 for num in even_numbers]
print("even_numbers=", even_numbers)
print("spread_number=", spread_numbers)




