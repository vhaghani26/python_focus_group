# Session 4: Text Editors

By: Viktoria Haghani

Session Date: 2022-01-25

Last Updated: 2022-01-20

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Text Editors

### Introduction to Text Editors

A text editor is a type of computer program/software application that allows you to edit code as plain text files. It acts similar to editing a Word document, but for code. Rather than using `nano`, which requires the use of the keyboard only, text editors allow you to navigate with your mouse, copy and paste easily, and move code around in a much more human friendly way. Therefore, it's time for us to stop using `nano`. 

### Choosing a Text Editor

All of the files you have been editing with `nano` up to this point could have been edited with a text editor, such as: Atom, BBEdit, Geany, Gedit, Jedit, Notepad++, Sublime, VS Code, etc. So which programming/text editor should you use? It depends. According to Ian Korf, "Whatever is installed by default in your Linux distribution should be fine. I use Geany on Linux, BBEdit on Mac, and Notepad++ on Windows." As a Windows user myself, I'm a big fan of Notepad++. Since most (if not all) of you are Mac users, BBedit is a great option. 

### Installing Your Text Editor

As much as I'd love to provide more concrete instructions here, your text editor choice may be different. For the purposes of this tutorial, I am going to run through setting up BBEdit. I'd like to quickly note that I am not at all familiar with the use of BBEdit and Mac-based text editors. I will try my best to give you straightforward instructions, but I am relying heavily on external resources for guidance. 

If you have chosen to proceed with a different text editor, please carry out the installation and set up on your own at this time. If you have any questions, please feel free to ask and we can explore or troubleshoot together.

#### Setting Up BBEdit

[BBEdit](https://www.barebones.com/products/bbedit/download.html) is one of the leading text editors for MacOS. Although there is a paid version, the free version is sufficient for most (and probably all) of what you will need to do. First, you will need to go to your browser and search "BBEdit" and click on the first link. As of the day I am making this, the first link should be "BBEdit 14 - Bare Bones Software." Click on the link, and then navigate to the right hand side of the page where there is a "Free Download" button. Wait for the file to download, and then open the file. Once opened, you should get a screen that instructs you to drag the BBEdit icon into the Applications folder. Do so. 

Once you have downloaded BBedit, you can create or open files. [Here](https://itservices.usc.edu/files/2013/11/bbedit.pdf) are some instructions from USC on the use of BBedit. Essentially, you will navigate to the "File" menu to carry out most of these tasks.

## The `print()` Function

Last week, we started playing around with the `print()` function. `print()` is one of the most widely used functions. We will discuss how functions work in more depth later, but for now, I will explain briefly. A function looks something like this: `function()`, where the function name is outside of the parentheses, and the parentheses are there to take arguments. An argument is something you give a function as an input. In this case, our function is `print`, and our argument (input) is "Hello, World!". Try activating Python at your terminal and printing your name! In my case, it would look like this:

```
print("Viki")
```

Note that `print(Viki)` does not work, as the absence of quotation marks interprets "Viki" as a variable (we will learn more about variables in the future). Try a few more commands and see what you can do! Note that you can also use single quotations to print as long as the quotations marks flanking the statement are the same style (single vs. double).

## Comments in Python

Now that you have a text editor and the majority of set-up is complete, we can get to the meat of the coding! Exit Python at the terminal using `quit()` or `exit()`. We will begin by creating your session directory, `session04/`. Then, create a new file called `comments.py`. 

```
mkdir session_04
cd session_04/
touch comments.py
```

Using your text editor, add the interpreter directive to the beginning of your `comments.py` file:

```
#!/usr/bin/env python3
```

Here, you will learn how to use different comment styles in your code. Comments are useful for a number of reasons, but primarily because (1) it helps someone else read and understand what your code is doing and (2) it helps the future *you* understand the code you wrote. Organization is key when coding, so comments are a really easy way to facilitate this.

### Inline Comments

One type of comment you can write is an inline comment. This is a comment that occurs in the same line as code that is being run. To add a comment, we use the `#` symbol. Everything after the `#` is interpreted as a comment in Python, so it does not get read or executed. Add the following code to `comments.py`. Do this using your text editor instead of `nano`.

```
print("Here is an example of an inline comment") # Inline comment
```

Run this at the command line.

```
python3 comments.py
```

Notice that the output is:

```
Here is an example of an inline comment
```

Here, we see that our comment does not get printed.

### Single Line Comments

While inline comments are helpful, I personally have a preference for single line comments. This acts almost like a header, saying something like:

```
# Print my name
print("Viki")
```

Add this code with your name to `comments.py` and rerun it. The output should now also print out your name. The reason I prefer single line comments is because it seems more organized. It keeps a nice separation between commentary and functional code, so you don't get overwhelmed looking at your code.

#### The 80-Character Line Limit

One of the other reasons I prefer single line comments is because it keeps your lines shorter. Historically, computer terminals could only display 25 rows and 80 columns of text on screen at once. Any lines that were longer were just cut out of sight. Thus, old programmers split up long lines of code so that none exceeded 80 characters. It isn't relevant anymore, but it still looks neater, as you won't have unusually long code lines. It has also become a convention/artifact of old coding. Essentially, it doesn't *really* matte, but who doesn't want nice looking code?

[Source](https://richarddingwall.name/2008/05/31/is-the-80-character-line-limit-still-relevant/)

### Multi-Line Comments/Comment Blocks

I find two uses for multi-line comments.

1. Have a comment block as a descriptor
2. Prevent draft code from running

#### Comment Blocks as Descriptors

Let's start with a comment block. Sometimes I like providing a brief description on how to execute code before running it. For `comments.py`, we could do something like this:

```
'''
Script Usage:
To run comments.py, use the command "python3 comments.py" at the command line.

Output:
The output of comments.py are miscellaneous statements used as arguments to demonstrate the print() function
'''
```

or

```
"""
Script Usage:
To run comments.py, use the command "python3 comments.py" at the command line.

Output:
The output of comments.py are miscellaneous statements used as arguments to demonstrate the print() function
"""
```

Notice that we no longer use `#` for the comments. We *can* technically still use it, like this:

```
# Script Usage:
# To run comments.py, use the command "python3 comments.py" at the command line.

# Output:
# The output of comments.py are miscellaneous statements used as arguments to demonstrate the print() function
```

Personally, I think this can be tedious and frankly just annoying. However, Python's (PEP 8 Style Code Style Guide)[https://www.youtube.com/watch?v=Hwckt4J96dI] prefers multiple single line comments. This is because if done incorectly, you may accidentally turn your comments into docstrings. It's ultimately up to you, but the several single-line comments are *technically* the way you're recommended to do it.

#### Drafting Code

Even though there's contention regarding code block syntax, drafting code is a different story. The use of either three single or three double quotes flanking code is much quicker and does not become a permanent part of the code. What do I mean by this? Let's say we have a script of 100 lines for now (not uncommon to have scripts this length or longer) and you're trying to troubleshoot something. Instead of running the entire script every time, you're only testing out a portion of the code. Therefore, you can comment out code that you are not trying to run. Let's try a simple example. You do not have to understand the code written below just yet. All you need to know is that the two code blocks separated  by a blank line do different things. Add the following into `comments.py`:

```
# Prints numbers 1-20
for i in range(1,21):
	print(i)

# Prints the names of all my pets	
pet_names = ["Stella", "Blueberry", "Sunny", "Bird", "Zoscia"]
for pet in pet_names:
	print(pet)
```

Run the script and see the outputs. Now let's add a new name to the list pet_names, like so:

```
# Prints numbers 1-20
for i in range(1,21):
	print(i)

# Prints the names of all my pets	
pet_names = ["Stella", "Blueberry", "Sunny", "Bird", "Zoscia", "New Pet"]
for pet in pet_names:
	print(pet)
```

Run the script again and compare outputs. You should see "New Pet" added to the output. Notice that comparing the outputs can be a little difficult when you have so much being printed out. In this example, I don't care about the numbers 1-20. I know it already works the way I intend it to work, and now I only want to test the code the prints the pet names to make sure I added the pet name properly. This is where a comment block comes in handy. I can just comment out the first block of code so that my script only runs the pet name part instead of both the number and pet name part. To do this, we can add three single or double quotes flanking the code:

```
'''
# Prints numbers 1-20
for i in range(1,21):
	print(i)
'''

# Prints the names of all my pets	
pet_names = ["Stella", "Blueberry", "Sunny", "Bird", "Zoscia", "New Pet"]
for pet in pet_names:
	print(pet)
```

Run the script again. Notice that we no longer see the numbers 1-20. While the use of comment blocks may be less frequent in completed code, it is very helpful when drafting code or troubleshooting since it lets you focus on one part at a time.

Push your changes to GitHub using terminal commands or GitHub desktop.

## Variables

When coding, you will likely generate and store lots of information. In order to store the information, we can assign it to a variable. There are a few things we need to know about variables in Python:

* Python does not have a command for declaring a variable. The variable is created the moment you first assign a value to it using the assignment operator: `=`
* You can assign any data type to a variable (we will talk more about data types later)
* Variable names should not contain any spaces (spaces are usually replaced with underscores, which is the case with the variable: pet_names)
* Variable names must begin with a letter or the underscore character (a variable name cannot star with a number)
* Variable names can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
* Variables are case-sensitive (a and A are different variables)

In your session directory, create a new file called `variables.py`. We will demonstrate some examples of legal and illegal variable names. Put the following code in your `variables.py` file:

```
#!/usr/bin/env python3


# Illegal variable names
1animal = "Snake"
an-animal = "Dog"
an animal = "Cat"

# Legal variable names
ananimal = "Budgie"
an_animal = "Iguana"
_an_animal = "Gecko"
anAnimal = "Owl"
AnAnimal = "Fish"
ANANIMAL = "Bunny"
an_animal_1 = "Guinea Pig"
```

Notice how we are using comments to tell ourselves more information about the code. Now, try running the script:

```
python3 variables.py
```

You should get an invalid syntax error. Why? Because our variables are illegal! We cannot use that syntax for our variable names. Now, comment out the entire "illegal variables" section and try rerunning your script.

```
'''
# Illegal variable names
1animal = "Snake"
an-animal = "Dog"
an animal = "Cat"
'''

# Legal variable names
ananimal = "Budgie"
an_animal = "Iguana"
_an_animal = "Gecko"
anAnimal = "Owl"
AnAnimal = "Fish"
ANANIMAL = "Bunny"
an_animal_1 = "Guinea Pig"
```

When you rerun the script, you should not get an error. You might also be a little shocked to see that you also have no outputs. This is because we did not put anything in our script that gives us an output. Let's try calling and printing on of our variables:

```
# Legal variable names
ananimal = "Budgie"
an_animal = "Iguana"
_an_animal = "Gecko"
anAnimal = "Owl"
AnAnimal = "Fish"
ANANIMAL = "Bunny"
an_animal_1 = "Guinea Pig"

print(an_animal_1)
```

Rerun your script. You should see the output "Guinea Pig." One thing that's great about variables is that they can be changed! Let's say you've decided you don't like "Guinea Pigs" as part of your list. Change it to another animal:

```
an_animal_1 = "Bear"

print(an_animal_1)
```

Rerun your script. Now your output should be "Bear." 

**Note**: Although it isn't a strict convention, and certainly not necessary for early/personal coding, there is a convention that variables that are completely capitalized represent global/absolute values (i.e. things that do not change anywhere in the script; variable is the same throughout the script) and lowercase variables can repesent dynamic values. This becomes more important when developing software, but there is no need to do this or worry about it any time soon. Personally, I just stick to using all lowercase letters separated by underscores.

## Exit Ticket: Update README.md and Git Push

Using a similar style from last week, update your README.md in `python_focus_group/`. Once you have finished for the day, push all of your stuff to GitHub. 

Congratulations, you finished Session 4!