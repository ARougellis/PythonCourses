# LIST COMPREHENSION

Previously, if we wanted to create a new list from an already existing list, it would look as follows...
```
# Say we wanted to take a list of numbers and add 1 to each element of the list
numbers = [1, 2, 3]
new_numbers = []
for num in numbers;
    new_num = num + 1
    new_numbers.append(new_num)
```
This code can be compressed with a new way of doing list comprehension. Pseudocode as follows...

`new_list = [new_item for item in old_list]`

Here's some examples... 
```
# Ex.1
#   Simplified verion of old method...
numbers = [1, 2, 3]
new_numbers = [num+1 for num in numbers]

# Outputs: 
#       [2, 3, 4]

# -------------------

# Ex.2
#   Square every elememnt in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]

# Output: 
#       [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
```

This doesn't JUST work for list of numbers. List comprehension works for **python sequences**. 
>Python Sequences include 
> - lists
> - ranges
> - strings
> - tuples
> 
Examples below...

```
# Ex.1
name = "Alex"
new_list = [letter for letter in name]

# Output:
#       ['A', 'l', 'e', 'x']

# -------------------

# Ex.2
#   Double every elememnt in a range
doubled = [num*2 for num in range(1, 5)]

# Output; 
#       [2, 4, 6, 8]
```

## Conditional List Comprehension

This is very similar to the regular ol list comprehension, but with an conditional parameter. Pseudocode as follows....

``` new_list = [new_item for item in list if condition]```

This allows us to only add elements of a list if the item meets the conditions criteria. Examples below...
```
# Ex.1
#   From a list of names, only add short names (length <= 4) to the new list
names = ['Alex', 'Nathan', 'Victor', 'Joel', 'Sam', 'Ellie', 'Chloe']
short_names = [name for name in names if len(name)<=4]

# Output: 
#       ['Alex', 'Joel', 'Sam']

# -------------------

# Ex.2
#   New list consist of only the even numbers of the old list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [num for num in numbers if num%2==0]

# Output: 
#       [2, 8, 34]
```