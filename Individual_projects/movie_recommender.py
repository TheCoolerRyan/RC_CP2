#RC 1st, movie recommender
import csv

#create somethingt to put the movie lists into a dictoinary
def paser():
    #Use try and except
    try:
        with open("Individual_projects/movies_list.csv", mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = {}
            for line in content:
                rows[line[0]] =  [line[1],line[2],line[3],int(line[4]),list[line[5]]]

    except:
        print("We can't find the csv file")

    else:
        for key,value in rows.items():
            print(f"{key}: {value}")

#Create function for genre
def genres(rows,genre, not_available):
    for key, value in rows.items():
        amount = list(f"{value[2]}").split("/")
        if (amount).length() == 1:
            if value[2] != genre:
                not_available.append(key)
            else:
                pass
        else:
            for i,x in amount:
                if i != genre and x != genre:
                    not_available.append(key)
                else:
                    pass
    return not_available


#Create function for director
def directors(rows, director,not_available):
    for key, value in rows.items():
        amount = list((f"{value[1]}").split(",").strip())
        if (amount).length() == 1:
            if value[1] != director:
                not_available.append(key)
            else:
                pass
        elif (amount).length() == 2:
            for i,x in amount:
                if i != director and x != director:
                    not_available.append(key)
                else:
                    pass
        else:
            for i,x,z in amount:
                if i != director and x != director and z != director:
                    not_available.append(key)
                else:
                    pass
    return not_available

#Create function for actor 
def actors(rows,actor, not_available):
    for key, value in rows.items():
        amount = list((f"{value[5]}").split(",").strip())
        if (amount).length() == 1:
            if value[5] != actor:
                not_available.append(key)
            else:
                pass
        elif (amount).length() == 2:
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
#Create function for length
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
#Create function that will look at the selected filters, and combine there requirements
def combine(rows):
    not_available = []
    pass
#Pretty print function




#Create the main function
def main(rows):
    print("Hey, this is a movie recommendation program that can tell you the length , title, year, genre, and more!!!")




paser()