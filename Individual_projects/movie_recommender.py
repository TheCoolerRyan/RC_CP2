#RC 1st, movie recommender
import csv

def paser():
    try:
        with open("Individual_projects/movies_list.csv", mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = {}
            for line in content:
                rows[line[0]] = [line[1],line[2],line[3],int(line[4]),[line[5]]]

    except:
        print("We can't find the csv file")
    return rows


def genres(rows, not_available):
    contains = ["Sci-Fi", "Adventure", "Comedy", "Animation", "Drama", "History", "Biography", "Sport", "Family", "Romance",]
    print("Available genres ->")
    for i in contains:
        print((i).title())
    while True:
        genre = input("\nWhat genre would you like to search for:").strip().title()
        if genre in contains:
            break
        else:
            print("That is not a available option...")
    for key, value in rows.items():
        amount = list((f"{value[1]}").split("/"))
        if len(amount) == 1:
            if value[1] != genre and genre not in amount:
                not_available.append(key)
            else:
                pass
        else:
            if amount[0] != genre and amount[1] != genre and genre not in amount:
                not_available.append(key)
            else:
                pass
    return not_available


def directors(rows, not_available):
    while True:
        exit = False
        for i in rows.values():
            print(f"{i[0]}")
        director = input("Please input what director you would like to see. (Both first and last name):").strip().title()
        for i in rows.values():
            z = list(i[0].split(","))
            for x in z:
                if director == x:
                    exit = True
                    break
                else:
                    pass
            if exit == True:
                break
            else:
                pass
        if exit == True:
            break
        else:
            pass
    for key, value in rows.items():
        amount = list((f"{value[0]}").strip().split(","))
        if len(amount) == 1:
            if value[0] != director:
                not_available.append(key)
            else:
                pass
        elif len(amount) == 2:
            for i in amount:
                if i[0] != director and i[1] != director and director not in amount:
                    not_available.append(key)
                else:
                    pass
        else:
            for i in amount:
                if i[0] != director and i[1] != director and i[2] != director and director not in amount:
                    not_available.append(key)
                else:
                    pass
    return not_available


def actors(rows, not_available):
    contents = []
    for i in rows.values():
        for x in i[4]:
            contents.append(x.split(","))
    while True:
        end = False
        for i in contents:
            for x in i:
                print(f"{x}")
        actor = input("\nPlease type the name of the actor you want to search for here:").strip().title()
        for i in contents:
            for x in i:
                if actor == x:
                    end = True
                else:
                    pass
        if end == True:
            break
        else: 
            print("That is not an available actor...")
    amount = []
    fix = []
    for key, value in rows.items():
        for i in value[4]:
            fix.append((i).split(","))
            for x in fix:
                for z in x:
                    amount.append(z)
        
        if len(amount) == 1:
           
            if amount != actor and actor not in amount:
                not_available.append(key)
            else:
                pass
        elif len(amount) == 2:
            if amount[0] != actor and amount[1] != actor and actor not in amount:
                not_available.append(key)
            else:
                pass
        else:
            x = 0
            for i in amount:
                if i == actor:
                    x += 1
                else:
                    pass
            if x < 1:
                not_available.append(key)
            else:
                pass
    return not_available

def lengths(rows,not_available):
    while True:
        min = input("What would you like to be the minimum amount of time time? (Numbers only):").strip()
        max = input("What would you like to be the max amount of time? (Numbers only):").strip()
        if min.isdigit() == True and max.isdigit() == True:
            min = int(min)
            max = int(max)
            if min < max:
                break
            else:
                print("The minimum time must be less than the max...")
        else:
            print("Please put only numbers...")
    for key,value in rows.items():
        if value[4] < min or value[4] > max:
            not_available.append(key)
        else:
            pass
def combine(rows):
    not_available = []
    pass

def pretty():
    pass



def main(rows):
    print("Hey, this is a movie recommendation program that can tell you the length , title, year, genre, and more!!!")




rows = paser()
test = actors(rows, [])
print(test)


#Set the end values to a set so then they can't have duplacites