# Unlimited Arguments

## *args : Many Positional Arguments

Let's take, for example, the add function we created in the past...
```
def add(n1, n2):
    return n1 + n2
```
With that function, we are limited to only 2 numbers as inputs. But what if we wanted to add more than 2 numbers?

Any arguments prefixed with a `*` will allow any number of arguments to be used as the input.
```
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
```
Now we can pass as many arguments as we want nto the function above. Like `add(3, 5, 9, 4, 1, ...)`


## **kwargs : Many Keyword Arguments

This method basically uses dictionary as an input. 

As an example, lets create a calculator...

```
def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    
# Input:
caluclator(2, add=3, multiply=5)

# Output:
#       25
```
