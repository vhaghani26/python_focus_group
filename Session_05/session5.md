# Session 5: 

By: Viktoria Haghani

Session Date: 2022-02-08

Last Updated: 2022-02-03

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

[Last week](https://github.com/vhaghani26/python_focus_group/blob/main/Session_04/session4.md), we learned about variables. As a brief reminder, we can store several data types in a Python variable. Today, we're going to learn more about those data types.  

Go to `python_focus_group/` (you can now just type `pfg` to do so!). Create a new session directory, enter it, and make a file called `data_types.py`:

```
pfg
mkdir session_05
cd session_05
touch data_types.py
```

Using your text editor, open `data_types.py`. You can use this file to take notes on the data types. Remember you can include comments in addition to your executable code as a way to annotate/take notes on what you're learning.

[This](https://www.w3schools.com/python/python_datatypes.asp) is some of the reference material I am using for the Python data types in conjunction with the sources I mentioned at the beginning of the document.

### Text Types

### Numeric Types

### Sequence Types

### Mapping Types

### Set Types

### Boolean Types

### Binary Types

## Getting the Data Type

## Setting the Specific Data Type

Most times that you assign a Python variable with some type of data, Python is able to assign a data type to that variable. In some instances, there may be incompatibilities that require manual fixes. For example, consider the following:

```
a = 1
b = 1.5
c = '1'
```

The variable `a` is an integer, `b` is a float, and `c` is a string (text). Well, what happens when I want to add `a` and `b`? Let's try.

```
print(a + b)
```

Notice that we get an error. The types are incompatible, so you need to make `a` a float or make `b` an integer. Note that if we make `b` an integer, the transition from float to integer causes the loss of some information. In Python, instead of rounding a value up or down, everything after the decimal point gets dropped. Let's see what this looks like:

```
d = 1.9
print(type(d))

e = int(d)
print(type(e))
print(e)
``` 

Look at our outputs. It says that `d` is a float and `e` is an integer, meaning we succesfully converted `d` into an integer. However, when we print `e`, we see that our value is `1` instead of `2`. This shows us that the conversion Python uses to go from float to integer isn't as accurate as going from integer to float. 




## Type Casting