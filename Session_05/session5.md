# Session 5: BASH Aliases and Python Data Types

By: Viktoria Haghani

Session Date: 2022-02-15

Last Updated: 2022-02-08

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Aliasing (in .bashrc/.profile)

A bash alias is an extremely helpful thing to take advantage of. It is essentially a shortcut or keyboard abbreviation that you can customize to make your life easier at the command line. Typically, the aliases you create get put in a `.bashrc`, `.profile`, or `.zshrc` file depending on how your system is set up/what operating system you use. These files contain configuration information that manage how your profile/terminal work for you. Everything contained in the file your system uses is run upon starting the terminal. When you create an alias and put it in your configuration file, it will run the command upon starting your terminal. This means you are free to use your shortcuts at any time! The alias command takes on the following structure:

```
alias "the shortcut you want to use"="the actual/old command"
```

Note that if the shortcut does not contain any spaces, you do not need quotes around it. Last week, I mentioned that I would discuss how I change my directory by only typing `pfg`. This is because in my `.bashrc`, I put the following:

```
alias pfg="cd /mnt/c/Users/vicky/Documents/GitHub/python_focus_group"
```

In English, this means that if I type `pfg`, the command `cd /mnt/c/Users/vicky/Documents/GitHub/python_focus_group` gets run. My favorite aliases to add to my `.bashrc` or `.profile` are:

```
alias ls="ls -F" # Add one char of */=>@| to enteries to denote type (file, directory, alias)
alias rm="rm -i" # Prompt user before every removal
alias cp="cp -i" # Prompt before overwrite
alias mv="mv -i" # Prompt before overwrite
```

Because the aliases listed above primarily qualify as "make the terminal stop you from doing something stupid," I'd highly recommend adding them into your file. The configuration bash files are ALWAYS located in your home directory. Navigate to your home directory and list ALL the directory contents (this is required in order to display files that begin with `.`):

```
cd ~
ls -al
```

Most Mac users will have a `.zshrc` file. If this is not present, look for `.bashrc` or `.profile` instead. Since this part can be quite tricky, you can check out [these instructions](https://www.moncefbelyamani.com/which-shell-am-i-using-how-can-i-switch/) to find out shell you are using and how to switch if needed. Open the file your system uses or the one you'd like to use using your text editor or nano since this will be a quick edit. Find somewhere appropriate to put the aliases (I usually scroll to where I see aliases already listed), and add in the following to your file:

```
alias ls="ls -F" # Add one char of */=>@| to enteries to denote type (file, directory, alias)
alias rm="rm -i" # Prompt user before every removal
alias cp="cp -i" # Prompt before overwrite
alias mv="mv -i" # Prompt before overwrite
alias pfg="cd your/path/to/python_focus_goup/" # Use pfg to change into python_focus_group
```

To get your path to `python_focus_group/`, you can navigate to the directory and use `pwd`. Save your file and close it. Then, restart your terminal (close it and open a new one) so that the commands get executed when it restarts. 

**Note**: [Here](https://linuxhint.com/differences_between_bash_zsh/) is some extra reading on the differences between the configuration file types.

## Data Types in Python

[Last week](https://github.com/vhaghani26/python_focus_group/blob/main/Session_04/session4.md), we learned about variables. As a brief reminder, we can store several data types in a Python variable. Today, we're going to learn more about those data types. There is a lot we can dive into for each data type, so today is meant to serve as an overview for these different data types. In the coming sessions, we will focus more heavily on individual data types to get a better understanding of how we can use these data types in our code.

Go to `python_focus_group/` (you can now just type `pfg` to do so!). Create a new session directory, enter it, and make a file called `data_types.py`:

```
pfg
mkdir session_05
cd session_05
touch data_types.py
```

Using your text editor, open `data_types.py`. You can use this file to take notes on the data types. Remember you can include comments in addition to your executable code as a way to annotate/take notes on what you're learning.

[This](https://www.w3schools.com/python/python_datatypes.asp) is some of the reference material I am using for the Python data types in conjunction with the sources I mentioned at the beginning of the document.

### Text Types (Strings)

A string is a data type that is a sequence of characters. Even though it can contain numbers, the way a string is formatted tells Python to interpret those characters as characters rather than numbers. Let's take a look!

```
# Strings
str1 = "Hello world"
str2 = "Spring is coming!"
str3 = "My dog ate 3 slices of my pizza"
str4 = "I can't believe my dog did that"
```

Notice that we have an apostrophe, a number, and even an exclamation mark in the above statements. Because we follow string formatting (flanking the outside of our string with single or double quotes), Python knows that we are inputting characters inside and that it should interpret it as such. 

Note that there is a `str()` function. We do not want to say anything like `str = x`, as this will override the `str()` function and give errors. For this reason, I will add numbers or prefixes to my variables. I used numbers in the above example. If I only have one variable, I would do something like `my_str` instead. This helps prevent overriding functions while also still having informative variable names.

### Numeric Types (Integers, Floats, and Complexes)

Numeric types are data types containing numbers.

#### Integers

#### Floats

#### Complexes

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

## Exit Ticket

Update your `README.md` and Git push all your work from this session.

Congratulations, you finished Session 5!