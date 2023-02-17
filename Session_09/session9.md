# Session 9: Mapping Types and Comparison and Logic Operators

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2023-02-16

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

### Mapping Types (Dictionaries)

Dictionaries are a type of collection in Python. It has keys and values, where a key is analogous to the index. To create a dictionary, we use curly brackets: `{}`. The keys have to be immutable and unique (since they act as an index), but the values can be immutable, mutable, and duplicates. Each key and value pair is separated by a comma. Let's make a dictionary!

```
# Make our first dictionary
dict1 = {'a':0, 'b':1, 'c':2}
print(dict1)
```

You can use several data types as the values in a dictionary.

```
# Mix data types in a dictionary
dict2 = {"my_string":"Coffee", "my_int": 8, "my_float":9.2, "my_list":[1, 2, 3, 4, 5]}
print(dict2)
```

We can search for values in a dictionary like we would use indexing.

```
# Find values in a dictionary
dict3 = {
  "brand": "Honda",
  "model": "Civic",
  "year": 2020
}
print(dict3["brand"])
```

We can add new entries using the assignment operator `=`.

```
# Add new value dictionary entry
dict3["owner"] = "Sadie"
print(dict3)
```

We can also delete entries.

```
# Delete dictionary entry
del(dict3["owner"])
print(dict3)
```

Although we will cover Boolean types (True or False) at the end of this section, we can return a Boolean by verifying dictionary elements. Essentially, we can check if a value is in the dictionary using the `in` command.

```
# Check if elements are in the dictionary (note that it only works for keys)
check1 = "owner" in dict3
print(check1)
check2 = "year" in dict3
print(check2)
check3 = 2020 in dict3
print(check3)
```

Finally, we can print all keys or values in our dictionary.

```
# View all keys
print(dict3.keys())
# View all values
print(dict3.values())
```

Dictionaries can be iterated through in loops as well, but we will touch on that when we start learning about loops.

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

This concludes our mapping/sequence (storage) types! Although you can use whatever mapping/sequence type you prefer, the most commonly used are lists (if you don't need paired entries) and dictionaries (for paired entries). Since I've started coding in Python, I've only ever used lists or dictionaries - not sets, tuples, frozensets, etc. Ultimately, it's up to you to decide what you like to work with best, but hopefully you should have an overview on how to work with these different Python data types. The best part is that there's a lot of functional overlap between each type. For example, with many types, you can add, remove, or change an element. You can also nest many of these data types. The internet is your friend if you ever forget!

## Boolean Types (Boolean)

While Boolean values are usually not directly coded for, they are extremely helpful since any logical operator or statement ends up being a Boolean output. Booleans are most heavily associated with conditionals, one of the most important aspects of coding (we'll learn it soon!). A Boolean value can take two on two values: True or False. Make a new file called `booleans.py`. We're going to take a look at how Booleans work!

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

## Comparison Operators

As I mentioned earlier, we do not usually code for a Boolean. Instead, we allow Python to do the work for us. Comparison operators compare some value or operand, then, based on some condition, produce a Boolean.

We can use the equality operator, `==` to determine if values are equal.

```
# Variables
a = 5
b = 10
c = 5

# Determine if values are equal
IsEqual = a == b
print(IsEqual)
```

Let's compare the magnitude of the values.

```
# Check if a value is greater than another
IsGreater = a > b
print(IsGreater)

# Check if a value is less than another
IsLess = a < b
print(IsLess)

# Check if a value is less than or equal to another
IsLessOrEqual = a <= c
print(IsLessOrEqual)

# Check if a value is greater than or equal to another
IsGreaterOrEqual = b >= c
print(IsGreaterOrEqual)
```

Testing for equality is easy, but now how do we test for inequality using operators? In Python, we can use the inequality operator: `!=`.

```
# See if values are not equal
IsNotEqual1 = a != b
print(IsNotEqual1)

IsNotEqual2 = a != c
print(IsNotEqual2)
```

Interestingly, we can also use the equality and inequality operators for strings.

```
# Check if strings match
str1 = "Hello, World!"
str2 = "Hello, World!"
str3 = "Hello World!"

print(str1 != str2)
print(str1 == str2)
print(str1 != str3)
print(str1 == str2)
```

Even more strangely, we can compare letters.

```
# Compare letters
print("A" > "B")
print("A" < "B")
```

What does this even mean? Well, inequality operation for letters, words, and symbols goes according to the [ASCII value](https://www.ascii-code.com/) of letters. For example, the ASCII code for ! is 21, and the ASCII code for + is 43. Therefore, + is larger than !. Similarly, the value for A is 101 and B is 102. The case of the letters make a difference, so comparison between letters in Python is case-sensitive.

For your reference, here is a list of the comparison operators you can use in Python:

| Operation | Meaning |
|-----------|---------|
| `<` | strictly less than |
| `<=` | less than or equal |
| `>` | strictly greater than |
| `>=` | greater than or equal |
| `==` | equal (since only one `=` is a variable assignment) |
| `!=` | not equal |
| `is` | object identity |
| `is not` | negated object identity |

[Source](https://docs.python.org/3/library/stdtypes.html)

## Logic Operators

Logic operators take Boolean values and produce different Boolean values. The "not," "or," and "and" operator takes in two values to produce a new Boolean value. You can use "if, and" and "if, or" statements. The "and" statement is only True when both conditions are true. The "or" statement is true if one condition is True. The "not" statement outputs the opposite true value. This is essentially what we see in a [truth table](https://docs.oracle.com/html/E79061_01/Content/Reference/Truth_tables.htm). Let's take a look at these.

```
# Basic logic operators
print(not(True))
print(not(False))
```

The following example uses a conditional (if statement), which we will dive into in a future session. I will keep it basic here, but wanted to demonstrate the logic used.

```
# Using logic operators in a basic conditional
album_year = 1983
if album_year > 1979 and album_year < 1990:
	print("This album was made in the 80’s")
```

## Exit Ticket

Update your `README.md` and Git push all your work from this session. Try pushing changes for files individually so you can customize comments.

Congratulations, you finished Session 9! 

## Extra Practice

This section is not intended to be part of the lesson, but rather extra practice after the session to help solidify some of the concepts learned.

### Exercise

Make a script that does the following:

1. Make a dictionary called `my_dict` where the keys are `confusion, recording, organization, complaints, soup` and the values are `True, No, 57, [1, 2, 3], alphabet`, respectively.
2. Print the key corresponding the `recording`.
3. Add the key and value set `catastrophe` and `False`, respectively.
4. Delete the `recording` entry and its corresponding value.
5. Check if "soup" is in the dictionary.
6. Print all the keys in the dictionary.
7. Print all the values in the dictionary.
8. Make a list containing the following: `Balalaika, Bouqet, Outlook, Petticoat, Summit, Chime, Labourer, Patty, Persimmon, Sample`.
9. Turn the list into a set called `my_set1`.
10. Add `Nucleotidase` to the set.
11. Remove `Summit` from the set.
12. Check if `Violin` is in the set.
13. Make another set called `my_set2` containing the following: `Alias, Assist, Belfry, Sideboard, Soap, Balalaika, Persimmon`.
14. Find the elements that intersect the two sets.
15. Find the elements unique to `my_set2`.
16. Combine `my_set1` and `my_set2`. 
17. Assign `a = 16653509` and `b = 2448111` and determine if the values are equal.
18. Use a comparison or logic operator to determine which is greater.

### Solution

You can view the solution to the exercise [here](https://github.com/vhaghani26/python_focus_group/blob/main/Session_09/extra_practice_solution_09.py). Your solution may look a little different, so as long as you get the proper outputs, you're good to go! 

