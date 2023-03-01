#######################################################################
#    DAY 18 : ___Turtle and Graphical User Interface (GUI)___
#######################################################################

import random
from turtle import Turtle, Screen

timmy = Turtle()

# Using the class attributes to customize our turtle
timmy.shape('turtle')
timmy.color("DarkBlue", "DeepSkyBlue")


# ---------------------------------------------------
# TURTLE CHALLENGE 1: Draw a Square
#

def turtle_draws_square(turtle, side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


# turtle_draws_square(timmy, 100)


# ---------------------------------------------------
# TURTLE CHALLENGE 2: Draw a Dashed Line
#

def turtle_draws_dashed_line(turtle, iterations, len_of_segments=10):
    for i in range(iterations):
        turtle.forward(len_of_segments)
        turtle.penup()
        turtle.forward(len_of_segments)
        turtle.pendown()


# turtle_draws_dashed_line(timmy, 10)


# ---------------------------------------------------
# TURTLE CHALLENGE 3: Drawing Different Shapes
#

"""
Shapes to draw...
    - triangle -> square -> pentagon -> hexagon -> heptagon -> octagon -> nonagon -> decagon

AC: 
    - each shape must be the a random color
    - each of the sides length=100
    - all shapes drawn in sequence 
"""
shapes = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10
}

colors = ["black", "deep sky blue", "dark green", "red", "purple", "salmon", "goldenrod", "dark grey"]


def turtle_draws_shapes(turtle, shapes_dict, colors, side_length=100):
    for shape in shapes_dict:
        # Changing pen color for each shape
        rand_color = random.choice(colors)
        turtle.pencolor(rand_color)

        # determining angle of shape
        num_of_sides = shapes[shape]
        angle = 360 / num_of_sides

        # Drawing the shape
        for i in range(num_of_sides):
            turtle.forward(side_length)
            turtle.left(angle)


# turtle_draws_shapes(timmy, shapes, colors)


# ---------------------------------------------------
# TURTLE CHALLENGE 4: Generate Random Walk
#






screen = Screen()
screen.exitonclick()
