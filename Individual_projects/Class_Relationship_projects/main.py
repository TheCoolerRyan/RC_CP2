from calculations import *

def main():
    #Define library
    gradebook = GradeBook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        #Ask which function they want and run the corisponding function
        if choice == '1':
            name = input("Enter student's name: ")
            student_id = input("Enter student ID: ")
            # Check if student already exists
            if gradebook.find_student_by_id(student_id):
                print("A student with that ID already exists.")
            else:
                new_student = Student(name, student_id)
                gradebook.add_student(new_student)

        elif choice == '2':
            student_id = input("Enter student ID to add grades: ")
            student = gradebook.find_student_by_id(student_id)
            if student:
                try:
                    grade_input = input("Enter grade (0-100): ")
                    grade = float(grade_input)
                    student.add_grade(grade)
                    gradebook.save_to_csv()
                except ValueError:
                    print("Invalid input. Please enter a numeric grade.")
            else:
                print("Student not found.")

        elif choice == '3':
            student_id = input("Enter student ID to view record: ")
            student = gradebook.find_student_by_id(student_id)
            if student:
                student.display_info()
            else:
                print("Student not found.")

        elif choice == '4':
            gradebook.display_all_students()

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

main()