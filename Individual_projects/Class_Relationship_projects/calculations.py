#RC 1st, Calculations and results for students

#Import needed files
import csv
import os


# Define the Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        #Add a grade after validating it's within 0-100.
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Grade {grade} added for {self.name}.")
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def calculate_average(self):
        #Calculate the average of the student's grades.
        if not self.grades:
            return None  # No grades yet
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        #Convert numerical average to a letter grade.
        avg = self.calculate_average()
        if avg is None:
            return "N/A"
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_info(self):
        #Display student info, including grades and average.
        avg = self.calculate_average()
        avg_display = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg_display}")
        print(f"Letter Grade: {self.get_letter_grade()}")


# Define the GradeBook class
class GradeBook:
    def __init__(self):
        # Set the path relative to script location
        self.filename = os.path.join("Individual_projects", "Class_Relationship_projects", "students.csv")
        self.students = []
        self.load_from_csv()

    def add_student(self, student):
        #Add a new student to the gradebook.
        self.students.append(student)
        print(f"Student {student.name} added.")
        self.save_to_csv()

    def find_student_by_id(self, student_id):
        #Search for a student by their ID.
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_student_by_name(self, name):
        #Search for a student by their name.
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def save_to_csv(self):
        #Save all students and their grades to CSV.
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "ID", "Grades"])
            for student in self.students:
                grades_str = ",".join(map(str, student.grades))
                writer.writerow([student.name, student.student_id, grades_str])

    def load_from_csv(self):
        #Load students and grades from CSV.
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row["Name"]
                    student_id = row["ID"]
                    grades_str = row["Grades"]
                    student = Student(name, student_id)
                    if grades_str:
                        grades_list = list(map(int, grades_str.split(',')))
                        student.grades = grades_list
                    self.students.append(student)
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            pass

    def display_all_students(self):
        #Display info for all students.
        if not self.students:
            print("No students in the gradebook.")
            return
        for student in self.students:
            print("-" * 20)
            student.display_info()
            print("-" * 20)

# User Interface Functions
def display_menu():
    print("\n=== Student Grade Management System ===")
    print("1. Add a new student")
    print("2. Enter grades for a student")
    print("3. View individual student record")
    print("4. View class summary")
    print("5. Exit")