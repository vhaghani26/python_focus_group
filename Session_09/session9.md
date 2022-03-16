# Session 9:

By: Viktoria Haghani

Session Date: TBD
Last Updated: 2021-12-16

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

### Mapping Types (Dictionaries)

### Set Types (Set, Frozenset)

Sets are a type of collection. This means that like lists and tuples, you can input different Python data types. Unlike lists and tuples, sets are unordered, meaning that sets do not record element position. For us, this means we cannot index sets, which ends up making them less useful than lists (in my opinion). To define a set, you can use curly brackets: `{}`. Using type-casting, we can also convert a list to a set. Make a new file called `sets.py` and let's get started!

```
#!/usr/bin/env python3

# Creating a set using list to set type-casting
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)
```

To add an element to the set, we can use the `add()` function:

```
# Try adding an element to the set
album_set.add("Back in Black")
print(album_set)
```

To remove something from a set, we can use the `remove()` function.

```
# Remove element from set
album_set.remove(10.0)
print(album_set)
```

We can verify if an element is in the set using the `in` command.

```
# Verify element presence in a list
exists = "Back in Black" in album_set
print(exists)

no_exists = "Pillow" in album_set
print(no_exists)
```

To find the intersection of two sets, we use the `&` command or the `intersection()` function

```
# Find intersecting elements in lists
another_album_set = {"Thriller", "Closer", "The Queen is Dead", "Born in the USA", "Synchronicity"}
my_intersections1 = album_set & another_album_set
print(my_intersections1)

my_intersections2 = album_set.intersection(another_album_set)
print(my_intersections2)
```

Unlike lists and tuples, sets only have unique elements, meaning there is only one of a particular element in a set. Duplicate terms are not present. 

```
# Demonstrate lack of duplicates in sets
duplicated_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(duplicated_list)

duplicated_list_as_set = set(duplicated_list)
print(duplicated_list_as_set)
```

### Boolean Types (Boolean)

A Boolean value can take two on two values: True or False. Make a new file called `booleans.py`. We're going to take a look at how Booleans work!

```
#!/usr/bin/env python3

bool1 = type(True)
print(bool1)
```

We can also use numerics to represent a Boolean value, where 1 represents True and 0 represents False:

```
# Demonstrate Boolean as integer
bool2 = int(True)
print(bool2)
bool3 = int(False)
print(bool3)

# Demonstrate Boolean as float
bool4 = float(True)
print(bool4)
bool5 = float(False)
print(bool5)
```

Similar to the `int()`, `str()`, and `float()` functions, we can also use the `bool()` function to typecast:

```
# Type cast numeric to Boolean
bool6 = bool(1)
print(bool6)

bool7 = bool(0)
print(bool7)
```

[Include comparison operations]

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

## For-Loops

## While Loops