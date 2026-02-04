# Python Focus Group

## Introduction

The purpose of forming this Python Focus Group is to teach people how to code in Python. Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX, and a number of other sources that will be linked in subsequent sessions.

## Survey

I enjoy teaching and look for opportunities to improve where I can, and I can only do so with your feedback. Additionally, if I decide to pursue teaching professionally later on (e.g. at a community college) then having teaching reviews is extremely helpful. As such, if you attend or watch any of the sessions, I'd really appreciate if you could fill out [this survey](https://forms.gle/wVjumSgXeLSF9X8G7). It should only take a minute or two!

## Session_01

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/session1.md

Recording: https://youtu.be/LumSgtw8PIg

* Terminals
* Opening the Terminal
* Using the Terminal
* Directories
* GitHub
* GitHub Personal Access Tokens
* Files
* UNIX Cheat Sheet

## Session_02

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_02/session2.md

Recording: https://www.youtube.com/watch?v=OItmKM8uuyI

* File and Directory Manipulation
* Renaming a Directory
* Renaming a File
* Moving Files
* Moving Directories
* Copying Files
* Wildcards at the Command Line
* Deleting Files
* Deleting Directories
* Linking Files & Directories
* File Permissions

## Session_03

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/session3.md

Recording: https://youtu.be/uOv00Z2nxUg

* GitHub Desktop
* Installing Python via Conda
* Verifying Python Installation
* Python at the Command Line
* Python Scripts

## Session_04

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_04/session4.md

Recording: NA

* Text Editors
* The `print()` Function
* Comments in Python
* Variables

## Session_05

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_05/session5.md

Recording: https://youtu.be/v7MOOiPRwZE

* Aliasing (in .bashrc/.profile)
* Text Types (Strings)
* Escape Sequences
* Manipulating Strings
* Stripping Spaces

## Session_06

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_06/session6.md

Recording: https://youtu.be/IvIlPjDzDTg

* Indexing Strings
* Strides
* Assessing String Properties
* Replicating String Elements
* Concatenating Strings
* String Formatting (String Interpolation) 

## Session_07

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_07/session7.md

Recording: https://youtu.be/COkd1Q3uw58

* Numeric Types (Integers, Floats, Complexes) 
* Setting the Specific Data Type (Type Casting)
* Python Expressions
* Complex Math Operations and First Module Import

## Session_08

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_08/session8.md

Recording: TBD

* Sequence Types (Tuples, Lists, Ranges)

## Session_09

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_09/session9.md

Recording: TBD

* Mapping Types (Dictionaries)
* Set Types (Set, Frozenset)
* Boolean Types (Boolean)
* Comparison Operators
* Logic Operators

## Session_10

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_10/session10.md

Recording: TBD

* For-Loops
* While-Loops

## Session_11

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_11/session11.md

Recording: TBD

* Conditionals (If-Else Statements)
* Adding `elif` to Conditionals
* `and` vs. `or` in Conditionals
* Removing `else` from Conditionals
* Conditionals within Loops

## Session_12

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_12/session12.md

Recording: TBD

* Functions
* Making a Function
* Function Descriptions

## Session_13

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_13/session13.md

Recording: TBD

* Argparse
* Argparse Set-Up
* Required Arguments
* Optional Arguments
	* Default Values
* Switches
* Argparse Template

## Session_14

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_14/session_14.md

Recording: TBD

* Introduction to `screen`
* Installation
* Using `screen`
* `screen` Cheat Sheet

## Session_15

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_15/session_15.md

Recording: TBD

* Why should you use Conda?
* Installing Conda
* Mamba
* Creating Environments
* Activating an Environment
* Installing Packages
* Deactivating an Environment
* Advanced Conda Documentation

## Session_16

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/session_16.md

Recording: TBD

* Packages for Working with Data Frames
* Packages for Research Computing in Python
* The JupyterLab Interface
* Starting a Data Analysis Project
	* Project Organization
	* Initializing the Project
	* Creating a Jupyter Notebook
	* Using Jupyter Notebooks
	* Reading Files
	* Loading the Terns Data
	* Inspecting a Data Frame
* Documentation for 2000-2023 California Least Tern Data Set

## Session_17

Notes: https://github.com/vhaghani26/python_focus_group/blob/main/Session_17/Session_17.ipynb

Recording: TBD

* Summarizing Data in a Data Frame
* Working with Different Data Types

__________________________________


# Topic Bank

All sections below are topics I plan to integrate into sessions.

## Objects and Attributes

Python represents data as **objects**. Numbers, strings, data structures, and
functions are all examples of objects.

An **attribute** is an object attached to another object. An attribute usually
contains metadata about the object to which it is attached. You can access
attributes by typing a `.` after an object.

When an attribute is a function, it's called a **method**. For example, all
strings have a `capitalize` method.  Here's the code to capitalize a string:

```{code-cell}
"snakes everywhere!".capitalize()
```

The built-in `dir` function lists all of the attributes attached to
an object. Here are the attributes for a string:

```{code-cell}
dir("hi")
```

:::{caution}
Attributes that begin with two underscores `__` are used by Python internally
and are usually not intended to be accessed directly.
:::

## Classes

### Creating a Class

## Snakemake


_________
