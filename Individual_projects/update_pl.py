#RC 1st, update personal library program

import csv

#Create add function
def add(collection):
    #Ask for them to input the title
    title = input("Please give me the book title:").strip().title()
    #Ask them to input the author
    author = input("Please give me the Author:").strip().title()
    while True:
        year = input("Please give me the year it was publish:").strip()
        if year.isdigit() == True:
            break 
        else:
            print("Thats not a number...")
    genre = input("Please give me the main genre:").strip().title()
    #Then put those to values into a list and add that to the list
    collection.append({title: [author, year, genre]})
    #Print off what you have added
    print(f"You have added:\n{title} by {author}! Published in {year} and its main genre is {genre}!")
    #Spacer for easier viewing (Added while improving code)
    print("\n")
    return collection

#Create view function
def view(collection):
    #For everything in the list, print of book name by author
    while True:
        choice = input("If you would like to see a detaild list put 1, if you want to see a simple list put 2:")
        if choice == "1" or choice == "2":
            break
        else:
            print("Thats not available!")
    #print the simple or the complex
    if choice == "1":
        if not collection:
            print("You don't have anything to view...")
        else:
            for i in collection:
                key = list(i.keys())[0]
                value = list(i.values())
                print(f"{key} by {value[0][0]}! Published in {value[0][1]} and its main genre is {value[0][2]}!")
    else:
        if not collection:
            print("You don't have anything to view...")
        else:
            for i in collection:
                key = list(i.keys())[0]
                value = list(i.values())
                print(f"{key} by {value[0][0]}")
    #Spacer for easier viewing (Added while improving code)
    print("\n")

#Create remove function
def remove(collection):
    #for every list in the list, print off them numbered and author by name
    if not collection:
        print("There is nothing to remove...")
    else:
        x = 1
        for i in collection:
            key, value = i.keys()
            print(f"{x}. {key} by {value[0]}")
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

#create a save function
def save(collection):
    #Save the curret collection
    with open("Individual_projects/books.csv", mode = "w", newline= "") as csv_file:
        fieldnames = ['title','creator','year','genre']
        writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
        for i in collection:
            key = list(i.keys())[0]
            value = list(i.values())
            writer.writerow({'title': key, 'creator': value[0][0], 'year': value[0][1], 'genre': value[0][2]})
    
    #Pull to reconnect everything
    try:
        with open("Individual_projects/books.csv",mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            collection = []
            for line in content:
                collection.append({line[0]: [line[1],line[2],line[3]]})
    except:
        print("Can't find file...")
    else:
        print("Library saved")
    #Return the list to continue working.
    return collection

#Create main function
def main():
    #Create tupple of of functions
    functions = ("add","view","remove","search","save", "exit")
    #Create list for lists of books and authors
    collection = []
    #Put it in a main while loop
    while True:
        try:
            with open("Individual_projects/books.csv",mode = "r") as csv_file:
                content = csv.reader(csv_file)
                headers = next(content)
                collection = []
                for line in content:
                    collection.append({line[0]: [line[1],line[2],line[3]]})
        except:
            print("Can't find file...")
        while True:
            #Ask them what function they would like while in a while loop
            x = 1
            for i in functions:
                i = i.title()
                print(f"{x}. {i}")
                x +=1
            choice = input("What function would you like to chose? (Please put the name, not the number, inside of view there is also an option for detailed viewing):").strip().lower()
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
        elif choice == "save":
            collection = save(collection)
        else:
            print("How the crap did you manage this?????")
    

main()