def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, world")

greet()

@decorator
def add():
    print(1+1)

add()