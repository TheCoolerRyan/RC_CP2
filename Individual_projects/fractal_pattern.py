#RC 1st, Fractal pattern generator

#Import turtle



#Create dictionary that will create the fractal




#Create dictionary that will change colors




#Create main





#Example to work of off
import turtle

def draw_triangle(points, color, my_turtle):
    """Draws a single filled triangle."""
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

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

def main():
    # --- User Input Section ---
    print("--- Sierpinski Triangle Generator ---")
    try:
        user_depth = int(input("Enter recursion depth (e.g., 3, 4, or 5): "))
        user_color = input("Enter a color name (e.g., 'blue', 'purple', 'forestgreen'): ").lower()
    except ValueError:
        print("Invalid depth. Defaulting to 3.")
        user_depth = 3
    
    # Setup Turtle
    my_turtle = turtle.Turtle()
    my_screen = turtle.Screen()
    my_turtle.speed(0)  # 0 is the fastest speed
    
    # Define initial triangle points [x, y]
    # These coordinates center the triangle on the screen
    my_points = [[-200, -150], [0, 200], [200, -150]]
    
    # Execute
    sierpinski(my_points, user_depth, my_turtle, user_color)
    
    print("Drawing complete! Click the window to exit.")
    my_screen.exitonclick()


main()