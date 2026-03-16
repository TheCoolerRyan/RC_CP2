#Ryan Crop 1st, Classes Project (Calculator)
from calculations import *
# User Interface
def main():
    print("\nGeometry Calculator:")
    shapes = []
    
    while True:
        try:
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

            if choice == "1":
                radius = float(input("Enter the radius of the circle: "))
                shapes.append(Circle(radius))

            elif choice == "2":
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                shapes.append(Rectangle(length, width))

            elif choice == "3":
                side = float(input("Enter the side length of the square: "))
                shapes.append(Square(side))

            elif choice == "4":
                length = float(input("Enter the length of the triangle: "))
                width = float(input("Enter the width of the triangle: "))
                shapes.append(Triangle(length, width))

            elif choice == "5":
                radius = float(input("Enter the radius of the sphere: "))
                shapes.append(Sphere(radius))

            elif choice == "6":
                side = float(input("Enter the side length of the cube: "))
                shapes.append(Cube(side))

            elif choice == "7":
                length = float(input("Enter the length of the cuboid: "))
                width = float(input("Enter the width of the cuboid: "))
                height = float(input("Enter the height of the cuboid: "))
                shapes.append(Cuboid(length, width, height))

            elif choice == "8":
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                shapes.append(Cylinder(radius, height))

            elif choice == "9":
                if not shapes:
                    print("No shapes created yet")
                else:
                    for i, shape in enumerate(shapes, 1):
                        print(f"{i}. {shape.display_info()}")

            elif choice == "10":
                if len(shapes) < 2:
                    print("You need at least two shapes are needed to compare")
                
                number = 0
                for shape in shapes:
                    number += 1
                    print(f"\n{number}. {shape.display_info()}")

                else:
                    print("\n")
                    idx1 = int(input("Enter the number of the first shape: ")) - 1
                    idx2 = int(input("Enter the number of the second shape: ")) - 1
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

            elif choice == "12":
                print("Goodbye")
                break

            else:
                print("Invalid input")
        except:
            print("Invalid input")


# runs the program
main()