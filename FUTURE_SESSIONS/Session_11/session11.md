# Session 11: Conditionals 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2023-04-05

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Conditionals (If-Else Statements)

What exactly is a conditional? Well, a conditional is when you want to carry out a certain set of actions only if something (data in this case) meets a certain condition. For example, if the weather is sunny out, then I will wear shorts. Otherwise, I will wear long pants. 

Now what about data? In many situations, our data is dynamic and we want to carry out different operations given a set of conditions. As such, one of the most widely used and powerful tools in bioinformatics is the use of conditionals. Additionally, you can define conditions based on nearly all data types. Let's dive in and see what we can do with conditionals!

Make a new file calle `conditionals.py` and let's get started! 

Imagine you are at a club that requires you to be 18 years old to enter. Let's simulate this scenario in code. Try running the following in your script and let's see the output.

```
#!/usr/bin/env python3

age = 19

if age >= 18:
    print("You may enter!")
else:
    print("You are too young to enter.")
```

Upon running it, we see that since the age is 19, we may enter! What if our age is not 19? Let's change the age to 16 and run it again. You should now see a different response. This is the power of the conditional - different code is executed based on what condition gets met.

Generally speaking, conditionals have the following structure:

```
if {some condition}:
    {code to execute}
else:
    {alternative code to execute if the condition is not met}
```

Aside from simply carrying out code, you can also use the variable in the code:

```
age = 14
print("Dad: Happy birthday! How old are you turning this year?")
print(f"Son: Thank you. I’m turning {age} this year")
if age >= 16:
	print("Dad: Good, now go get a job")
else:
	print(f"Dad: Wow, only {16-age} more years until you can get a job")
```

## Adding `elif` to Conditionals

There may be times when you have more than two possible paths to execute depending on the data. In this case, you can add an `elif` statement. `elif` stands for "else if," essentially meaning "if it doesn't match the first condition, see if it matches this one." It makes more sense in action, so let's take a look. Below, we will check to see the status of `x` in relation to `y`.

```
x = 5
y = 10

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
```

Change the values of `x` and `y` and see how the outputs change.

## `and` vs. `or` in Conditionals

In other cases, you may want there to be a combination of conditions to be met. You can use `and` or `or` to specify conditions in the same statement. Despite sounding straightforward, this is actually quite a confusing concept, so let's break it down with some examples.

**1. Using `and`**

The use of `and` means that BOTH conditions must be satisfied in order for the code to execute. Using the previous example of the club, let's say that the club only allows people from age 18-20. Anyone who is 21 needs to go to another club. This means that people entering the club have to be 18 or older **AND** younger than 21. See below:

```
age = 20

if age >= 18 and age < 21:
    print("You may enter!")
else:
    print("This club is not for you.")
```

Try changing the age above and see what happens.

We can also introduce an `elif` statement here for practice:

```
age = 20

if age >= 18 and age < 21:
    print("You may enter!")
elif age < 18:
    print("You're too young!")
else:
    print("This club is not for you.")
```

**2. Using `or`**

Contrary to both conditions being satisfied, the use of `or` means that only one of the specified conditions will trigger the code in the conditional to execute. For example, let's say that you have a bag of marbles consisting of yellow, blue, green, and red marbles. Your favorite colors are blue and green, so if you get either blue or green, you will be happy. Let's simulate your reaction:

```
marble = "blue"

if marble == "blue" or marble == "green":
    print("Yay! This is one of my favorite colors.")
else:
    print("Oh no, I wanted a different color.")
```

Change `marble` to green now. See that it still satisfies the condition. Next, let's replace `or` with `and` to break the conditional.

```
marble = "blue"

if marble == "blue" and marble == "green":
    print("Yay! This is one of my favorite colors.")
else:
    print("Oh no, I wanted a different color.")
```

Even though we picked a blue marble in the above example, we are still seeing the "I wanted a different color" message pop up. Why is this? Well, since we have a blue marble, the only way to trigger the happy reaction is if the marble is simultaneously blue and green due to the use of `and`. 

Overall, being able to distinguish between `and` and `or` is an important concept in conditionals, but one that I have personally mixed up on multiple occasions. Make sure to thoroughly think through how you are phrasing your conditional and test it out when you are writing a script.

## Removing `else` from Conditionals

Imagine that you are reading in a data frame. Some data frames have headers, while others may not have headers. In this scenario, the code you are trying to execute downstream uses indexing that does not accomodate headers, so what can you do? Should you change the entire code? No! You can simply write a conditional such that if the data frame has headers, you delete the row containing the headers, and then skip to the rest of the code. This means that we can say something along the lines of "if the data frame has headers, then delete the first row of the data frame." However, this leaves us hanging with the `else` statement. What can we do?

Fortunately, we don't strictly _need_ an `else` statment. Let's see an example of just using the `if` statement on its own.

```
my_pets = ["Iguana", "Gecko", "Bird"]

if "Gecko" in my_pets:
    print("Ooh! Viki has a gecko!")
    
print("We have now passed the conditional")
```

We should see the above code letting us know that I have a gecko. Now, let's delete gecko from the list and re-run it:

```
my_pets = ["Iguana", "Bird"]

if "Gecko" in my_pets:
    print("Ooh! Viki has a gecko!")

print("We have now passed the conditional")
```

Notice that since we did not meet the condition, the code moves on without executing the code within the conditional, even with no `else` statement. This is helpful when a workflow may contain an additional step that is only needed depending on the input.

## Conditionals within Loops

One of the most common uses of conditionals is inside a loop. This is similar to the concept of a nested for-loop, but instead contains a conditional embedded below the for-loop. Let's take the below example, where we want to sort a list of numbers based on if it is a single- or double-digit number.

```
# Original list
my_numbers = [74, 60, 4, 93, 2, 1, 54]

# New lists
single_digits = []
double_digits = []

for num in my_numbers:
    if num < 10:
        single_digits.append(num)
    else:
        double_digits.append(num)

print(single_digits)
print(double_digits)
```

As you continue learning to code, you'll increasingly see that there are so many different ways to accomplish the same task. Below are some alternative implementations of the above code. You can see that some ways may be more efficient than others.

```
# Original list
my_numbers = [74, 60, 4, 93, 2, 1, 54]

# New lists
single_digits = []
double_digits = []

for num in my_numbers:
    if num >= 10:
        double_digits.append(num)
    else:
        single_digits.append(num)

print(single_digits)
print(double_digits)
```

And 

```
# Original list
my_numbers = [74, 60, 4, 93, 2, 1, 54]

# New lists
single_digits = []
double_digits = []

for num in my_numbers:
    # Convert the number to a string to assess length
    num = str(num)
    if len(num) == 1:
        single_digits.append(int(num))
    else:
        double_digits.append(int(num))

print(single_digits)
print(double_digits)
```

## Exit Ticket

Update your `README.md` and Git push all your work from this session.

Congratulations, you finished Session 11! 