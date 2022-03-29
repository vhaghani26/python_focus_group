# Session 9:

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2022-03-29

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

### Mapping Types (Dictionaries)

### Set Types (Set, Frozenset)

Make a new file called `set_types.py` and let's get started!

#### Sets

Sets are a type of collection. This means that like lists and tuples, you can input different Python data types. Unlike lists and tuples, sets are unordered, meaning that sets do not record element position. For us, this means we cannot index sets, which ends up making them less useful than lists (in my opinion). To define a set, you can use curly brackets: `{}`. Using type-casting, we can also convert a list to a set. 

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

To find the intersection of two sets, we use the `&` command or the `intersection()` function.

```
# Find intersecting elements in lists
another_album_set = {"Thriller", "Closer", "The Queen is Dead", "Born in the USA", "Synchronicity"}
my_intersections1 = album_set & another_album_set
print(my_intersections1)

my_intersections2 = album_set.intersection(another_album_set)
print(my_intersections2)
```

To see what is unique to a set (or different between them), you can use the `difference()` function.

```
# Find elements unique to each set
unique_to_album_set = album_set.difference(another_album_set)
unique_to_another_album_set = another_album_set.difference(album_set)
print(f'My album_set is {album_set} and another_album_set is {another_album_set}. {unique_to_album_set} are unique to album_set and {unique_to_another_album_set} are unique to another_album_set') 
```

Joining sets uses the `union()` function.

```
# Combine sets
combined_sets = album_set.union(another_album_set)
print(combined_sets)
```

Notice that 'Thriller' only shows up once even though it was in both lists. Unlike lists and tuples, sets only have unique elements, meaning there is only one of a particular element in a set. Duplicate terms are not present. 

```
# Demonstrate lack of duplicates in sets
duplicated_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(duplicated_list)

duplicated_list_as_set = set(duplicated_list)
print(duplicated_list_as_set)
```

Finally, we can check if sets are supersets (`issuperset()`) or subsets (`issubset()`) of each other.

```
# Supersets and subsets 
my_subset = {'A', 'B', 'C'}
my_superset = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}

# Check if a set is a superset
check_superset1 = my_superset.issuperset(my_subset)
print(check_superset1)
check_superset2 = my_subset.issuperset(my_superset)
print(check_superset2)

# Check if a set is a subset
check_subset1 = my_superset.issubset(my_subset)
print(check_subset1)
check_subset2 = my_subset.issubset(my_superset)
print(check_subset2)
```

#### Frozensets

Frozen sets are an immutable (i.e. cannot be edited) version of a set. Due to this, frozen sets can be used as keys in dictionaries or as elements in another set. Similar to sets, frozen sets are not ordered, meaning we cannot index them.

To create a frozen set, we can use the `frozenset()` function.

```
# Make an empty frozen set
print(f'The empty frozen set is: {frozenset()}')

# Tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
# Turn the tuple of vowels into a frozenset
fSet = frozenset(vowels)
print(f'The frozen set is: {fSet}')

# frozensets are immutable
fSet.add('v')
```

Now let's create a frozenset using the keys of a dictionary.

```
# Random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
# Turn dictionary keys into a frozen set
fSet = frozenset(person)
print(f'The frozen set is: {fSet}')
```

[Source](https://www.programiz.com/python-programming/methods/built-in/frozenset)

## Boolean Types (Boolean)

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

# Comparison Operators

[Include comparison operations]
