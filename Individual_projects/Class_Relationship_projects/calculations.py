#RC 1st, calculator for gradebook
import csv
import ast


#Create a gradbook class that will manage all students
class Gradebook:
    #Run the init function (Grab students)
    def __init__(self,  students = []):
        self.students = students

    def create_student(self):
        while True:
            x = 0
            name = input("\nPlease tell me your name:").strip().title()
            for i in self.students:
                if i["Name"] == name:
                    x += 1
                else:
                    pass
            if x == 0:
                break
            else:
                print("That name has already been taken...\n")
        while True:
            id = input("\nPlease inter your ID:").strip()
            if id.isdigit() == True:
                break
            else:
                print("Please only enter in numbers...")


        #TRY ADDING SELF TO THE ITEMS
        self.students.append(Student(name, id, grades= []))
        print()

#Create a student class that will create the students
class Student:
    #Run the init function (Grabbing for Name and ID)
    def __init__(self, name, id, grades = []):
        self.name = name
        self.id = id
        self.grades = grades

    #Create the string function to return a sentance
    def __str__(self):
        if not self.grades:
            grade = "None"
        else:
            grade = self.grades
        return f"Student added succesfully\nName: {self.name}\nID: {self.id}\nGrades: {grade}"







#This is how i will read and write to the csv
students_data = [['Name', 'ID', 'Grades'], ['John Doe', '136748', [2,5,3]]]

with open('P:\Crop, Ryan\RC_CP2\Individual_projects\Class_Relationship_projects\students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(students_data)


# The file path you provided
file_path = r'P:/Crop, Ryan/RC_CP2/Individual_projects/Class_Relationship_projects/students.csv'

students_data = []

with open(file_path, 'r', newline='') as f:
    # DictReader uses the first row (Name, ID, Grades) as keys
    reader = csv.DictReader(f)
    
    for row in reader:
        # Convert the 'Grades' string back into a list object
        row['Grades'] = ast.literal_eval(row['Grades'])
        students_data.append(dict(row))

# Output: [{'Name': 'John Doe', 'ID': '136748', 'Grades': [2, 5, 3]}]
print(students_data)

gradebook= Gradebook(students_data)
gradebook.create_student(students_data)
