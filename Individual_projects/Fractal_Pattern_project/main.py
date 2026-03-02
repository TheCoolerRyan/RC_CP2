#RC 1st, Fractal pattern generator

#Import turtle
import turtle
from triangle_creation import *

try:
    import dog_inp
except:
    print("Please use pip install to install dog_inp")

#Create main
def main():
    x = 0
    print("This is the a program that will draw the sierpinski triangle for you!")
    while True:
        #Ask them how many times they want to repeat it (1-5)
        input("Once you pass this point, you will pick the depth of the sierpinski. Do you acknowledge this? (Just click enter, the message will explode)\n")
        num = dog_inp.menu([1,2,3,4,5])
        num = num.get("index")
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
        if x > 0:
            my_turtle.showturtle()
        else:
            pass
        #Figure out the color

        #Create base points for the main triangle
        my_points = [[-200, -150], [0, 200], [200, -150]]

        #call the function to create the complex triangle and inside of it will be the draw triangle function
        sierpinski(my_points, num, my_turtle)
        turtle.hideturtle()
        window.exitonclick()

        #Allow them to quit or play again
        print("Thank you for running my program! What would you like to do:")
        quit = dog_inp.menu(["Quit","Run again"])
        quit = quit.get("index")
        if quit == 0:
            break
        else:
            pass

        #Lazy fix
        x += 1

main()
