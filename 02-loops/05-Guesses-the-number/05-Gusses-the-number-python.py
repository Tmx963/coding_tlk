#-----------------------------------------------------------------------------
# Name:        Loops (break and continue)
# Purpose:     loops control statements
# Author:       Faysal
# Created:     19-Mar-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------


# Generate a random number between 1 and 10
import random
target_number = random. randint(1, 10)
# keep asking until the correct number is guessed

while True:
    guess = int(input("Guess the number: ")) # take user input
    if guess == target_number:
     print("Correct! ")
    'break' # Exit the loop
else:
     print(" Wrong, try again! ")




