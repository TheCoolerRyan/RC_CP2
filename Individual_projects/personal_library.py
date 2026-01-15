#RC 1st, personal library program

#Create list for lists of books and authors
collection = []
#Create tupple of the functions
functions = ("add","view","remove","search","exit")

#Create add function
def add(collection):
    #Ask for them to input the title
    title = input("Please give me the book title.").strip().title()
    #Ask them to input the author
    author = input("Please give me the Author").strip().title()
    #Then put those to values into a list and add that to the list
    collection.append([title,author])
    #Print off what you have added
    print(f"You have added:\n{title} by {author}!")
    return collection

#Create view function
def view(collection):
    #For everything in the list, print of book name by author
    for i in collection:
        print(f"{i[0]} by {i[1]}")

#Create remove function
def remove(collection):
    #for every list in the list, print off them numbered and author by name
    x = 1
    for i in collection:
        print(f"{x}. {i[0]} by {i[1]}")
        x += 1
    #Have them input what number they would like to get rid of
    while True:
        rid = input("What number would you like to get rid off?").strip()
        if rid.isdigit() == True and int(rid) > 0 and int(rid) < x+1:
            rid = int(rid)-1
            break
        else:
            print("That is not a valid option...")
    collection = collection.pop(rid)
    #Return new list
    return collection

#Create search function
def search(collection):
    #Ask them if they would like to search based of off title or author
    while True:
        method = input("Would you like to search using the author, or the title?:").strip().lower()
        if method == "author" or method == "title":
            break
        else:
            print("That is not an option.")
    #if its based of off author then for each list in the list, check the list[1] for the author
    if method == "author":
        for i in collection:
            if method in collection[i[1]]:
                print(f"{i[0]} by {i[1]}")
            else:
                pass
    #if its based of off title, then for each list in the list, check the list[0] for the title
    elif method == "title":
        for i in collection:
            if method in collection[i[0]]:
                print(f"{i[0]} by {i[1]}")
            else:
                pass
    else:
        print("How did you manage this?")

#Create main function
    #Put it in a main while loop
            #Ask them what function they would like while in a while loop
            #Check if its in a tupple
            #Break
        #Then put if statements to run the function and see which function they chose.
    