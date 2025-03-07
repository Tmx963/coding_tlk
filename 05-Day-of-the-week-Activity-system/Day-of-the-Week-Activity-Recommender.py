#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Faysal
# Created:     27-Feb-2025
# Updated:     15-Aug-2025
#-----------------------------------------------------------------------------


# Ask the user to enter the current day of the week (e.g., "Monday", "Tuesday").
Day = input("Enter the any of thr week: ")
#Use conditional statements to recommend an activity based on the day.
if Day == "monday":
    print("start your week with a workout!")
elif Day == "Tuesday":
    print(" it'a a greate day to read a book!")
elif Day == "Wednesday":
    print("Mid-week movie night: ")
elif Day == "Thursday":
    print(" try something new: ")
elif Day == "Friday":
    print(" relaxing day: ")
elif Day == "Saturday":
    print(" Going out: ")
elif Day == "Sunday":
    print(" Finishing homework: ")
else:
    print(" the last day of the week: ")
