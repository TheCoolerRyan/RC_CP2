#RC 1st, movie recommender
import csv

#create somethingt to put the movie lists into a dictoinary
def sort():
    #Use try and except
    try:
        with open("Individual_projects/movies_list.csv", mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = {}
            for line in content:
                rows[line[0]] =  [line[1],line[2],line[3],int(line[4]),list[line[5]]]

    except:
        print("We can't find the csv")

    else:
        for key,value in rows.items():
            print(f"{key}: {value}")


#Create function that will look at the selected filters, and combine there requirements





#Create the main function
def main(rows):
    print("Hey, this is a movie recommendation program that can tell you the length , title, year, genre, and more!!!")




sort()