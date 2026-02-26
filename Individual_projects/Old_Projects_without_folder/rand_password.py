#RC 1st, random paswword generator
#Import string to help with character recognition
import string
import random
#Use random.choice
#Creat lists for the random.choice to pull from
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
            if length.isdigit() == True and int(length) > 0:
                length = int(length)
                break
            else:
                print("That is incorect format...")
        
        #Does the password need lowercase letters
        while True:
            lower = input("Would you like there to be lowercase letters? (put y/n):").strip().lower()
            check = stupid(lower)
            if check == True:
                if lower == "y":
                    require_lists.append("low")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")

        #Does the password need uppercase letters 
        while True:
            upper = input("Would you like there to be capital letters? (put y/n):").strip().lower()
            check = stupid(upper)
            if check == True:
                if upper == "y":
                    require_lists.append("up")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")

        #Does the password need numbers 
        while True:
            number = input("Would you like there to be numbers? (put y/n):").strip().lower()
            check = stupid(number)
            if check == True:
                if number == "y":
                    require_lists.append("num")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")

        #Does the password need special characters letters
        while True:
            special = input("Would you like there to be special characters? (put y/n):").strip().lower()
            check = stupid(special)
            if check == True:
                if special == "y":
                    require_lists.append("dif")
                else:
                    pass
                break
            else:
                print("That is incorrect format...")
        if "low" in require_lists or "up" in require_lists or "num" in require_lists or "dif" in require_lists:
            break
        else:
            print("You did not select any of the content options, please pick at least one option as yes.")
    return length, require_lists



#Create function that uses those requirements to create the passwords
def create(characters, require_lists, length,passwords):
    #Use a for loop to go through the main 
    x = 1
    for i in range(1,5):
        password = ""
        #Create the first attempt
        while True:
            correct_password = True
            start = []
            #Then create a loop that will check wether or not the character meets the requirments (Upper, Lower, number, special character).
            for i in range(length):
                start.append(random.choice(characters))
            if "low" not in require_lists:
                for i in start:
                    if i.islower() == True:
                        correct_password = False
                    else:
                        pass
            if "up" not in require_lists:
                for i in start:
                    if i.isupper() == True:
                        correct_password = False
                    else:
                        pass
            if "num" not in require_lists:
                for i in start:
                    if i.isdigit() == True:
                        correct_password = False
                    else:
                        pass
            if "dif" not in require_lists:
                for i in start:
                    if i in string.punctuation:
                        correct_password = False
                    else:
                        pass
            if correct_password == True and check(start,require_lists) == True:
                break
            else:
                pass
        for i in start:
            password += (i)
        passwords[f"Password_{x}"] = password
        x += 1
    return passwords


#Create function to check the passwords
def check(start,require_lists):
    #Check each character in the password 
    good = True
    #Check to make sure that all requirements were met 
    if "low" in require_lists:
        if any(char.islower() for char in start) == True:
            pass
        else:
            good = False
    if "up" in require_lists:
        if any(char.isupper() for char in start) == True:
            pass
        else:
            good = False
    if "num" in require_lists:
        if any(char.isdigit() for char in start) == True:
            pass
        else:
            good = False
    if "dif" in require_lists:
        if any(char in string.punctuation for char in start) == True:
            pass
        else:
            good = False
    #Return true or false depending on the password
    return good
        
   



#Create main  function to run the code
def main():
    #Create all needed variables and put them into a loop to keep the program going
    while True:
        characters = list(string.ascii_letters + string.digits + string.punctuation)
        require_lists = []
        passwords = {}
   
    #Call requirement function
        length, require_lists = requirments(require_lists)

    #Call password creator
        passwords = create(characters, require_lists, length,passwords)

    #Print of all of the passwords
        for key, value in passwords.items():
            print(f"{key}: {value}")

    #Ask them if they want to 
        exit = input("Do you want to quit? If you want to quit, put 1. Otherwise put 2.:").strip()
        if exit == "1":
            break
        else:
            pass
    #If they do, break.


main()