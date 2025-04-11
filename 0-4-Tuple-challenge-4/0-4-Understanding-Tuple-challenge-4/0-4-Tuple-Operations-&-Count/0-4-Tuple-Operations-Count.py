#-----------------------------------------------------------------------------
# Name:     Understanding Tuples in Python   (Tuples.py)
# Purpose:     To provide information about how Understanding Tuples in Python (if)
#			   work in Python
#
# Author:      Faysal
# Created:     2-April-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------


# creating a tuple with repeated values
fruit_tuple = ("apple", "banana", "cherry", "banana", "apple")

# ask user to enter a fruit name
fruit_name = input("enter a fruit name: ")

# counting occurrences of the fruit in the tuple
count = fruit_tuple.count(fruit_name)
print(f"'{fruit_name}' appears {count}  times in the tuple.")
