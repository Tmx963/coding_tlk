# -----------------------------------------------------------------------------
# Name:      set methods   ( set methods.py)
# Purpose:     To provide information about how set methods work in
#			   Python
#
# Author:      Faysal
# Created:     7_April-2025
# Updated:     15-Aug-2025
# -----------------------------------------------------------------------------
data = {10, 20, 30, 40, 50}
data_copy = data.copy()
print("copy", data_copy)

data.pop()
print("After pop:", data)

data.clear()
print("After clear:", data)