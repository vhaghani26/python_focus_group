# Session 11: Conditionals 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2023-04-05

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Conditionals (If-Else Statements)

What exactly is a conditional? Well, a conditional is when you want to carry out a certain set of actions only if something (data in this case) meets a certain condition. For example, if the weather is sunny out, then I will wear shorts. Otherwise, I will wear long pants. 

Now what about data? In many situations, our data is dynamic and we want to carry out different operations given a set of conditions. As such, one of the most widely used and powerful tools in bioinformatics is the use of conditionals. Let's dive in and see what we can do with conditionals!

Make a new file calle `if_else.py` and let's get started! 

Imagine you are at a club that requires you to be 18 years old to enter. Let's simulate this scenario in code. Try running the following in your script and let's see the output.

```
#!/usr/bin/env python3

age = 19

if age > 18:
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

## Adding `elif` to Conditionals


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












## Exit Ticket

Update your `README.md` and Git push all your work from this session. Try pushing changes for files individually so you can customize comments.

Congratulations, you finished Session 10! 