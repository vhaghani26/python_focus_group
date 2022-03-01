# Session 6: 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2022-02-11

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Data Types in Python

Last week, we started learning about text types and how to manipulate text types. This week, we will continue diving into text types.

### Indexing Strings

Go to `python_focus_group/` (you can now just type `pfg` to do so!). Create a new session directory, enter it, and make a file called `more_strings.py`:

```
pfg
mkdir session_06
cd session_06
touch more_strings.py
```

Each element of a string can be accessed using an index. It is helpful to think of a string as an ordered sequence. Each element in the sequence is accessed using its number (including spaces). In Python, indexing defaults to starting at 0, meaning 0 is the first index. It looks something like this:

| I | n | d | e | x |   | A | r | r | a | y  |  s |
|---|---|---|---|---|---|---|---|---|---|----|----|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

So to access the first A in "Arrays", we can use the following:

```
#!/usr/bin/env python3

# Indexing strings
string_to_index = "Index Arrays"

first_A = string_to_index[6]
print(first_A)
```

We can also do a range of letters

```
first_word = string_to_index[0:5]
print(first_word)

last_word = string_to_index[6:12]
print(last_word)
```

Notice that in the first example above, we start with 0 and end at 5. Why not 4? We'll expand more when we get to the `range()` function. To quickly explain, it does not use the formatting `[start, end]`. It instead uses something more like `[start index, total elements]`. In the above example, we started at the index 0 and wanted the first 5 elements, so our range is `[0:5]`. A standard rule of thumb if you want to just think about it in terms of indeces is to use `[start index, end index + 1]`. 

Another note on Python convention is that the index `-1` represents the last index. We can access the last index like so:

```
last_index = string_to_index[-1]
print(last_index)
```

### Strides

We can also use a stride to index strings. A stride value indicates that we want to select every Xth position. To demonstrate this, let's try this:

```
# Strides
every_2nd_value = string_to_index[::2]
print(every_2nd_value)
```

We can also get more complicated. We can specify what values we want to start and end at. Let's select every 2nd value starting at 0 and ending at 5:

```
complicated_stride = string_to_index[0:5:2]
print(complicated_stride)
```

### Assessing String Properties

There are several functions we can use on strings. Another few notable ones are `len()` and `find()`. 

`len()` allows us to learn the length of a string. Using the same "Index Arrays" sample as before, let's figure out the length:

```
# Length function
string_to_index = "Index Arrays"
print(len(string_to_index))
```

Note that the output is 12. The last index is 11, but since Python starts with an index of 0, there are 12 characters in the string - not 11. This function becomes more helpful when working with other data types, but I just wanted to demonstrate how we can work with strings.

`find()` allows us to find sub-strings. The argument of the function is the sub-string you would like to find. The output is the first index of the sequence. For example, if we want to find what index "Arrays" begins at, we would use:

```
# Find function
start_index_Arrays = string_to_index.find("Arrays")
print(start_index_Arrays)
```

The output is 6, which is the index we expect based on Python indexing of strings. If the sub-string is not in the string, the output is -1. Let's see:

```
not_found = string_to_index.find("I'm not here")
print(not_found)
```

### Replicating String Elements

We can replicate strings using multiplication (`*`):

```
# Replicating strings
my_bird = "Bird"
total_birds = my_bird * 3
print(total_birds)
```

### Concatenate Strings

We can also concatenate strings using `+`:

```
# Concatenating strings
first_name = "Viki"
last_name = "Haghani"
full_name = first_name + last_name
print(full_name)
```

### String Formatting

Notice above that we had to add the strings. There are other ways Python has developed for us to work with different string variables. This is something I use VERY frequently.

Previously, we have used commas in our print statements:

```
# String formatting
first_name = "Viki"
last_name = "Haghani"
print(first_name, last_name)
```

But what if we want to control the way the text looks? What if we want to add words, spaces, or punctuation in between? Well, there are three string formatting methods that can be employed.

#### Method 1: `printf()`

`printf()` is the name of an old C function. The syntax is well-known among programmers, but looks odd upon first glance.

```
txt = "Nucleus"
num = 3/11

# Method 1: printf()
print('%s %.3f' % (txt, num))
```

The `%s` indicates that the first element is a string. The `%.3f` means two things. The `3` indicates that we want to display three numbers after the decimal point. The `f` indicates that the second element is a float (more on floats later). We can also change notations even more, including changing things to an integer (`%d`) or to scientific notation (`%e`). Remember that the order of our instructions is respective to the order of our arguments:

```
print('%s %.3f %d %e' % (txt, num, 2.1, .1))
```

Now for the fun reveal: this is ugly! It works, but it's more complicated than simply printing the arguments after variables have been assigned (it's more useful for more complicated situations). I've NEVER had to use this string format. I prefer f-strings (Method 3).

#### Method 2: `str.format()`

The `format()` method is a powerful way to control string formatting. Let's see: 

```
# Method 2: str.format()
print('{} {}'.format(txt, num))
print('{} {:.3f}'.format(txt, num))
```

The first line here does not have us manipulate any formatting since nothing is between the `{}` entries. In the second line, we specify that we want our variable `num` to display as a 3 decimal point float. Notice that they print out differently. Another fun reveal: this is also ugly! It's complicated and irritating to use. This brings us to my favorite method, which is also the most intuitive: f-strings.

#### Method 3: f-strings

F-strings play into a larger type of string manipulation referred to as string interpolation. String interpolation refers to the idea that there are variables (placeholders) inside a string literal. This allows us to put python code inside a string directly in a fairly straightforward manner:

```
# Method 3: f-strings
first_name = "Viki"
last_name = "Haghani"

my_first_f_string = f'My first name is {first_name} and my last name is {last_name}. That makes my full name {first_name + " " + last_name}'
print(my_first_f_string)
```

To mimic the above example regarding decimal manipulation, we can do the following:

```
num = 3/11

decimal_manip = f'The value of 3/11 is {num}. If we round to three decimal places, that makes 3/11 = {num:.3f}'
print(decimal_manip)
```

The general formatting with f-strings is that you have single or double quotes with an f at the beginning:

```
my_variable = "variable"
f"Some string with my {my_variable}"
f'Some string with my {my_variable}'
```

And you put your string in the middle of the quotations. Anything that is contained within the curly brackets `{}` is carrying out Python code or calling on a variable. This is much more straightforward in my opinion, and why I recommend f-strings for string formatting. This is extremely helpful when troubleshooting because you can do something like `print(f'My data frame looks like: {data frame}')`, which allows you to visualize and annotate different parts of your code effectively. It also becomes extremely helpful when you get to troubleshooting for-loops (more on this later). Ultimately, this is something I recommend you use in your code.

## Exit Ticket

Update your `README.md` and Git push all your work from this session. Try pushing changes for files individually so you can customize comments.

Congratulations, you finished Session 6! 

## Extra Practice

This section is not intended to be part of the lesson, but rather extra practice after the session to help solidify some of the concepts learned.

**Exercise**: Make a script that does the following:

1. Using a method of your choice, fix the error that arises from the following code: `print('Anthony J. D'Angelo said, "Develop a passion for learning. If you do, you will never cease to grow."')`
2. Make the following sentence appear completely uppercase: The door swung open to reveal pink giraffes and red elephants.
3. Determine the index of the "a" in "departure."
4. Determine the length of the sentence: The tattered work gloves speak of the many hours of hard labor he endured throughout his life
5. Given a variable `breed = "Great Dane"`, use string formatting (e.g. f-string) to print the following sentence: The Great Dane looked more like a horse than a dog.
6. Assign `breed` to `"Mastiff"` and reprint the statement.

**Solution**

Your solution may look a little different, so as long as you get the proper outputs, you're good to go! Here is one potential solution:

```
#!/usr/bin/env python3

# Using a method of your choice, fix the error that arises from the following code: print('Anthony J. D'Angelo said, "Develop a passion for learning. If you do, you will never cease to grow."')
print('Anthony J. D\'Angelo said, "Develop a passion for learning. If you do, you will never cease to grow."')

# Make the following sentence appear completely uppercase: The door swung open to reveal pink giraffes and red elephants.
str1 = "The door swung open to reveal pink giraffes and red elephants."
STR1 = str1.upper()
print(STR1)

# Determine the index of the "a" in "departure"
str2 = "departure"
index_a = str2.find("a")
print(index_a)

# Determine the length of the sentence: The tattered work gloves speak of the many hours of hard labor he endured throughout his life
str3 = "The tattered work gloves speak of the many hours of hard labor he endured throughout his life"
my_length = len(str3)
print(my_length)

# Given a variable `breed = "Great Dane"`, use string formatting (e.g. an f-string) to print the following sentence: The Great Dane looked more like a horse than a dog.
breed = "Great Dane"
print(f'The {breed} looked more like a horse than a dog')

# Assign breed to "Mastiff" and reprint the statement.
breed = "Mastiff"
print(f'The {breed} looked more like a horse than a dog')
```