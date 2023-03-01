#######################################################################
#    DAY 18 : ___Turtle and Graphical User Interface (GUI)___
#######################################################################

import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)

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


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)

    return color_tuple


def turtle_draws_shapes(turtle_name, shapes_dict, side_length=100):
    for shape in shapes_dict:
        # Changing pen color for each shape
        turtle_name.pencolor(random_color())

        # determining angle of shape
        num_of_sides = shapes[shape]
        angle = 360 / num_of_sides

        # Drawing the shape
        for i in range(num_of_sides):
            turtle_name.forward(side_length)
            turtle_name.left(angle)


# turtle_draws_shapes(timmy, shapes)


# ---------------------------------------------------
# TURTLE CHALLENGE 4: Generate Random Walk
#

"""
AC:
    1. Generate a random walking path/ line drawn by turtle     [ ]
    2. Increase thickness of lines drawn                        [x]
    3. Every segment of line should be same length              [ ]
    4. Each Segment should be a different color                 [x]
            - using `colors` dictionary from TURTLE CHALLENGE #3
    5. Speed up drawing process                                 [x]
"""


def random_walk(turtle_name, number_of_segments=200, segment_length=25):
    timmy.pensize(7)
    timmy.speed('fast')

    move = ["forwards", "backwards"]
    direction = [0, 90, 180, 270]

    for i in range(number_of_segments):
        turtle_name.pencolor(random_color())
        turtle_name.setheading(random.choice(direction))
        movement_direction = random.choice(move)
        if movement_direction == "forwards":
            turtle_name.forward(segment_length)
        elif movement_direction == "backwards":
            turtle_name.back(segment_length)


# random_walk(timmy)


# ---------------------------------------------------
# TURTLE CHALLENGE 5: Draw a Spirograph
#


def turtle_draws_spirograph(turtle_name, angle):
    turtle_name.speed('fastest')
    for i in range(int(360/angle)):
        turtle_name.pencolor(random_color())
        turtle_name.left(angle)
        turtle_name.circle(100)


turtle_draws_spirograph(timmy, 5)


screen = Screen()
screen.exitonclick()
