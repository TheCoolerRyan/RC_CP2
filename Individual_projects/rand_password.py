#RC 1st, random paswword generator
#Import string to help with character recognition
import string

#Use random.choice
#Creat lists for the random.choice to pull from
characters = list(string.ascii_letters + string.digits + string.punctuation)
require_lists = []
#Create stupid proffing function
def stupid(letter):
    #Check to see if the value is y or n, if it is the return true
    if letter == "y" or letter == "n":
        return True
    #If it is not correct format, return false
    else:
        return False



#Create function for asking for password requirements
def requirments(require_lists):
    #Create a loop to keep the requirements correct
    while True:
        #Ask for the length of the password and check to see that its a number
        while True:
            length = input("What should the length of the password be? (Only numbers please):").strip()
            if length.isdigit() == True:
                length = int(length)
                break
            else:
                print("That is incorect format...")
        
        #Does the password need lowercase letters
        while True:
            lower = input("Would you like there to be lowercase letters? (put y/n):").strip()
            check = stupid(lower)
            if check == True:
                if special == "y":
                    require_lists.append("low")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")

        #Does the password need uppercase letters 
        while True:
            upper = input("Would you like there to be capital letters? (put y/n):").strip()
            check = stupid(upper)
            if check == True:
                if special == "y":
                    require_lists.append("up")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")

        #Does the password need numbers 
        while True:
            number = input("Would you like there to be numbers? (put y/n):").strip()
            check = stupid(number)
            if check == True:
                if special == "y":
                    require_lists.append("num")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")

        #Does the password need special characters letters
        while True:
            special = input("Would you like there to be special characters? (put y/n):").strip()
            check = stupid(special)
            if check == True:
                if special == "y":
                    require_lists.append("dif")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")
        break
    return length,






#Create function that uses those requirements to create the passwords
def create(characters, require_lists):
    #Use a for loop to go through the main 
    while True:
        #Then create a loop that will check wether or not the character meets the requirments (Upper, Lower, number, special character).

            #If it does, break and add it to the final string
            #Otherwise get a new thing from it


#Create function to check the passwords
    #Check each character in the password 
        #Then check to make sure that it follows the requirments
    #Check to make sure that all requirements were met 
    #Return true or false depending on the password





#Create main  function to run the code
    #Put them into a loop to keep the program going
    #Call requirement function


    #Loop though this 4 times
        #Then Create a loop that goes until the password is right

            #Call password creator

            #Call password cheacker
            #If password checker returns true then break from this

    #Print of all of the passwords

    #Ask them if they want to exit

    #If they do, break.