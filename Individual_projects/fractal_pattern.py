#RC 1st, Fractal pattern generator

#Import turtle
import turtle
import dog_inp

#Create dictionary that will create the basic triangle
def draw_triangle(points, my_turtle):
    #Create the turtle to draw the base triangle
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])

#Create a function to get the midpoing between the points
def get_mid(p1,p2):
    #return the value of them dividin of of each other
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    

#Create function that does the details of the sierpinski
def sierpinski(points, num, my_turtle):
    #Plug in the function that will create the base triangle
    draw_triangle(points,my_turtle)

    #Create the recursion
    #Create main checking to see if degree >0
    if num > 0:
        #Go through each section and do recursion for each triangle
        # Left triangle
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   num-1, my_turtle)
        # Top triangle
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   num-1, my_turtle)
        # Right triangle
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   num-1, my_turtle)


#Create main
def main():

    #Ask them how many times they want to repeat it (1-5)
    num = dog_inp.menu([1,2,3,4,5])
    num = num.get("index")
    #Create stuff for turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    window = turtle.Screen()
    window.title("Fractal Pattern")
    #Figure out the color

    #Create base points for the main triangle

    my_points = [[-200, -150], [0, 200], [200, -150]]
    #call the function to create the complex triangle and inside of it will be the draw triangle function
    sierpinski(my_points, num, my_turtle)


main()