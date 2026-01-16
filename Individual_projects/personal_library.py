#RC 1st, personal library program

#Create add function
def add(collection):
    #Ask for them to input the title
    title = input("Please give me the book title:").strip().title()
    #Ask them to input the author
    author = input("Please give me the Author:").strip().title()
    #Then put those to values into a list and add that to the list
    collection.append([title,author])
    #Print off what you have added
    print(f"You have added:\n{title} by {author}!")
    #Spacer for easier viewing (Added while improving code)
    print("\n")
    return collection

#Create view function
def view(collection):
    #For everything in the list, print of book name by author
    for i in collection:
        print(f"{i[0]} by {i[1]}")
    #Spacer for easier viewing (Added while improving code)
    print("\n")

#Create remove function
def remove(collection):
    #for every list in the list, print off them numbered and author by name
    x = 1
    for i in collection:
        print(f"{x}. {i[0]} by {i[1]}")
        x += 1
    #Have them input what number they would like to get rid of
    while True:
        rid = input("What number would you like to get rid off?:").strip()
        if rid.isdigit() == True and int(rid) > 0 and int(rid) < x+1:
            rid = int(rid)-1
            break
        else:
            print("That is not a valid option...")
    collection = collection.pop(rid)
    #Return new list
    #Spacer for easier viewing (Added while improving code)
    print("\n")
    return collection

#Create search function
def search(collection):
    #Ask them if they would like to search based of off title or author
    while True:
        method = input("Would you like to search using the author, or the title?:").strip().lower()
        if method == "author" or method == "title":
            break
        else:
            print("That is not an option.\n")
    #if its based of off author then for each list in the list, check the list[1] for the author
    if method == "author":
        x=0
        authors = input("Please tell me the name you want to search for:").strip().title()
        
        for i in collection:
            if authors == i[1]:
                print(f"\n{i[0]} by {i[1]}")
            else:
                pass
            x+=1
    #if its based of off title, then for each list in the list, check the list[0] for the title
    elif method == "title":
        x= 0
        titles = input("Please tell me the book name you want to search for:").strip().title()
        for i in collection:
            if titles == i[0]:
                print(f"\n{i[0]} by {i[1]}")
            else:
                pass
            x+=1
    else:
        print("How did you manage this?")

#Create main function
def main():
    #Create tupple of of functions
    functions = ("add","view","remove","search","exit")
    #Create list for lists of books and authors
    collection = []
    #Put it in a main while loop
    while True:
        while True:
            #Ask them what function they would like while in a while loop
            x = 1
            for i in functions:
                i = i.title()
                print(f"{x}. {i}")
                x +=1
            choice = input("What function would you like to chose? (Please put the name, not the number):").strip().lower()
            #Check if its in a tupple
            if choice in functions:
                #Break
                break
            else:
                print("That is not an option!!!")

        #Spacer for easier viewing (Added while improving code)
        print("\n")

        #Then put if statements to run the function and see which function they chose.
        if choice == "add":
            collection = add(collection)
        elif choice == "view":
            view(collection)
        elif choice == "remove":
            collection == remove(collection)
        elif choice == "search":
            search(collection)
        elif choice == "exit":
            print("Okay, goodbye and thank you for using my program!!! :)")
            break
        else:
            print("How the crap did you manage this?????")
    

main()