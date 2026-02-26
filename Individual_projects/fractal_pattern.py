#RC 1st, Fractal pattern generator

#Import turtle
import turtle


#Create dictionary that will create the fractal
def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()



#Create function that does the details of the sierpinski




#Create main
def main():
    #Figure out the amount of depth that they want
    #Figure out the color
    my_points = [[-200, -150], [0, 200], [200, -150]]

    #Ill call the main function to create the complex triangle and inside of it will be the draw triangle function



















#Example to work of off
import turtle
def get_mid(p1, p2):
    """Calculates the midpoint between two coordinates."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle, user_color):
    """Recursive function to draw the triangle."""
    # Draw the base triangle
    draw_triangle(points, user_color, my_turtle)
    
    if degree > 0:
        # Left triangle
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle, user_color)
        # Top triangle
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   degree-1, my_turtle, user_color)
        # Right triangle
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle, user_color)

