# Session 6: Numeric and Sequence Types

By: Viktoria Haghani

Session Date: 2022-03-08

Last Updated: 2026-04-08

Session Recording: https://youtu.be/COkd1Q3uw58

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Numeric Types (Integers, Floats, and Complexes)

We spent the last two sessions learning about strings and string operations (aka text types). This week, we will begin taking a look at numeric types. Numeric types are data types containing numbers. Let's make a new file called `numeric_types.py` in a `session_06/` directory. Use your text editor to edit the file.

### Integers

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

### Floats

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

### Complexes

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

## Sequence Types (Tuples, Lists, Ranges)

### Tuples

Tuples are an ordered sequence. They are written as comma-separated elements within parenthesis. Strings, integers, and floats can be contained in a tuple. Tuples are immutable, which means we can't change them. Start by making a script named `tuples.py`.

```
#!/usr/bin/env python3

tuple1=("disco", 10, 1.2)
print(type(tuple1))
```

#### Indexing Tuples

Much like we learned for other data types, we can use indexing to access elements within each tuple. Recall that indexing in Python is 0-based, so to access the first element in the tuple, we can use the index 0.

```
# Indexing tuples
tuple1=("disco",10,1.2)
first_element = tuple1[0]
first_el_type = type(tuple1[0])
print(tuple1[0], type(tuple1[0]))
```

Previously, we have learned that we can access the last element of a data type using the -1 index. We can also count backwards beginning from -1. Let's see what that looks like!

```
# Using negative indexing
last = tuple1[-1]
second_to_last = tuple1[-2]
third_to_last = tuple1[-3]
print(f'The last element is {last}. The second to last element is {second_to_last}. The third to last (first in this case) element is {third_to_last}')
```

If we would like to know the index of an element within a tuple, we can use the `index()` function.

```
# Find element index
genres_tuple = ("pop","rock","soul","hard rock","soft rock","R&B","progressive rock","disco")
genres_tuple.index("disco")
genres_tuple.index("rock")
```

#### Slicing Tuples

If we would like multiple elements from a tuple, we can slice the tuple. This follows the standard indexing convention, including the last index having one added to it. Essentially, this is like indexing but for more than one value.

```
# Slicing tuples
tuple_to_slice = ("disco", 10, 1.2, "hard rock", 10)
print(tuple_to_slice[0:3])
```

As a quick note, we can determine the total number of elements using the `len()` function, which we learned about for strings.

```
# Determine length of tuple
print(len(tuple_to_slice))
```

#### Sorting Tuples

We can sort a tuple using the "sorted" function. The input is the original tuple and the output is a new, sorted tuple. Using the function `sorted()` will temporarily sort a tuple, but it will not change the original tuple.

```
# Use the sorted() function
Ratings = (10,9,6,5,10,8,9,6,2)
print(f'The original tuple is: {Ratings}')

RatingsSorted = sorted(Ratings)
print(f'The sorted tuple is: {RatingsSorted}. Notice that our original tuple, {Ratings} is still unsorted')
```

Notice that the output shows that the `RatingsSorted` output has brackets `[]` instead of parentheses `()`. This is because the type has changed. It has become a list (we'll cover this soon!). This is because tuples are immutable (i.e. can't be changed), so the data type needs to change for us to manipulate it. Let's verify:

```
print(type(RatingsSorted))
```

In addition to sorting numbers, we can also sort strings:

```
# Sort tuple with strings
Cars=("bmx","audi","toyota","subaru")
Cars_sorted = sorted(Cars)
print(Cars_sorted)
```

#### Concatenating Tuples

Now what if we want to add something to a tuple? Well, we can't. We can, however, concatenate tuples to create new ones.

```
# Concatenating tuples
tuple1 = ("disco", 10, 1.2)
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
```

#### Nesting Tuples

Nesting is a very important part of learning Python. It applies for several sequence data types and can be extremely helpful for a number of situations. Nesting just refers to containing a data type within a data type (specifically a sequence type). In the case of tuples, that means that it's a tuple containing a tuple in it. We can use indexing to access different elements. For indexing nested data, we use the same 0-based indexing and each nested data entry gets its own new "index array." 

```
# Work with nested tuples
nested_tuple = (1, 2, ("pop", "rock"), (3, 4), ("disco", (5, 6)))

# Access the nested tuple at index 2
print(nested_tuple[2])

# Access the first element of the nested tuple at index 2 ("pop")
print(nested_tuple[2][0])

# Access the double nested 6 at the very end of the tuple
print(nested_tuple[4][1][1])

# Access the "s" in "disco"
print(nested_tuple[4][0][2])
```

### Lists

While learning about tuples, we ran into a lot of limitations related to the fact that tuples are immutable. Lists are essentially the same thing as tuples, but they can be manipulated! Lists are ordered sequences represented with square brackets. They can contain strings, floats, integers, other lists, and even other data types. You can even make a list of data frames. Lists are one of the most powerful data types that you can use in Python, and I use lists in nearly every script I write. Although we haven't explicitly learned about lists yet, you've seen them in other sessions as examples in code. Let's make a new file called `lists.py` and learn about why lists are as magical as they are. Let's look at some examples:

```
#!/usr/bin/env python3

# Make a list
list1 = ["Viki", "Oran", "Julia", "Kelly"]
print(list1)

# Include multiple data types in a list
list2 = ["Lamp", 3, 7.2, True, (1, 2, 3)]
print(list2)
```

#### Indexing Lists

By now, you should all be fairly comfortable with the rules of indexing. Please interject if you are still not comfortable with indexing. As you've noticed, this comes up with most data types, so it's important for you to understand it. Since the conventions are the same, let's try some indexing:

```
# Index a list
print(list2[0])
print(list2[0][0])
print(list2[-1])
print(list2[4][1])
```

#### Slicing Lists

This uses the same notation as tuples.

```
# Slice list
cars = ("bmx","audi","toyota","subaru")
some_cars = cars[0:2]
print(some_cars)
```

#### Adding Elements to Lists

Depending on if you are adding one or multiple elements to a list, you can use different functions. To add one element to a list, you can use `append()`. This is one of the most commonly used list functions.

```
# Appending to a list
my_fav_artists = ["Michael Jackson", "Metallica", "Guns N Roses"]
my_fav_artists.append("Billy Idol")
print(my_fav_artists)
```

Now if we want to add multiple artists to a list, we can use the `extend()` function. Notice that the `extend()` function only takes one list as an argument.

```
# Extending a list
my_fav_artists.extend(["Journey", "Bon Jovi", "Duran Duran", "Depeche Mode"])
print(my_fav_artists)
```

You can also specify what index you'd prefer to add an element to using the `insert()` function. The first argument of `insert()` is the index you'd like to add the element to and the second argument is what you're adding to the list.

```
# Insert item at a certain index of a list
my_fav_artists.insert(0, "Prince")
print(my_fav_artists) 
```

#### Changing Elements in Lists

In order to change an element in a list, we can access the index and reset the value.

```
# Change list element
my_fav_artists[0] = "Billy Joel"
print(my_fav_artists)
```

#### Removing Elements from Lists

Removing a list element can be done using the `del()` command and the index of the element.

```
# Delete element
del(my_fav_artists[0])
print(my_fav_artists)
```

You can also remove the last item of a list using the `pop()` command. Note that the `pop()` command outputs the last element, but it removes the element from the original list. It's like cutting the value from the list and pasting it to a different variable.

```
# Remove last item in list
my_fav_artists_popped = my_fav_artists.pop()
print(my_fav_artists)

# Access popped value
print(my_fav_artists_popped)
```

I'd like to note that the list does contain my favorite artists, but the replacements and removals are not reflective of my true opinions. Sorry Billy Joel, Prince, and Depeche Mode.

#### Printing List Elements Using `*`

Sometimes, we may want to view list elements without printing it in Python list formatting. This may be helpful down the line when you interact with the command line through Python scripts. Let's see the following:

```
my_nums = [1, 2, 3, 4, 5]

print(my_nums)
print(*my_nums)
```

Notice that by preceeding the list with `*`, the format of the output has changed. 

#### Turning Strings into Lists

We can convert a string to a list using `split()`. `split()` converts every group of characters separated by a space into an element of a list.

```
my_str = "Jack and Jill went up the hill"
split_str = my_str.split()
print(split_str)
```

The split function uses a default delimiter of a space, but we can specify a different delimiter, such as a comma, by using it as an argument in the `split()` function:

```
# Split using delimiter
alph = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
split_alph = alph.split(",")
print(split_alph)
```

#### Aliasing Lists

This is very similar to aliasing files using UNIX language. You can alias a list, meaning that if you change an element in one list, it also changes the other list. You can do so using the assignment operator `=`.

```
# Alias a list
listA = [1, 2, 3, 4, 5]
listB = listA
print(f'List A is originally {listA} and List B is originally {listB}')
# Add an element to listA but don't explicitly change listB
listA.append(6)
print(f'We changed List A and now it is {listA}. Since List B reflects this change as an aliased list, List B is also {listB}.')
```

#### Cloning Lists

Once again, similar to UNIX, cloning a list means that the lists will not be linked and therefore you can work independently on either list. You use the same notation as aliasing, but put a colon in square brackets after the list name.

```
# Clone a list
listC = listA[:]

# Change listA again but not listC
listA.append(7)
print(listA)
print(listC)
```

#### Simple Statistics with Lists of Numbers

Using a list of numbers, you can perform simple statistics.

```
# Perform simple statistics
listD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find the minimum in the list
print(min(listD))

# Find the maximum in the list
print(max(listD))

# Find the sum of the list
print(sum(listD))
```

#### For-Loops

For-loops are an entire discussion on their own and they can apply to other data types, so while we won't be covering them today, I wanted to note that for-loops can be applied to lists, and this is ultimately what makes lists as powerful as they are.

#### A Last Note About Lists

There are several miscellaneous functions you can use to manipulate lists. I couldn't cover them all in one session if I tried, so my advice is that if you want to know if you can manipulate a list in a certain way, Google "how to do X to a list in Python." You'll usually get an answer! 

### Ranges

The last sequencing type is a range. The `range()` function returns a sequence of numbers. Ranges become immensely useful in for-loops (which we'll learn in a later session). For now, we'll take a quick look at what it does. Make a new file called `ranges.py`.

```
#!/usr/bin/env python3

# Turn our range into a list
numbers = list(range(1,6))
print(numbers)
```

Let's take a look at our output more closely. Notice that our list starts with "1" and ends with "5." This is the same behavior we notice with indexing; our last digit has an off-by-one behavior. This means we have to add one to the last digit to get the range we want. For example, if we want the numbers 1-20 in a list, we have to use the following:

```
# Turn our range into a list containing numbers 1-20
range1_20 = list(range(1,21))
print(range1_20)
```

We can also tell Python to skip numbers in a given range. This is very similar in notation to the strides we learned about when we learned about strings. Essentially, the notation is `(first number in range, last number in range + 1, every Xth value you want)`. Now let's put this in action. Let's try to view all even numbers in the range 1 through 10.

```
# Even numbers from 1-10
even_numbers=list(range(2,11,2))
print(even_numbers)
```

If we look more closely at the information in the range function, we see that we start at 2. Why not 1? This is because adding a value to skip other values accounts for the first value already. This command is basically us saying "Starting at 2 and ending at 11, skip every 2nd number." In this case, beginning our range with 1 means that our second element, 2, would be skipped instead. Be mindful of how indexes and ranges work, as they're not as intuitive as they sound.