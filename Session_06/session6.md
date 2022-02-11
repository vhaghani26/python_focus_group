# Session 6: Lab - Numeric Types, Type Casting, and Expressions

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2022-02-11

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Data Types in Python

Last week, we started learning about text types and how to manipulate text types. This week, we will continue diving into more Python data types.

### Numeric Types (Integers, Floats, and Complexes)

Numeric types are data types containing numbers. Let's make a new file called `numeric_types.py` in a `session_06/` directory. Use your text editor to edit the file.

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

## Setting the Specific Data Type (AKA Type Casting)

Create a new file called `type_casting.py`. Most times that you assign a Python variable with some type of data, Python is able to assign a data type to that variable. In some instances, there may be incompatibilities (which result in the type error I mentioned earlier) that require manual fixes. For example, consider the following:

```
#!/usr/bin/env python3

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

## Python Expressions

Now that you've learned about numeric types, we'll learn what we can do with numeric types! Doing math in Python requires special syntax so that the correct mathematical operations are carried out. Here is a table of the different operations that can be used in Python (including the type casting data previously discussed):

| Operation | Result | 
|-----------|--------|
| `x + y` | sum of x and y |
| `x - y` | difference of x and y |
| `x * y` | product of x and y |
| `x / y` | quotient of x and y |
| `x // y` | floored quotient of x and y |
| `x % y` | remainder of `x/y` |
| `-x` | x negated |
| `+x` | x unchanged |
| `abs(x)` | absolute value or magnitude of x |
| `int(x)` | x converted to integer |
| `float(x)` | x converted to float |
| `complex(re, im)` | a complex number with real part *re*, imaginary part *im* (defaults to 0) |
| `c.conjugate()` | conjugate to the complex number c |
| `divmod(x, y)` | the pair `(x // y, x % y)` |
| `pow(x, y)` | x to the power y |
| `x ** y` | x to the power y |

There are also more complicated operations that we will not cover here. You can take a look at [this](https://docs.python.org/3/library/stdtypes.html) to read more if you are interested.

Now we'll take a look at how to use these operations. Make a new file called `expressions.py` for this topic.

```
#!/usr/bin/env python3

# Set miscellaneous variables to use in expressions
a = 10
b = 5
c = 3
d = -19
e = 2


# Find the sum of a and b (use f-string formatting)
print(f'The sum of {a} and {b} is {a + b}')
```

```
# Find the difference between a and b
print(f'The difference between {a} and {b} is {a - b}')
```

```
# Find the product of a and b
print(f'The product of {a} and {b} is {a * b}')
```

```
# Find the quotient of a and b (a divided by b)
print(f'The quotient of {a} and {b} is {a/b}')
```

```
# Find the floored quotient of a and c (drops remainder)
print(f'The floored quotient of {a} and {c} is {a//c}')
```

```
# Find the remainder of a divided by c
# This is referred to as the modulo
print(f'The remainder of {a} divided by {c} is {a % c}')
```

```
# Find negative d
print(f'When we negate {d}, we get {-d}')
```

```
# Find the absolute value of d
print(f'The absolute value of {d} is {abs(d)}')
```

```
# Raise a to the power of c
print(f'{a} to the power of {c} is {pow(a,c)}')
```

```
# Try another way to raise a to the power of c
print(f'{a} to the power of {c} is {a ** c}')
```

Python also follows the standard order of operations (PEMDAS). We can observe when we make more complicated expressions:

```
exp1 = a * e + d
print(exp1)

exp2 = a * (e + d)
print(exp2)

exp3 = a ** e + d - b * c
print(exp3)

# Math example
total_min = 43 + 42 + 57
total_hr = total_min/60
print(total_hr)
```

Notice that depending on your preference, you can assign Python code snippets to variables and print them directly or print them within the `print()` function. I alternate between the two depending on the complexity of the code I'm writing and whether or not I want any string formatting/string interpolation. 

You can also do math and assignment at the same time. This becomes more helpful in loops (which we will learn in a future session). This is a shorthand notation that we can use. First, you initiate some variable with a value (typically 0, but depends on the case). Then, you use the initiated variable and carry out some manipulation that uses the previous variable value. Then, this new value overwrites the variable value. This is like a baby version of recursive functions, which essentially just means the previous value is required to compute the new value.

```
# Practice simultaneous math and assignment
i = 0
i = i + 1 # fully written out
print(i)

i = 0
i += 1 # shorthand notation
print(i)
```

# Complex Math Operations and First Module Import

Make a new file called `complex_math.py` or keep going in `expressions.py`. It's ultimately your preference, but I'd recommend starting a new file since we will import a module for the first time. 

A module refers to some Python file containing statements, definitions, functions, etc. It's code that someone else has written and made available for public use. Many modules are already included with a Python installation, but on occasion, you will have to install it yourself. For complex math operations, it is helpful to import the module `math`, which should already be installed. Let's try importing the module!

```
#!/usr/bin/env python3

import math
```

Run this to ensure that the module is able to load. For module loading, Python uses the convention `import {module}`. These statements typically go at the beginning of the script, which is why I recommended starting a new file. Furthermore, when using a module, you usually call a function/aspect like so: `module_name.function`. Let's implement some other math functions now.

```
# Use square root for Pythagorean theorem
a = 3
b = 4

hyp = math.sqrt(a**2 + b**2)
print(hyp)

# Use log2
print(math.log2(0.25))

# Use pi
print(math.pi)

# Use Euler's number
print(math.e)

# Use infinity 
print(math.inf)

# Use factorial
print(math.factorial(a))
```

If you're ever doing more complicated math than this, many times there will be modules or libraries available for install. Remember Google (or your preferred search engine) is your friend for bioinformatics!

## Exit Ticket

Update your `README.md` and Git push all your work from this session. Try pushing changes for files individually so you can customize comments.

Congratulations, you finished Session 6! 