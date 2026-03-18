#Ryan Crop 1st, Calculations for Classes Project.
import csv
# Shape classes
class Circle:
    def __init__(self, radius):
        self.radius = radius if radius > 0 else None

    def area(self):
        if self.radius:
            return round(3.14159 * self.radius ** 2, 2)
        return None

    def perimeter(self):
        if self.radius:
            return round(2 * 3.14159 * self.radius, 2)
        return None

    def formula(self):
        return "Area: π * radius^2, Perimeter: 2 * π * radius"

    def display_info(self):
        if self.radius:
            return f"Circle: Radius = {self.radius}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Radius must be positive"


class Rectangle:
    def __init__(self, length, width):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None

    def area(self):
        if self.length and self.width:
            return round(self.length * self.width, 2)
        return None

    def perimeter(self):
        if self.length and self.width:
            return round(2 * (self.length + self.width), 2)
        return None

    def formula(self):
        return "Area: length * width, Perimeter: 2 * (length + width)"

    def display_info(self):
        if self.length and self.width:
            return f"Rectangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Length and width must be positive"


class Square:
    def __init__(self, side):
        self.length = side if side > 0 else None
        self.width = side if side > 0 else None

    def area(self):
        if self.length and self.width:
            return round(self.length * self.width, 2)
        return None

    def perimeter(self):
        if self.length and self.width:
            return round(4 * self.length, 2)
        return None

    def formula(self):
        return "Area: side^2, Perimeter: 4 * side"

    def display_info(self):
        if self.length and self.width:
            return f"Square: Side = {self.length}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Side length must be positive"


class Triangle:
    def __init__(self, length, width):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None

    def area(self):
        if self.length and self.width:
            return round(0.5 * self.length * self.width, 2)
        return None

    def formula(self):
        return "Area: 0.5 * length * width"

    def display_info(self):
        if self.length and self.width:
            return f"Triangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}"
        return "Length and width must be positive"


# 3d shape classes
class Sphere:
    def __init__(self, radius):
        self.radius = radius if radius > 0 else None

    def volume(self):
        if self.radius:
            return round((4 / 3) * 3.14159 * self.radius ** 3, 2)
        return None

    def surface_area(self):
        if self.radius:
            return round(4 * 3.14159 * self.radius ** 2, 2)
        return None

    def formula(self):
        return "Volume: (4/3) * π * radius^3, Surface Area: 4 * π * radius^2"

    def display_info(self):
        if self.radius:
            return f"Sphere: Radius = {self.radius}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Radius must be positive"


class Cube:
    def __init__(self, side):
        self.side = side if side > 0 else None

    def volume(self):
        if self.side:
            return round(self.side ** 3, 2)
        return None

    def surface_area(self):
        if self.side:
            return round(6 * (self.side ** 2), 2)
        return None

    def formula(self):
        return "Volume: side^3, Surface Area: 6 * side^2"

    def display_info(self):
        if self.side:
            return f"Cube: Side = {self.side}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Side length must be positive"


class Cuboid:
    def __init__(self, length, width, height):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None
        self.height = height if height > 0 else None

    def volume(self):
        if self.length and self.width and self.height:
            return round(self.length * self.width * self.height, 2)
        return None

    def surface_area(self):
        if self.length and self.width and self.height:
            return round(2 * (self.length * self.width + self.length * self.height + self.width * self.height), 2)
        return None

    def formula(self):
        return "Volume: length * width * height, Surface Area: 2 * (lw + lh + wh)"

    def display_info(self):
        if self.length and self.width and self.height:
            return f"Cuboid: Length = {self.length}, Width = {self.width}, Height = {self.height}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Dimensions must be positive"


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius if radius > 0 else None
        self.height = height if height > 0 else None

    def volume(self):
        if self.radius and self.height:
            return round(3.14159 * self.radius ** 2 * self.height, 2)
        return None

    def surface_area(self):
        if self.radius and self.height:
            return round(2 * 3.14159 * self.radius * (self.radius + self.height), 2)
        return None

    def formula(self):
        return "Volume: π * radius^2 * height, Surface Area: 2 * π * radius * (radius + height)"

    def display_info(self):
        if self.radius and self.height:
            return f"Cylinder: Radius = {self.radius}, Height = {self.height}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Radius and height must be positive"

#Create a stupid proffing function
def proffing(num):
    #Check to make sure its a number and its above 0
    if num.isdigit() == True:
        num = int(num)
        if num > 0:
            #Based on wether or not its above 0 return either the number or the False
            return str(num)
        else:
            return False
    else:
        return False
    


def load():
    pass

def save(shapes):
    feildnames = ["Name", "Length", "Width", "Height", "Radius"]
    with open("Individual_projects/Classes_Project/geometry_information.csv", "w", newline = "") as user_list:
        writer = csv.DictWriter(user_list, fieldnames = feildnames)
        writer.writeheader()
        for shape in shapes:
            writer.writerows(shape)

