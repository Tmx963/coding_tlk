# -----------------------------------------------------------------------------
# Name:      Adding and Removing Elements (Using Update and Discard)     ( Adding and Removing Elements (Using Update and Discard)   .py)
# Purpose:     To provide information about how  Adding and Removing Elements (Using Update and Discard) work in
#			   Python
#
# Author:      Faysal
# Created:     7_April-2025
# Updated:     15-Aug-2025
# -----------------------------------------------------------------------------
letters = {'a', 'b', 'c'}
letters.update({'d', 'e', 'f'})
letters.discard('b')
print(letters)
