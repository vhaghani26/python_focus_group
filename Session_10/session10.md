# Session 10: Determining Data Types and Loops 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2023-02-15

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Getting the Data Type

After several sessions of learning about different data types, we'll finally come to a close and move on. There are still some more data types that you may run into over time (e.g. a data frame), but we now have a great basis to work off of for our coding skills. To come to a close with the "Data Types" unit, we'll cover how to differentiate different data types. We've already seen it before, but I'll introduce it formally since it's helpful to check your data type. This will usually be used in response to some sort of type error. To do so, you can use the `type()` function. Let's make some variables containing different data types in a script called `data_types.py` and determine the types:

```
#!/usr/bin/env python3

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
	
# The range() function
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
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

There may be other times where you have two sets of data that you need to iterate through at the same time. I use this quite often in my own work, but for simplicity, I will use an example where we associate a list of numbers and letters to each other. Notice the difference in variable assignment compared to a traditional for-loop. The variables are assigned respective to the data input in the `zip()` function, but you can still call the variables whatever you want. All that matters is the order that the variables and data are listed.

```
# Parallel for-loop
listA = [1, 2, 3, 4, 5]
listB = ["A", "B", "C", "D", "E"]

for A, B in zip(listA, listB):
	print(f'Variable A is {A} and variable B is {B}. Here is AB: {A}{B}')

# Rename variables
for something1, something2 in zip(listA, listB):
	print(something1, something2)

# Switch the order of the lists
for A, B in zip(listB, listA):
	print(A, B)
```

### For-Loops for Dictionaries

While parallel for-loops are helpful for two lists or other mapping/sequencing data types, dictionaries have their own method of iteration. You can access the keys and values individually or both at the same time! This is done using the `keys()`, `values()`, and `items()` functions, respectively.

```
ages = {"Viki": 24, "Logan": 25, "Osman": 30}

# Access keys only
for name in ages.keys():
	print(name)

# Access values only
for age in ages.values():
	print(age)

# Access keys and values
for name, age in ages.items():
	print(f'{name} is {age} years old.')
```

## While-Loops

Make another script called `while_loops.py`.

While-loops are similar to for-loops, but instead of executing a statement a set number of times, a while loop will only run if a condition is met. This is especially helpful if you want to iterate a certain number of times.

```
#!/usr/bin/env python3

# Basic while-loop with 10 iterations
i = 0
while i < 10:
	print(i)
	i += 1

# A while-loop with two variables
x = 11
y = 1
while y < x:
	print(y)
	y += 1
```


Be careful with while-loops, however, as it is easy to get stuck in one. Below is an example of a never ending while-loop. Press cmd/ctrl + C to interreupt the broken loop when you run it.

```
# Broken while-loop
i = 0
while i < 10:
	print(i)
```

Comment the above while-loop out. Let's take a look at some other while-loops. We will be looking at logic and comparison operators in the next session, but this demonstrates some of the utility of while-loops in practice.

```
# More complicated while-loop
dates = [1982, 1980, 1973, 2000]
i = 0
year = 0
while year != 1973:
    year = dates[i]
    i = i + 1
    print(year)
print("It took ", i ,"repetitions to get out of loop.")

# Another complicated while-loop
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while Rating >= 6:
    print(Rating)
    Rating = PlayListRatings[i]
    i += 1

# One last while-loop for reference
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1
print(new_squares)
```

## Exit Ticket

Update your `README.md` and Git push all your work from this session. Try pushing changes for files individually so you can customize comments.

Congratulations, you finished Session 10! 