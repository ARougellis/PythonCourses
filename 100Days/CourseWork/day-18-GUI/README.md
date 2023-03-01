# Turtle Module and Graphical User Interface

## Course Notes

### I. Different ways of Importing Modules

#### i. Basic Imports
1. `import <module>`   
- In order to use a class, you must call upon the module then the class, like so...
`turtle.Turtle()`
2. `from <module> import <class>`  
- easier way of calling upon class like so...  
`from turtle import Turtle`

#### ii. Aliasing Modules
Sometimes names of modules are a bit long and annoying to tpe everytime you want to use it.
In these cases you can use an _alias_. i.e...  
`import turtles as t`  
Then you call upon that modules like...  
`t.Turtle()`

#### iii. Installing Modules
Sometimes you need to download modules that dont come with the python standard language library. 
For this, we use `pip install`. 

### II. Tuples

**Tuples** are very similar to list, but instead of square brackets `[]`, tuples use parenthesis `()` as seen below...  
`example_tuple = (1, 3, 8)`  
You can access any element in a tuple the same way you would a list...  
`example_tuple[1] = 3`  

So, _what's the difference between lists and tuples_????  
    Tuple vales are set in stone, or **Immutable**. You cannot modify any elements in a tuple and you cannot add/remove elements.  
