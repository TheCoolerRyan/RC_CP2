#RC 1st, Main file for word counter project

#Import all of the required files
from txt_handling import *


#Create the main function
def main():
    #Ask them for the direct file path and input into all file cordenants
    path = input("Enter the exact file path for your document:")
    choices = ("Save", "View","Add","Exit")
    #Put them into a loop 
    while True:
        #Put them into a while loop and ask if they want to Update document info, view document, add content to document, or exit
        print("Please chose one of the following:")
        x = 1
        for i in choices:
            print(f"{x}. {i}")
            x += 1
        while True:
            num = input()
            if num.isdigit() == True and int(num) >1:

        
        #Once they a currect variable break

        #If its 1
            #Then put them into a while loop to save
        #if its 2

        #If its 3

        #If its 4
            #Then quit 