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

## Manipulating Strings

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

We can remove the white space from the string on the right or left side using `rstrip()` and `lstrip()`. 

```
# Stripping spaces
spaced_out = " M y N a m e I s V i k i "
right_strip = spaced_out.rstrip()
left_strip = spaced_out.lstrip()

print(right_strip)
print(left_strip)
```

### Indexing Strings

Each element of a string can be accessed using an index. It is helpful to think of a string as an ordered sequence. Each element in the sequence is accessed using its number (including spaces). In Python, indexing defaults to starting at 0, meaning 0 is the first index. It looks something like this:

| I | n | d | e | x |   | A | r | r | a | y  |  s |
|---|---|---|---|---|---|---|---|---|---|----|----|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

So to access the first A in "Arrays", we can use the following:

```
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

## thing.function() or function(thing)?

One thing you'll notice is that the functions we use are a little inconsistent here. For example, we use `thing.upper()` and then we use `len(thing)`. Why is `thing` on the outside in one and on the inside for the other? It depends on if the function is using object syntax. In Python, strings are considered objects. When using object syntax, the function comes after the variable. For `upper()` and `lower()`, these are functions specific to strings, and therefore use object syntax (`thing.function()`). `len()` is not specific to strings. It can be applied to other data types, such as lists, and therefore is not specific to an object. In that case, the function does NOT use object syntax, and it instead uses normal function syntax (`function(thing)`). 

Sometimes it is hard to differentiate, so if in doubt, Google it!

## Exit Ticket

Update your `README.md` and Git push all your work from this session.

Congratulations, you finished Session 5!