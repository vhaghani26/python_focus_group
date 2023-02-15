# Session 10: Determining Data Types and Loops 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2023-02-15

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Getting the Data Type

After several sessions of learning about different data types, we'll finally come to a close and move on. There are still some more data types that you may run into over time (e.g. a data frame), but we now have a great basis to work off of for our coding skills. To come to a close with the "Data Types" unit, we'll cover how to differentiate different data types. We've already seen it before, but I'll introduce it formally since it's helpful to check your data type. This will usually be used in response to some sort of type error. To do so, you can use the `type()` function. Let's make some variables containing different data types and determine the types:

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

Note that among the data types above, I primarily use strings, integers, floats, lists, ranges, dictionaries, and Boolean types. Your experiences may differ, so not all of the displayed types above may be necessary, but it's helpful to be aware that they exist.

## For-Loops

Make a new file calle `for_loops.py` and let's get started!

We can perform an action on every component of various data types (e.g. lists, dictionaries, tuples, sets, strings) using a for-loop function. The concept can be thought of as "for every item, do this action." This is called iteration. It allows you to carry out many actions at once instead of doing it individually for objects, variables, or data. It is one of the most widely and commonly used tools in Python. Regarding syntax, after the initial "for" statement, every indented line following the for/in command is considered inside the loop, and each indented line is executed once for each value in the list. While this may sound a little complicated, it is far easier understood in practice. 

### Basic For-Loops

Let's implement some for-loops for practice. Try running this in your script to see how the outputs are different.

```
#!/usr/bin/env python3

# Make a list
magicians = ["alice", "david", "carolina"]

# Printing the list to see the magicians
print(magicians)

# Printing each magician individually
for magician in magicians:
	print(magician)
```

Notice how the outputs are different. This is because the for loop carried out the print function for each element in the list rather than printing the whole list. Let's try another for-loop!

```
# Carry out more complicated actions
for magician in magicians:
	print(magician.title() + " , that was a great trick!")
	print("I can’t wait to see your next trick, " + magician.title() + ".\n")
```

If we want to do something after a for-loop, write the code without an indentation. You can also include a line break if you prefer to keep the code cleaner.

```
# Carry out more complicated actions
for magician in magicians:
	print(magician.title() + " , that was a great trick!")
	print("I can’t wait to see your next trick, " + magician.title() + ".\n")
	
print("Thank you, everyone. That was a great magic show!"
```

Here are some more examples of basic for-loops. Including how you can implement the `range()` function.

```
# More basic for-loops
A = [1, 2, 3, 4, 5]
for value in A:
    print(value)
	
dates = [1982, 1980, 1973]
for date in dates:
    print(date)
	
# A more complicated for-loop where you can access the index and list items
x = len(dates)
for i in range(x):
    print(i, dates[i])  
```

### Nested For-Loops

Another common use of for-loops is to nest them in order to work in combinations of variables. Nesting simply means to put a for-loop inside another for-loop. Let's say you want to determine all possible combinations of paired students in group A and group B. You can use a nested for-loop!

```
# Nested for-loop
groupA = ["Janine", "Jessica", "Jules"]
groupB = ["Osman", "Dag", "Logan"]

for person1 in groupA:
	for person2 in groupB:
		print(person1, person2)
```

Look at the output. See that this creates all combinations of variables within the two lists. This becomes incredibly useful when working with data sets with nested metadata, such as having male and female mice, each with WT and MUT genotypes, and each from several time points. Here is a more applied example of what this would look like using my project set-up. It uses many nested for-loops.

```
# Viki's Project Set-Up
sexes = ["male", "female"]
genotypes = ["WT", "MUT"]
time_points = ["E18", "P30", "P60", "P120"]
cell_types = ["Camk2a", "VIP"]

print("All conditions for Viki's project:")
for sex in sexes:
	for genotype in genotypes:
		for time_point in time_points:
			for cell_type in cell_types:
				print(sex, genotype, time_point, cell_type)
```

### Parallel For-Loops

#### For-Loops for Dictionaries

## While-Loops