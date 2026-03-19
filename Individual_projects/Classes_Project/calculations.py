#Ryan Crop 1st, Calculations for Classes Project.
import csv
# Shape classes
class Circle:
    #Grabe radius
    def __init__(self, radius):
        self.radius = radius if radius > 0 else None
    #grab the are
    def area(self):
        if self.radius:
            return round(3.14159 * self.radius ** 2, 2)
        return None
    #Take the raidus and grab the perimeter
    def perimeter(self):
        if self.radius:
            return round(2 * 3.14159 * self.radius, 2)
        return None
    #Create the needed formula
    def formula(self):
        return "Area: π * radius^2, Perimeter: 2 * π * radius"
    #Printing off all of the stats for the shape
    def display_info(self):
        if self.radius:
            return f"Circle: Radius = {self.radius}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Radius must be positive"


class Rectangle:
    #Create the values of the length and width through init
    def __init__(self, length, width):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None
    #Grab the area using values
    def area(self):
        if self.length and self.width:
            return round(self.length * self.width, 2)
        return None
    #Grab the perimeter using length and width
    def perimeter(self):
        if self.length and self.width:
            return round(2 * (self.length + self.width), 2)
        return None
    #Create the string of the formula so its saved
    def formula(self):
        return "Area: length * width, Perimeter: 2 * (length + width)"
    #Plug in all information and put it into a string
    def display_info(self):
        if self.length and self.width:
            return f"Rectangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Length and width must be positive"


class Square:
    #Create the base values that will be used throughout the functions
    def __init__(self, side):
        self.length = side if side > 0 else None
        self.width = side if side > 0 else None
    #Get the area for later use
    def area(self):
        if self.length and self.width:
            return round(self.length * self.width, 2)
        return None
    #Grab the perimeter using length and width
    def perimeter(self):
        if self.length and self.width:
            return round(4 * self.length, 2)
        return None
    #Create a string of the formula for user options
    def formula(self):
        return "Area: side^2, Perimeter: 4 * side"
    #Grab all of the values and put them into a string for when you print all of them off
    def display_info(self):
        if self.length and self.width:
            return f"Square: Side = {self.length}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Side length must be positive"


class Triangle:
    #Grab the values of its length and width and get the location
    def __init__(self, length, width):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None
    #Plug in its values to get its area
    def area(self):
        if self.length and self.width:
            return round(0.5 * self.length * self.width, 2)
        return None
    #Create a string version of its formulas to print of later
    def formula(self):
        return "Area: 0.5 * length * width"
    #Plug in all of the needed values for when it gets printed of
    def display_info(self):
        if self.length and self.width:
            return f"Triangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}"
        return "Length and width must be positive"


# 3d shape classes
class Sphere:
    #Grab the location and take asign the needed values
    def __init__(self, radius):
        self.radius = radius if radius > 0 else None
    #Take in the radius and use it to calculate the voluem
    def volume(self):
        if self.radius:
            return round((4 / 3) * 3.14159 * self.radius ** 3, 2)
        return None
    #Take in the radius to find the needed surface area
    def surface_area(self):
        if self.radius:
            return round(4 * 3.14159 * self.radius ** 2, 2)
        return None
    #Create a string version of its formulas to print of later
    def formula(self):
        return "Volume: (4/3) * π * radius^3, Surface Area: 4 * π * radius^2"
    #Plug in all of the needed values for when it gets printed of
    def display_info(self):
        if self.radius:
            return f"Sphere: Radius = {self.radius}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Radius must be positive"


class Cube:
    #Grab the location and take asign the needed values
    def __init__(self, side):
        self.side = side if side > 0 else None
    #Find out the volume using its side values
    def volume(self):
        if self.side:
            return round(self.side ** 3, 2)
        return None
    #Find out the surface area using its sides
    def surface_area(self):
        if self.side:
            return round(6 * (self.side ** 2), 2)
        return None
    #Create a string version of its formulas to print of later
    def formula(self):
        return "Volume: side^3, Surface Area: 6 * side^2"
    #Plug in all of the needed values for when it gets printed of
    def display_info(self):
        if self.side:
            return f"Cube: Side = {self.side}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Side length must be positive"


class Cuboid:
    #Grab the location and take asign the needed values
    def __init__(self, length, width, height):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None
        self.height = height if height > 0 else None
    #Grab the volume using its length width and height
    def volume(self):
        if self.length and self.width and self.height:
            return round(self.length * self.width * self.height, 2)
        return None
    #Figure out the surface area using legnt width and height
    def surface_area(self):
        if self.length and self.width and self.height:
            return round(2 * (self.length * self.width + self.length * self.height + self.width * self.height), 2)
        return None
    #Create a string version of its formulas to print of later
    def formula(self):
        return "Volume: length * width * height, Surface Area: 2 * (lw + lh + wh)"
    #Plug in all of the needed values for when it gets printed of
    def display_info(self):
        if self.length and self.width and self.height:
            return f"Cuboid: Length = {self.length}, Width = {self.width}, Height = {self.height}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Dimensions must be positive"


class Cylinder:
    #Grab the location and take asign the needed values
    def __init__(self, radius, height):
        self.radius = radius if radius > 0 else None
        self.height = height if height > 0 else None
    #Find the volume using radius and height
    def volume(self):
        if self.radius and self.height:
            return round(3.14159 * self.radius ** 2 * self.height, 2)
        return None
    #Find the surface are using radius and height
    def surface_area(self):
        if self.radius and self.height:
            return round(2 * 3.14159 * self.radius * (self.radius + self.height), 2)
        return None
    #Create a string version of its formulas to print of later
    def formula(self):
        return "Volume: π * radius^2 * height, Surface Area: 2 * π * radius * (radius + height)"
    #Plug in all of the needed values for when it gets printed of
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
            return (num)
        else:
            return False
    else:
        return False
    


