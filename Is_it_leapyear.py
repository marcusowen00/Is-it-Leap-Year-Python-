import os
import platform

#Check if it's leap year or not
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return "Yes, it is a leap year."
    elif year % 400 == 0:
        return "Yes, it is a leap year."
    else:
        return "No, it is not a leap year."

#User Input
while True:
    try:
        year = int(input("Enter a year : "))
    except ValueError:
        print("Please only enter years through numbers (E.g 1992, 2014). Try Again\n")
        continue
    else:
        break

#Execution
print(is_leap(year), end="\n")

#Ask the user if it likes to try again or not
quit_or_continue = str(input("Would you like to try again? Y/N : "))
quit_or_continue.lower()
if quit_or_continue == "y":
    if platform.system() == "Windows":
        _=os.system('cls')
        os.system("Is_it_leapyear.py")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        _=os.system('clear')
        os.system("Is_it_leapyear.py")