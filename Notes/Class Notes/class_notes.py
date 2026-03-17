#Ryan Crop 1st, Classes notes


#Example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def __str__(self):
        return f"Name = {self.name}\nSpecies = {self.species}\nAge = {self.age}"
    def birthday(self):
        self.age += 1



dog = Animal("Doug", "dog", 4)
gorilla = Animal("Whiskers", "Gorrila", 210)

"""print(dog)
print(gorilla)
dog.birthday()
print(dog)"""

# Example 2
class ClassPeriod:
    def __init__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"\nSubject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}"
    
