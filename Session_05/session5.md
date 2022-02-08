# Session 5: BASH Aliases, Text Types, and Text Operations

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

[Last week](https://github.com/vhaghani26/python_focus_group/blob/main/Session_04/session4.md), we learned about variables. As a brief reminder, we can store several data types in a Python variable. Today, we're going to start diving into Python data types. There is a lot we can discuss for each data type, so we will take it topic by topic so you have an in depth understanding of how to use and work with different data types.

[This](https://www.w3schools.com/python/python_datatypes.asp) is some of the reference material I am using for the Python data types in conjunction with the sources I mentioned at the beginning of the document.

## Text Types (Strings)

Go to `python_focus_group/` (you can now just type `pfg` to do so!). Create a new session directory, enter it, and make a file called `strings.py`:

```
pfg
mkdir session_05
cd session_05
touch strings.py
```

Using your text editor, open `strings.py`. You can use this file to take notes on the data types. Remember you can include comments in addition to your executable code as a way to annotate/take notes on what you're learning.

A string is a data type that is a sequence of characters. Even though it can contain numbers, the way a string is formatted tells Python to interpret those characters as characters rather than numbers. Let's take a look!

```
#!/usr/bin/env python3

# Examples of strings
str1 = "Hello world"
str2 = "Spring is coming!"
str3 = "My dog ate 3 slices of my pizza"
str4 = "I can't believe my dog did that"
```

Notice that we have an apostrophe, a number, and even an exclamation mark in the above statements. Because we follow string formatting (flanking the outside of our string with single or double quotes), Python knows that we are inputting characters inside and that it should interpret it as such. 

Note that there is a `str()` function. We do not want to say anything like `str = x`, as this will override the `str()` function and give errors. For this reason, I will add numbers or prefixes to my variables. I used numbers in the above example. If I only have one variable, I would do something like `my_str` instead. This helps prevent overriding functions while also still having informative variable names.

## Escape Sequences

In one of the earlier sessions, we started learning about how to use `print()` and how we need to correctly format string arguments using single or double quotes flanking the string. There were a few instances I demonstrated that resulted in an error. For example:

```
print('I'm in such a good mood today!')
```

To avoid the error, we can change the flanking quotations to double quotes. Alternatively, we can use escape sequences.

In Python, strings are interpreted as being entirely characters. However, there will be instances where we want to use actual Python code within a string (e.g. line break) or  we want to take a character as a literal character (e.g. make a single quote get interpreted as a character rather than Python code instructions). We can do so using escape sequences. An escape sequence is denoted using `\`. There are a few operations we can use this for:

* `\n` starts a new line
* `\t` inserts a tab
* `\\` makes the `\` get interpreted as a character, thus inserting a `\` into the string (this works for quotations as well)

Let's see these in practice:

```
# Escape Sequences
print("Roses are red,\nViolets are blue")
print("Loading \t Done")
print("Python escape sequences use a backslash: \\")
print('I\'m in such a good mood today!')
```

You can also put `r` in front of a string to make it get interpreted as a raw string (string literal). This is incredibly useful for writing readable regular expressions. Take the following:

```
print(r"//*/*//**")
```

This actually prints `//*/*//**`. This mimics directory paths, and can come in handy when you run into path issues reading in data down the line.

[Source](https://wiki.c2.com/?RawStrings)

## String Operations

When working with strings, you can use certain operations to manipulate them. Here are some functions you can use:

* `upper()` turns the string uppercase
* `title()` turns the string title case
* `lower()` turns the string lowercase
* `replace()` replaces part of the string

Now let's put these functions to use:

```
# String operations
original_str = "Viki is teaching me how to code in Python"

upper_str = original_str.upper()
print(upper_str)

title_str = original_str.title()
print(title_str)

lower_str = original_str.lower()
print(lower_str)
```

All of the above functions transform the case of the original string. We can also replace parts of the string. Let's replace my name in `original_str`:

```
replace_str = original_str.replace("Viki", "The internet")
print(replace_str)
```

### Stripping Spaces

### Indexing Strings

### Concatenate Strings

### String Formatting










## Exit Ticket

Update your `README.md` and Git push all your work from this session.

Congratulations, you finished Session 5!