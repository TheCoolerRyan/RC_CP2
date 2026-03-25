#RC 1st, main for gradbook

#Import basic files and make basic variables
from calculations import *
options = ["Add New Student", "Add Grade to Student", "View Student Record", "View All Students", "Class Summary", "Exit"]
#Create the main loop
def main(options):
    while True:
    #Ask them what of the 6 funtions they want to do
    #Get valid input
        while True:
            x =1
            for i in options:
                print(f"{x}. {options}")
                x += 1
            choice = input("Please enter the number of the options above:").strip()
            if choice.isdigit() == True and int(choice) >= 1 and int(choice) <= 6:
                choice = int(choice)
                break
            else:
                print("Please enter a valid input/number...")
        #Depending on if its 1-5,run there function. If its 6 then break.
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            break
        else:
            print("How the crap did you manage this???")


main(options)