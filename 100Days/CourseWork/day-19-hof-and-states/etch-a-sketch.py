from turtle import Turtle, Screen

"""
GOAL: 
    - Create an Etch-A-Sketch using Higher Order Functions. 

Controls: 
    - 'W' - Forwards
    - 'S' - Backwards
    - 'A' - Counterclockwise
    - 'D' - Clockwise
    - 'C' - Clear Drawing
"""

cursor = Turtle()
screen = Screen()


# Controls
def move_forwards():
    cursor.forward(15)


def move_back():
    cursor.back(15)


def counterclockwise():
    cursor.left(15)


def clockwise():
    cursor.right(15)


# Calling upon the event listener
screen.listen()

# Using higher order functions here
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="a", fun=counterclockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=cursor.reset)

screen.exitonclick()
