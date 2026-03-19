#Ryan Crop 1st, Classes Project (Calculator)
#Import calculations to use its functions
from calculations import *
# User Interface
def main():
    print("\nGeometry Calculator:")

    shapes = []
    
    while True:
        #CREATE A BUNCH OF MEASUREMENT VALUES THAT WILL BE SET TO ZERO EACH TIME
        #Show them what they can do
        print("\n1. Create a Circle")
        print("2. Create a Rectangle")
        print("3. Create a Square")
        print("4. Create a Triangle")
        print("5. Create a Sphere")
        print("6. Create a Cube")
        print("7. Create a Cuboid")
        print("8. Create a Cylinder")
        print("9. View All Shapes")
        print("10. Compare Shapes")
        print("11. View Shape Formulas")
        print("12. Exit")
        choice = input("Enter your choice: ")
        #Spacer
        print("\n\n")   
        #Create the value to check for the circle values
        if choice == "1":
             
            while True:
                radius = proffing((input("Enter the radius of the circle: ")))
                if radius != False:
                    break
                else:
                    print("Please enter a valid number")
            #Plug in circle values to the class
            shapes.append(Circle(radius))

        #Create the value to check for the rectangle values
        elif choice == "2":
            
            while True:
                length = proffing((input("Enter the length of the rectangle: ")))
                width = proffing((input("Enter the width of the rectangle: ")))
                if width != False and length != False:
                    break
                else:
                    print("Please enter a valid number")
                    #Plug in rectangle values to the class
            shapes.append(Rectangle(length, width))

        #Create the value to check for the Sqaure values
        elif choice == "3":
             
            while True:
                side = proffing((input("Enter the side length of the square: ")))
                if side != False:
                    break
                else:
                    print("Please enter a valid number")
            #Plug in sqaure values to the class
            shapes.append(Square(side))

        #Create the value to check for the Triangle values
        elif choice == "4":
             
            while True:
                length = proffing((input("Enter the length of the triangle: ")))
                width = proffing((input("Enter the width of the triangle: ")))
                if length != False and width != False:
                    break
                else:
                    print("Please enter a valid number")
            #Plug in the triangle values to the class
            shapes.append(Triangle(length, width))

        #Create the value to check for the Sphere values
        elif choice == "5":
             
            while True:
                radius = proffing((input("Enter the radius of the sphere: ")))
                if radius != False:
                    break
                else:
                    print("Please enter a valid input")
            #Plug in the sphere values to the class
            shapes.append(Sphere(radius))

        #Create the value to check for the cube values
        elif choice == "6":
             
            while True:
                side = proffing((input("Enter the side length of the cube: ")))
                if side != False:
                    break
                else:
                    print("Please enter a valid number")
            #Plug in the cube values to the class
            shapes.append(Cube(side))

        #Create the value to check for the cuboid values
        elif choice == "7":
             
            while True:
                length = proffing((input("Enter the length of the cuboid: ")))
                width = proffing((input("Enter the width of the cuboid: ")))
                height = proffing((input("Enter the height of the cuboid: ")))
                if length != False and width != False and height != False:
                    break
                else:
                    print("Please enter a valid number")
            #Plug in the vales to the class
            shapes.append(Cuboid(length, width, height))

        #Create the value to check for the cylinder values
        elif choice == "8":
             
            while True:
                radius = proffing((input("Enter the radius of the cylinder: ")))
                height = proffing((input("Enter the height of the cylinder: ")))
                if radius != False and height != False:
                    break
                else:
                    print("Please enter a valid number")
            #Plug in the values to the class for the calculation
            shapes.append(Cylinder(radius, height))

        #Allow for the to see all of the created shapes
        elif choice == "9":
            #Check to see that there are shapes, if there are then print them off
            if not shapes:
                print("No shapes created yet")
            else:
                for i, shape in enumerate(shapes, 1):
                    print(f"{i}. {shape.display_info()}")

        #Start the comparing process
        elif choice == "10":
            #Check to see if they have two shapes
            if len(shapes) < 2:
                print("You need at least two shapes are needed to compare")
            #Print of all of the shapes
            number = 0
            for shape in shapes:
                number += 1
                print(f"\n{number}. {shape.display_info()}")
            #Get the correct numbers and then compare there area and diameters
            else:
                print("\n")
                while True:
                    idx1 = int(input("Enter the number of the first shape: ")) - 1
                    idx2 = int(input("Enter the number of the second shape: ")) - 1
                    if idx1 >=0 and idx1 <= number and idx2 >= 0 and idx2 <= number:
                        break
                    else:
                        print("Please enter a valid number")
                shape1 = shapes[idx1]
                shape2 = shapes[idx2]

                print("\nComparison Results:")
                try:
                    if shape1.area() and shape2.area():
                        if shape1.area() > shape2.area():
                            print("Shape 1 has a larger area")
                        elif shape1.area() < shape2.area():
                            print("Shape 2 has a larger area")
                        else:
                            print("Both shapes have the same area")
                except:
                    pass

                try:
                    if shape1.perimeter() and shape2.perimeter():
                        if shape1.perimeter() > shape2.perimeter():
                            print("Shape 1 has a longer perimeter")
                        elif shape1.perimeter() < shape2.perimeter():
                            print("Shape 2 has a longer perimeter")
                        else:
                            print("Both shapes have the same perimeter")
                except:
                    pass

                try:
                    if shape1.volume() and shape2.volume():
                        if shape1.volume() > shape2.volume():
                            print("Shape 1 has a larger volume")
                        elif shape1.volume() < shape2.volume():
                            print("Shape 2 has a larger volume")
                        else:
                            print("Both shapes have the same volume")
                except:
                    pass
        
        #Print of all of the functions for each shape
        elif choice == "11":
            print("\nShape Formulas:")
            print("1. Circle: " + Circle(1).formula())
            print("2. Rectangle: " + Rectangle(1, 1).formula())
            print("3. Square: " + Square(1).formula())
            print("4. Triangle: " + Triangle(1, 1).formula())
            print("5. Sphere: " + Sphere(1).formula())
            print("6. Cube: " + Cube(1).formula())
            print("7. Cuboid: " + Cuboid(1, 1, 1).formula())
            print("8. Cylinder: " + Cylinder(1, 1).formula())

        #Allow them to quit
        elif choice == "12":
            print("Goodbye")
            break
            
            #Ssaftey incase they pick a dume number
        else:
            print("Invalid input")

# runs the program
main()