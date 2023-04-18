# Session 12: Functions and Object-Oriented Programming

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2023-04-18

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Functions

What do `print()`, `int()`, `type()`, `sqrt()`, and `str()` all have in common? They're functions! Up to this point, we have been using several functions that Python has pre-installed. They usually take some input then produce some output or change. Functions are perfect to use when you have code that is commonly reused. You can make your own functions, but typically, you will use an already-made function that is either built-in or created by someone else. Many of the functions Python has built-in already are found in the examples and other sections. Here, we focus on how functions work and how to make functions. 

## Making a Function

There are generally two components of a function: the function name and the argument(s). When we use the `print()` function, `print` is the function name, and the argument is whatever we put in the parentheses. To make our own function, we start with the key word `def` followed by the function name. The function name should be descriptive of what it does. 

### Functions Without Arguments

Create a script called `functions.py`. Now let's take a look at some example functions. First, we are going to see an example where there is no argument. 

```
#!/usr/bin/env python3

# Create a function
def greeting():
    print("Hello, world!")
```

In the above example, we used `def` to tell Python that we are about to create a function. The function name is `greeting`. It has no required arguments, and simply prints "Hello, world!" 

### Functions with Arguments

Now let's take a look at another example where we give it a required argument.

```
def join_names(firstname, lastname):
    print(firstname, lastname)
```






To help others use your functions (including your future self), use triple quotes to explain your function like so:

```
# Create function with a description
def add1(a):
    """
    Add 1 to a
    """
    b = a + 1
    return b

# Execute function
print(add1(5))
```

The reason the triple quote notation is so important is because you can use the `help()` function on your function to see what it does.

```
help(add1)
```

Notice how your description appears! This is referred to as the documentation string.

## Objects

## Classes

## Creating a Class

## Exit Ticket

Update your `README.md` and Git push all your work from this session.

Congratulations, you finished Session 11! 