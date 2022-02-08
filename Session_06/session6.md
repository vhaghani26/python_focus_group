# Session 6: 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2022-02-08

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Data Types in Python

Last week, we started learning about text and numeric types. This week, we will continue diving into different Python data types.

### Sequence Types (List, Tuples, Ranges)

### Mapping Types (Dictionaries)

### Set Types (Set, Frozenset)

### Boolean Types (Boolean)

### Binary Types (Bytes, Bytearray, Memoryview)

## Getting the Data Type

There may be times where it will be helpful to check your data type. This will usually be in response to some sort of type error. To do so, you can use the `type()` function. Let's make some variables containing different data types and determine the types:

```
# Create variables with different data types
type1 = "Hello World"
type2 = 3
type3 = 7.9
type4 = 1j
type5 = ["Dog", "Cat"]
type6 = ("Dog", "Cat")
type7 = range(5)
type8 = {"Name": "Viki", "Age": 23}
type9 = {"Peach", "Apple", "Strawberry"}
type10 = frozenset({"Peach", "Apple", "Strawberry"})
type11 = True
type12 = b"Hello"
type13 = bytearray(5)
type14 = memoryview(bytes(5))

# Check data types
print(type1, type(type1))
print(type2, type(type2))
print(type3, type(type3))
print(type4, type(type4))
print(type5, type(type5))
print(type6, type(type6))
print(type7, type(type7))
print(type8, type(type8))
print(type9, type(type9))
print(type10, type(type10))
print(type11, type(type11))
print(type12, type(type12))
print(type13, type(type13))
print(type14, type(type14))
```

Note that among the data types above, I've only personally had to use strings, integers, floats, lists, ranges, dictionaries, and Boolean types. Your experiences may differ, so not all of the displayed types above may be necessary, but it's helpful to be aware that they exist.

## Setting the Specific Data Type (AKA Type Casting)

Most times that you assign a Python variable with some type of data, Python is able to assign a data type to that variable. In some instances, there may be incompatibilities (which result in the type error I mentioned earlier) that require manual fixes. For example, consider the following:

```
# Assign numbers as an integer, float, and string
a = 1
b = 1.5
c = '1'
```

The variable `a` is an integer, `b` is a float, and `c` is a string (text). Well, what happens when I want to add `a` and `b`? Let's try.

```
# Demonstrate type incompatibilities
print(a + b)
```

Notice that we get an error. The types are incompatible, so you need to make `a` a float or make `b` an integer. Note that if we make `b` an integer, the transition from float to integer causes the loss of some information. In Python, instead of rounding a value up or down, everything after the decimal point gets dropped. Let's see what this looks like:

```
# Store float in d
d = 1.9
print(d, type(d))

# Convert float from d to integer and store that in e
e = int(d)
print(e, type(e))
``` 

Look at our outputs. It says that `d` is a float and `e` is an integer, meaning we succesfully converted `d` into an integer. However, when we print `e`, we see that our value is `1` instead of `2`. This shows us that the conversion Python uses to go from float to integer isn't as accurate as going from integer to float. 

Not all type conversions are compatible (e.g. `int("Hi")`). When you want to change a data type (which is called type casting), then you need to use certain functions. Here are examples of those functions for you to refer to. 

```
# Functions for type casting

# Turn the string "3" into an integer
my_int = int("3")
print(my_int, type(my_int))

# Turn the number 53 into a string
my_str = str(53)
print(my_str, type(my_str))

# Turn the integer 7 into a float
my_float = float(7)
print(my_float, type(my_float))
```

Overall, here's a summary of some of the type casting functions:

* `int()` is used to convert data into an integer
* `str()` is used to convert data into a string
* `float()` is used to convert data into a float