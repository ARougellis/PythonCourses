import turtle

import colorgram
import random
from turtle import Turtle, Screen

# If you are running line by line in python console, use this path...
# path_to_image = 'CourseWork/day-18-GUI/creating-hirst-painting/image.jpg'
# If you are trying to run the whole script at once, use this path...
path_to_image = 'image.jpg'


def extracting_colors(path_to_image):
    rgb_colors = []
    colors = colorgram.extract(path_to_image, 32)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        formatted_color = (r, g, b)
        rgb_colors.append(formatted_color)
    del rgb_colors[0:2]

    return rgb_colors


rgb_colors = extracting_colors(path_to_image)

"""
Use the turtle module and the list of colors from image to create your own Hirst Painting. 

AC: 
    - Painting must consist of 10x10 grid of colored spots
    - Each dot is 20 units in size
    - Each dot separated by 50 units
"""

timmy = Turtle()
turtle.colormode(255)


def create_hirst_painting(turtle_name, width=10, height=10):
    turtle_name.speed('fastest')
    turtle_name.hideturtle()
    turtle_name.penup()

    x_pos = -300
    y_pos = -300

    for i in range(height):
        turtle_name.goto(x=x_pos, y=y_pos)

        for j in range(width):
            turtle_name.forward(50)
            turtle_name.dot(20, random.choice(rgb_colors))

        y_pos += 50


create_hirst_painting(timmy)

screen = Screen()
screen.exitonclick()
