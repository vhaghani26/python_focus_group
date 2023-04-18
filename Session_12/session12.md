# Session 12: Functions 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2023-04-18

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. 

The information on functions was drawn from [this website](https://www.w3schools.com/python/python_functions.asp).

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
    
# Call function
greeting()
```

In the above example, we used `def` to tell Python that we are about to create a function. The function name is `greeting`. It has no required arguments, and simply prints "Hello, world!" 

### Functions with Arguments

Now let's take a look at another example where we give it a required argument.

```
# Create a function with argument 'some_string'
def add_underscore(some_string):
    new_string = some_string + "_"
    print(new_string)

# Call function
add_underscore("Viki")
```

### Functions with Multiple Defined Arguments

Similar to the above example, we just need to specify the arguments when we define the function:

```
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)

add_numbers(3, 7)
```

### Functions with Undefined Numbers of Arguments

There may be a case where you have a function without a set number of arguments. In order to address this, you add a `*` before the argument name in the function definition. This way, the function will receive a tuple of arguments (which can be accessed and used according to tuple operations).

```
# Create a function that prints the first letter (initial) of each input name
def first_letters(*names):
    for name in names:
        print(name[0])

first_letters("Bijoy", "Helen", "Miley", "Roxanna")
```

Try changing the number of arguments. You'll see that it will work no matter how many arguments you add.

### Defining Arguments with Keywords

Sometimes, the arguments required of a function may be complicated. It may be difficult to remember the order of all of the arguments. To address this, you can use `key = value` syntax, which means the order of arguments will not matter. Let's write a function that reports the youngest child:

```
def my_kids(child3, child2, child1):
    print("The youngest child is " + child3)
```

Now let's say that our youngest child is Linus. We will call the function like so:

```
my_kids("Emily", "Tobias", "Linus")
```

Because of the order of our arguments vs. the defined arguments, it thinks Emily is the youngest. We can clarify either by reordering our argument inputs or using keywords:

```
my_kids(child1 = "Emily", child2 = "Tobias", child3 = "Linus") 
```

Now we have the correct output!

### Setting Default Arguments

There are many cases where it can be helpful to set default values. This is usually for more complicated situations, but we can demonstrate it with a simple example.

```
def my_home(country = "USA"):
    print("I am from " + country)
    
my_home("Sweden")
my_home("Lebanon")
my_home()
```

Notice that the last output, where we do not define an argument, uses the default we have set.

### Data Types as Arguments

You can pass more than just strings and integers into functions. In fact, you can pass just about any data type into a function so long as it is handled accordingly. Below, let's pass in a dictionary:

```
def associate_ages(a_dictionary):
    for name, age in a_dictionary.items():
        print(f'{name} is {age} years old.')

ages = {"Viki": 25, "Logan": 25, "Osman": 30}
associate_ages(ages)
```

### How to `Return` Outputs

Up to this point, we have just printed our outputs. Often times, functions are needed to output data that is stored and used after the function is called. In order to access this information, we can use `return`. Let's take a previous example and see how we can implement this:

```
# Original
print("Here, we are testing the original function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)
    
my_var = add_numbers(3, 7)
print("My variable: ", my_var)

# With Return
print("Here, we are testing the rewritten function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    return my_sum
    
my_var = add_numbers(3, 7)
print("My variable: ", my_var)
```

Notice that with the original function, we see the value get printed, but nothing is stored in our variable. When we use `return` instead of `print()`, we are able to store and use the function output. The simplified comparison of the above function can be seen below:

```
# Original
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)

# With Return
def add_numbers(number1, number2):
    my_sum = number1 + number2
    return my_sum
```

### Empty Functions

If, for some reason, you need a function with no content, you must use `pass`. This is because function bodies cannot be empty. The function will yield `None` if it is used.

```
def empty_function():
    pass

a = empty_function()
print(a)
```

### Recursive Functions

Recursive functions can also be used in Python. A recursive function is a function that calls on itself. Here, let's implement a recursive function where we use the variable `k` and have it decrease by 1 every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

```
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)
```

## Function Descriptions

To help others use your functions (including your future self), use triple quotes to explain your function like so. You can also write other information, such as information about the arguments.

```
# Create function with a description
def add1(a):
    """
    Add 1 to a
    """
    b = a + 1
    return b

# Execute function
add1(5)
```

The reason the triple quote notation is so important is because you can use the `help()` function on your function to see what it does.

```
help(add1)
```

Notice how your description appears! This is referred to as the documentation string.

## Exit Ticket

Update your `README.md` and Git push all your work from this session.

Congratulations, you finished Session 12! 