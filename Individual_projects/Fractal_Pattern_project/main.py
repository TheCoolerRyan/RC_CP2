#RC 1st, Fractal pattern generator

#Import turtle
import turtle
import time
from triangle_creation import *



#Create main
def main():
    x = 0
    print("This is the a program that will draw the sierpinski triangle for you!")
    while True:
        while True:
            #Ask them how many times they want to repeat it (1-5)
            num = input("Pick the depth of the sierpinski please. (1-5):").strip()
            if num.isdigit() == True and int(num) >= 1 and int(num) <= 5:
                num = int(num)
                break
            else:
                print("That is not a number 1-5...")
        #Lazy fix
        if x > 0:
            pass
        else:
            #Create turtle
            my_turtle = turtle.Turtle()
            my_turtle.speed(0)
            my_turtle.shape("turtle")
            window = turtle.Screen()
            window.title("Fractal Pattern")
            root = window.getcanvas().winfo_toplevel()
            root.deiconify()
        #Figure out the color

        #Create base points for the main triangle
        my_points = [[-200, -150], [0, 200], [200, -150]]

        #call the function to create the complex triangle and inside of it will be the draw triangle function
        sierpinski(my_points, num, my_turtle)
        turtle.hideturtle()
        exiter = turtle.Turtle()
        exiter.write("Click to exit", align="center")
        exiter.onclick(x)
        window.clearscreen()
        root.withdraw()
        #Allow them to quit or play again
        quit = input("Thank you for running my program! Would you like to quit, if you do please put quit:").strip().lower()
        if quit == "quit":
            break
        else:
            pass

        #Lazy fix
        x += 1

main()
