# Object Oriented Programming

## Course Notes

### I. What is OOP?

Up till this point, we've been using **Procedural Programming**. 
PProgramming is when we set up procedures, or functions, that do their own particular 
things and where they build on top each other. But this comes with 
its own cons; such as ho messy this can get or how limited in complexity it can be. All in all, _PP is a one mn band, 
and we need a team_. 

Here comes OOP to simplify the relationships w/in our code and make it scalabele.  

An **object** has two properties, **attributes** and **methods**. 
- *Attributes* are a variable that's associated with a model object.
- *Methods* are functions that can be applied to said object.  

All in all, an object is a way to combining some data (attributes) and fucntionality (methods) all in the same things. 
But, we can ALSO have multiple objects from the same _"blueprint"_.
In OOP, this _blueprint_ is called a **Class**. We use _Classes_, which contains all functionality and schema etc., to create _objects_.

### II. How can we use OOP? 

#### i. Object Attributes
Objects have _attributes_, aka data it can keep track of.  

In order to access these attributes, the syntax is as follows...  
`car.speed`
- `car` : the object. 
- `speed` : the attribute
- `.` : separates the object from attribute

#### ii. Object Methods
In addition to the data an object holds (_attributes_), it also has things it can do (function). When these functions are
associated with the object is called a _method_.  

The syntax to use methods is very similar to that of attributes...  
`car.stop()`
- `car` : the object
- `stop()` : calling the function to the object.


## III. Installing Packages from PyPi

On Mac, click the 'PyCharm' tab at the very top.
1. Click 'Preferences'
2. Click 'Project: \<whatever project youre in\>'
3. Click 'Project Interpreter'
4. Click the '+' button to install packages. 
5. Search or the package
6. Install

From here, you can go about importing it normally with...  
`import <package>`


