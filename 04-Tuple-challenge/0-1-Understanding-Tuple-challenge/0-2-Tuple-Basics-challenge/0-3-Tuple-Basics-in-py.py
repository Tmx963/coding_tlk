#-----------------------------------------------------------------------------
# Name:     Understanding Tuples in Python (Tuples.py)
# Purpose:     To provide information about how Tuples (if)
#			   work in Python
#
# Author:      Faysal
# Created:     2-April-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------


# creating the tuple with five different elements
my_tuple = (42, 3.14, "Python", True, (1, 2, 3))

# printing the entire tuple
print(my_tuple)

# Accessing and print the third element
print(my_tuple[2])

# extracting the nested tuple nd printing the first element
nested_tuple = my_tuple[4]
print(nested_tuple[0])