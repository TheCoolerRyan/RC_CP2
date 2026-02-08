#RC 1st, movie recommender
import csv

def paser():
    try:
        with open("Individual_projects/movies_list.csv", mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = {}
            for line in content:
                rows[line[0]] = [line[1],line[2],line[3],int(line[4]),list[line[5]]]

    except:
        print("We can't find the csv file")
    return rows


def genres(rows, not_available):
    contains = ["sci-fi", "adventure", "comedy", "animation", "drama", "history", "biography", "sport", "family", "romance",]
    print("Available genres ->")
    for i in contains:
        print((i).title())
    while True:
        genre = input("\nWhat genre would you like to search for:").strip().lower()
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


def actors(rows,actor, not_available):
    for key, value in rows.items():
        amount = list((f"{value[5]}").split(",").strip())
        if len(amount) == 1:
            if value[5] != actor:
                not_available.append(key)
            else:
                pass
        elif len(amount) == 2:
            for i,x in amount:
                if i != actor and x != actor:
                    not_available.append(key)
                else:
                    pass
        else:
            for i,x,z in amount:
                if i != actor and x != actor and z != actor:
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
test = genres(rows, [])
print(test)