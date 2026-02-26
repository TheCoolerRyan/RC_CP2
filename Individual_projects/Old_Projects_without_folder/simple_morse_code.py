# RC 1st, Simple Morse Code Translator

#Create stupid proff function
def simple(sentance):
    #set the sentance to .lower and .strip
    sentance = (f"{sentance}").strip().lower()
    #return the answer
    return sentance

#Create a function to take the letters index in the list and then flip it
def comparison(sentance, choice,alphabet,morse_code):
    #Check to see which one of the functions its coming from
    if choice == "letter":
        #Create a string for the final sentance
        final = ""
        #Check each and every one to see which letter it is, then add that to the final string.
        for i in sentance:
            if i == " ":
                final + i
            else:
                index = alphabet.index(i)
                pick = morse_code[index]
                final = final + pick + " "
        return final
    #Repeat earlier code, but for morse code instead.
    else:
        final = ""
        for i in sentance:
            if i == "space":
                final += " "
            else:
                index = morse_code.index(i)
                pick = alphabet[index]
                final += pick
        return final


#Create a function to turn letters into morse code
def morse(alphabet,morse_code):
    choice = "letter"
    while True:
        good = True
    #Ask them for there sentance and aplly the stupid proff function
        sentance = input("Please give me a sentance you want to turn into morse code (No numbers):")
    #Make sure the answer is correct formating
        if len(sentance) > 0:
            for i in sentance:
                if i.isdigit() == True:
                    good = False
                else:
                    pass
            if good == True:
                sentance = simple(sentance)
                break
            else:
                print("No numbers, please.")
        else:
            print("Please make sure that there is only letters and that you actually type something...")
        
    #Then take that sentance add them to a list
    sentance = list(sentance)

    #print(Use the list comparasin function)
    print(f"\n{comparison(sentance,choice,alphabet,morse_code).capitalize()}\n")

#Create a function to turn morse code back into english
def words(alphabet,morse_code):
    #Put them into a while loop
    choice = "morse"
    sentance = []
    while True:
        #Ask them for the first part of morse code (The first letter sequence)
        pick = simple(input("Please give me a letter in morse code. If you want a space, type space. If you want to stop adding, put exit instead. (e.g. for morse code input ->  .--):"))
        #Check to make sure that its morse code, then add that to a list
        if pick in morse_code or pick == "space":
            sentance.append(pick)
        #If they put exit, have them stop inputing
        elif pick == "exit":
            break
        else:
            print("Please only input correct morse code...")

    #print(Use the list comparasin function)
    print(f"\n{comparison(sentance,choice,alphabet,morse_code).capitalize()}\n")


#Create main function
def main():
    #Explain
    print("This is a program that allows you to convert morse code to english and convert english to morse code. Please have a fun time and follow the rules!!!  :)")

    #Create two tuples containing morse code and letters
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    morse_code = (".-", "-...", "-.-.", "-..",  ".", "..-.", "--.",  "....", "..", ".---", "-.-", ".-..",  "--", "-." "---",  ".--.", "--.-", ".-.",  "...", "-",  "..-",  "...-", ".--",  "-..-", "-.--","--..")
    
    #loop to keep things going.
    while True:
        while True:
            #Print of all options and ask them which one they want to do
            choice = input("1. Turn sentance into Morse Code\n2. Turn Morse Code into english\n3. Exit\n")
            #Get correct input
            if choice == "1" or choice == "2" or choice == "3":
                break
            else:
                print("Please put 1, 2, 3.")

        #Then proceed to run the function that they selected (If it is exit, then quit/break)
        if choice == "1":
            morse(alphabet,morse_code)
        elif choice == "2":
            words(alphabet,morse_code)
        else:
            break



main()