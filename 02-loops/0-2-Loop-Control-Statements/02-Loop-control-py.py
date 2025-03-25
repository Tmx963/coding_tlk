#-----------------------------------------------------------------------------
# Name:        Loops (break and continue)
# Purpose:     loops control statements
# Author:       Faysal
# Created:     17-Mar-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------

for num in range(1, 6):
    if num == 3:
        continue  # Skip printing 3
    if num == 5:
        break  # Stop the loop when num is 5
    print(num)

