# Session 6: Lab - Work with string operations

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2022-02-08

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Data Types in Python

Last week, we started learning about text types and how to manipulate text types. This week, we will continue diving into different Python data types.

### Numeric Types (Integers, Floats, and Complexes)

Numeric types are data types containing numbers. Let's make a new file called `numeric_types.py` for this section. Use your text editor to edit the file.

#### Integers

Just like we learn in math class, an integer is any whole number. We cannot have a decimal at all for Python integers, as even something like `1.0` is interpreted as a different data type. Let's take a look at some examples of integers:

```
#!/usr/bin/env python3

# Integers
int1 = 1
int2 = 9
int3 = 42
int4 = 558
int5 = 21543215
```

Python language is very delicate. This is incredibly helpful in most cases, but it also means that you have strict guidelines to adhere to. For example, `21543215` and `21,543,215` are different data types. At the end of your "Integers" section, add the following:

```
not_int = 21,543,215

print(int5, type(int5))
print(not_int, type(not_int))
```

Notice that when we add commas, it is now considered a tupple, which is a sequence and not a numeric type anymore. Therefore, if you want to use an integer or set a variable to some integer value, use ONLY numeric characters (0-9).

#### Floats

Similar to an integer, a float is a numeric type. However, floats differ in that they allow us to use decimals and fractions, so we are not limited to using whole numbers when using floats.

```
# Floats
float1 = 1.0
float2 = 3.4
float3 = 74.3
float4 = 9.99999999999
float5 = 1844384.85262
float6 = 3/4
float7 = 9/16
```

#### Complexes

In addition to handling real numbers, Python is also capable of handling complex (i.e. imaginary) numbers. I don't anticipate that you will need to use this down the line, so I'll keep it simple. It's okay if it doesn't fully make sense to you. The goal is to expose you to its existence so that if you do need it, you'll be aware of it.

Complex numbers have a real and imaginary part, which are each a float. To extract these parts from a complex number, we can use `.real` and `.imag`. Appending `j` or `J` to a numeric literal yields an imaginary number (a complex number with a zero real part) that you can add to an integer or float to get a complex number with real and imaginary parts.

```
# Complexes

# Simple Complexes
comp1 = 2J
comp2 = 7j

# Complicated Complexes

# Initialize real part
x = 5

# Initialize imaginary part
y = 3

# Convert x and y into a complex and store it in z
z = complex(x, y)

# View the real and imaginary parts:
print("The real part of the complex number is: ", z.real)
print("The imaginary part of the complex number is: ", z.imag)

# Confirm that all are complexes:
print(comp1, type(comp1))
print(comp2, type(comp2))
print(z, type(z))
```

Notice that in our output, the complex component for `z` is represented as `3j` in our output.

Sources
* https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/
* https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

We'll go ahead and take a break here and dive into some more complicated data types next week. 

## Python Expressions

https://docs.python.org/3/library/stdtypes.html

## Comparison Operations

## Simple Statistics with Lists of Numbers

Note that we will discuss lists in more detail next session










### Sequence Types (List, Tuples, Ranges)

### Mapping Types (Dictionaries)

### Set Types (Set, Frozenset)

### Boolean Types (Boolean)

A Boolean value can take two on two values: True or False.

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