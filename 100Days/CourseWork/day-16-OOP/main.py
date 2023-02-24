# ----------------------------------------------------------------------------------------------------
# Simple Example of a Class : `turtle`
#

# from turtle import Turtle, Screen
"""
FIRST,
    I want to go into the turtle library we just imported, and extract a Turtle Class to create a new turtle object.

Below, we can see that we created a new object, called `timmy`
One way we couldve created timmy is with...
    - `timmy = turtle.Turtle()`
        - timmy : new object
        - turtle. : taps into the turtle module/library
        - Turtle() : a class within turtle (NOTE: the parenthesis initialize the class)

Instead, we'll simplify the procedure, as you see in the code...
"""

# # Creating object
# timmy = Turtle()
# # Using a method to change the shape of our object on the screen
# timmy.shape("turtle")
# # Using another method to change the color of our object on the screen
# timmy.color("DarkBlue", "DeepSkyBlue")
# # Moving the turtle foward by 100 paces
# timmy.forward(100)

# my_screen = Screen()
# # Using one of the object's attributes
# my_screen.canvheight

# Now lets call upon a method...
#       This method will allow us to click out of the screen created above
#
# my_screen.exitonclick()


# ---------------------------------------------------------------------------------------------------------
# `prettytable` Class
#

from prettytable import PrettyTable

poke_table = PrettyTable()
# Using an attribute to change style of the table.
# poke_table.align = "l"

# TASK : print a Pokemon table by column
poke_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
poke_table.add_column("Type", ["Electric", "Water", "Fire"])

