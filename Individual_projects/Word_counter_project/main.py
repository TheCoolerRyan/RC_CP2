#RC 1st, Main file for word counter project

#Import all of the required files
from txt_handling import *


#Create the main function
def main():
    #Ask them for the direct file path and input into all file cordenants
    path = input("Enter the exact file path for your document:")
    choices = ("Save", "View","Add","Exit")
    sentance = ""
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
            #Once they have a currect variable, break
            if num.isdigit() == True and int(num) >0 and int(num) < 5:
                break
            else:
                print("Please select a number 1-4")

        #If its 1
        if num == "1":
            #Then put them into a while loop to save
            print(save(path,sentance))
        #if its 2
        elif num == "2":
            print(view(path))
        #If its 3
        elif num == "3":
            sentance = add()
        #If its 4
        else:
            #Then quit 
            break

main()