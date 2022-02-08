# Session 5: BASH Aliases, Text Types, and Numeric Types

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

[This](https://www.w3schools.com/python/python_datatypes.asp) is some of the reference material I am using for the Python data types in conjunction with the sources I mentioned at the beginning of the document.

### Text Types (Strings)

Go to `python_focus_group/` (you can now just type `pfg` to do so!). Create a new session directory, enter it, and make a file called `text_types.py`:

```
pfg
mkdir session_05
cd session_05
touch text_types.py
```

Using your text editor, open `text_types.py`. You can use this file to take notes on the data types. Remember you can include comments in addition to your executable code as a way to annotate/take notes on what you're learning.

A string is a data type that is a sequence of characters. Even though it can contain numbers, the way a string is formatted tells Python to interpret those characters as characters rather than numbers. Let's take a look!

```
#!/usr/bin/env python3

# Strings
str1 = "Hello world"
str2 = "Spring is coming!"
str3 = "My dog ate 3 slices of my pizza"
str4 = "I can't believe my dog did that"
```

Notice that we have an apostrophe, a number, and even an exclamation mark in the above statements. Because we follow string formatting (flanking the outside of our string with single or double quotes), Python knows that we are inputting characters inside and that it should interpret it as such. 

Note that there is a `str()` function. We do not want to say anything like `str = x`, as this will override the `str()` function and give errors. For this reason, I will add numbers or prefixes to my variables. I used numbers in the above example. If I only have one variable, I would do something like `my_str` instead. This helps prevent overriding functions while also still having informative variable names.

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

## Exit Ticket

Update your `README.md` and Git push all your work from this session.

Congratulations, you finished Session 5!