#-----------------------------------------------------------------------------
# Name:        Loops (break and continue)
# Purpose:     loops control statements
# Author:       Faysal
# Created:     24-Mar-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------


# countdown timer program
count = 10 # start from 10
while count > 0:
    print(count)
    user_input = input('Enter "Stop" to cancel or press Enter: ') #Get user input
    if user_input.lower() == "Stop":
     print("countdown stopped!")
    break
count -= 1

