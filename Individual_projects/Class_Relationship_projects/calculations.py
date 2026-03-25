#RC 1st, calculator for gradebook
import csv

#Create a gradbook class that will manage all students
    #Run the init function (Grab students)



#Create a student class that will create the students
class Student:
    #Run the init function (Grabbing for Name and ID)
    def __init__(self, name, id):
        self.name = name
        self.id = id

    #Create the string function to return a sentance
    def __str__(self):
        return f"Student added succesfully\nName: {self.name}\nID: {self.id}\nGrades: None Yet"







##################TEST##TEST##TEST################
my_list = [['Name', 'ID', 'Grades'], ['John Doe', '136748', [2,5,3]]]

with open('P:\Crop, Ryan\RC_CP2\Individual_projects\Class_Relationship_projects\students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(my_list)