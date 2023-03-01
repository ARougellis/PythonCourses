# Turtle Module and Graphical User Interface

## Course Notes

### Different ways of Importing Modules

#### I. Basic Imports
1. `import <module>`   
- In order to use a class, you must call upon the module then the class, like so...
`turtle.Turtle()`
2. `from <module> import <class>`  
- easier way of calling upon class like so...  
`from turtle import Turtle`

#### II. Aliasing Modules
Sometimes names of modules are a bit long and annoying to tpe everytime you want to use it.
In these cases you can use an _alias_. i.e...  
`import turtles as t`  
Then you call upon that modules like...  
`t.Turtle()`

#### II. Installing Modules
Sometimes you need to download modules that dont come with the python standard language library. 
For this, we use `pip install`. 