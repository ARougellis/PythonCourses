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

# DICTIONARY COMPREHENSION

Allows us to create a new dictionary from an already existing list or dictionary. And we can add a condition at the end 
to do a conditional dictionary comprehension. 

Simple pseudocode from **_list_** : `new_dict = {new_key:new_value for item in list}`

Simple pseudocode from **_dictionary_** : `new_dict = {new_key:new_value for (key,value) in dict.items()}`

Some examples below... 
```
# Ex.1
#   Create a dictionry from a name list ans a score list
names = ['Alex', 'Nathan', 'Victor', 'Joel', 'Sam', 'Ellie', 'Chloe']
scores_dict = {student:random.randint(1,100) for student in names}

# Output: 
#       {'Alex': 62,
         'Nathan': 14,
         'Victor': 61,
         'Joel': 41,
         'Sam': 85,
         'Ellie': 48,
         'Chloe': 76}

# -------------------

# Ex.2
#   From the newly created dictionary above, make a new dict for students who passed.
passed_students = {student:score for (student,score) in scores_dict.items() if score > 60}

# Outputs: 
#       {'Alex': 62, 'Victor': 61, 'Sam': 85, 'Chloe': 76}

# -------------------

# Ex.3
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

# Output: 
#       {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

# -------------------

# Ex.3
#       Convert a dict of celsius to dict of fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}
```

# DataFrame

## Iterate through a DataFrame

To iterate through the rows of a datafrfame... 

```
df = 
        column_1            column_2
    0   col_1_element_0     col_2_element_0
    1   col_1_element_1     col_2_element_1

for (index, rows) in df.iterrows():
    print(row)
    
# Output:
#       Name: 0,  dtyp: object
#       column_1    col_1_element_0
#       column_2    col_2_element_0
#
#       Name: 1,  dtyp: object
#       column_1    col_1_element_1
#       column_2    col_2_element_1
```

We can also get ahold of a particular value using a dot notation bc the row is a series. In addition we can also through
a condition in there...
```
df = 
        column_1            column_2
    0   col_1_element_0     col_2_element_0
    1   col_1_element_1     col_2_element_1

for (index, rows) in df.iterrows():
    if row.column_2 == "col_2_element_1"
        print(row.column_1)

# Output:
#       col_1_element_1
```