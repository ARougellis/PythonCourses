## I. Higher Order Functions

The goal here is to call upon a function whenever a key on out keyboard is triggered. To do this, we need and __event 
listener__. This event listener "listens" to what the user does; like key commands, clicks, and key triggers.  

In order ot do this, especially with the `Turtles` module, we need _functions as inputs_.
```
def function_a(parameter):
    <do something>
    <doing something else>
    <return that>

def function_b():
    <do something>

# To pass this function as an input, only pass the name, w/o parenthesis
function_a(function_b)
```


## II. Object States and Instances
Say you wanted to create multiple objects off the same Class...
```
from turtles import Turtle

timmy = Turtle()
tommy = Turtle()
```
The objects `timmy` and `tommy` are built off the same class but operated completely separately. In other words, 
they are each a _separate instance_. These two objects can have different attributes and perform different 
methods at different times. For example...
```
#lets make timmmy green
timmy.color = 'green'
#and tommy purple
tommy.color = 'purple'
```
