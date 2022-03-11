# Session 8: Sequence Types

By: Viktoria Haghani

Session Date: 2022-03-15

Last Updated: 2022-03-11

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Sequence Types (Tuples, Lists, Ranges)

### Tuples

Tuples are an ordered sequence. They are written as comma-separated elements within parenthesis. Strings, integers, and floats can be contained in a tuple. Tuples are immutable, which means we can't change them. Start by making a script named `tuples.py`.

```
#!/usr/bin/env python3

tuple1=("disco", 10, 1.2)
print(type(tuple1))
```

#### Indexing Tuples

Much like we learned for other data types, we can use indexing to access elements within each tuple. Recall that indexing in Python is 0-based, so to access the first element in the tuple, we can use the index 0.

```
# Indexing tuples
tuple1=("disco",10,1.2)
first_element = tuple1[0]
first_el_type = type(tuple1[0])
print(tuple1[0], type(tuple1[0]))
```

Previously, we have learned that we can access the last element of a data type using the -1 index. We can also count backwards beginning from -1. Let's see what that looks like!

```
# Using negative indexing
last = tuple1[-1]
second_to_last = tuple1[-2]
third_to_last = tuple1[-3]
print(f'The last element is {last}. The second to last element is {second_to_last}. The third to last (first in this case) element is {third_to_last}')
```

If we would like to know the index of an element within a tuple, we can use the `index()` function.

```
# Find element index
genres_tuple = ("pop","rock","soul","hard rock","soft rock","R&B","progressive rock","disco")
genres_tuple.index("disco")
genres_tuple.index("rock")
```

#### Slicing Tuples

If we would like multiple elements from a tuple, we can slice the tuple. This follows the standard indexing convention, including the last index having one added to it. Essentially, this is like indexing but for more than one value.

```
# Slicing tuples
tuple_to_slice = ("disco", 10, 1.2, "hard rock", 10)
print(tuple_to_slice[0:3])
```

As a quick note, we can determine the total number of elements using the `len()` function, which we learned about for strings.

```
# Determine length of tuple
print(len(tuple_to_slice))
```

#### Sorting Tuples

We can sort a tuple using the "sorted" function. The input is the original tuple and the output is a new, sorted tuple. Using the function `sorted()` will temporarily sort a tuple, but it will not change the original tuple.

```
# Use the sorted() function
Ratings = (10,9,6,5,10,8,9,6,2)
print(f'The original tuple is: {Ratings}')

RatingsSorted = sorted(Ratings)
print(f'The sorted tuple is: {RatingsSorted}. Notice that our original tuple, {Ratings} is still unsorted')
```

Notice that the output shows that the `RatingsSorted` output has brackets `[]` instead of parentheses `()`. This is because the type has changed. It has become a list (we'll cover this soon!). This is because tuples are immutable (i.e. can't be changed), so the data type needs to change for us to manipulate it. Let's verify:

```
print(type(RatingsSorted))
```

In addition to sorting numbers, we can also sort strings:

```
# Sort tuple with strings
Cars=("bmx","audi","toyota","subaru")
Cars_sorted = sorted(Cars)
print(Cars_sorted)
```

#### Concatenating Tuples

Now what if we want to add something to a tuple? Well, we can't. We can, however, concatenate tuples to create new ones.

```
# Concatenating tuples
tuple1 = ("disco", 10, 1.2)
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
```

#### Nesting Tuples

Nesting is a very important part of learning Python. It applies for several sequence data types and can be extremely helpful for a number of situations. Nesting just refers to containing a data type within a data type (specifically a sequence type). In the case of tuples, that means that it's a tuple containing a tuple in it. We can use indexing to access different elements. For indexing nested data, we use the same 0-based indexing and each nested data entry gets its own new "index array." 

```
# Work with nested tuples
nested_tuple = (1, 2, ("pop", "rock"), (3, 4), ("disco", (5, 6)))

# Access the nested tuple at index 2
print(nested_tuple[2])

# Access the first element of the nested tuple at index 2 ("pop")
print(nested_tuple[2][0])

# Access the double nested 6 at the very end of the tuple
print(nested_tuple[4][1][1])

# Access the "s" in "disco"
print(nested_tuple[4][0][2])
```

### Lists

While learning about tuples, we ran into a lot of limitations related to the fact that tuples are immutable. Lists are essentially the same thing as tuples, but they can be manipulated! Lists are ordered sequences represented with square brackets. They can contain strings, floats, integers, other lists, and even other data types. You can even make a list of data frames. Lists are one of the most powerful data types that you can use in Python, and I use lists in nearly every script I write. Although we haven't explicitly learned about lists yet, you've seen them in other sessions as examples in code. Let's make a new file called `lists.py` and learn about why lists are as magical as they are. Let's look at some examples:

```
#!/usr/bin/env python3

# Make a list
list1 = ["Viki", "Oran", "Julia", "Kelly"]
print(list1)

# Include multiple data types in a list
list2 = ["Lamp", 3, 7.2, True, (1, 2, 3)]
print(list2)
```

#### Indexing Lists

By now, you should all be fairly comfortable with the rules of indexing. Please interject if you are still not comfortable with indexing. As you've noticed, this comes up with most data types, so it's important for you to understand it. Since the conventions are the same, let's try some indexing:

```
# Index a list
print(list2[0])
print(list2[0][0])
print(list2[-1])
print(list2[4][1])
```

#### Slicing Lists

This uses the same notation as tuples.

```
# Slice list
cars = ("bmx","audi","toyota","subaru")
some_cars = cars[0:2]
print(some_cars)
```

#### Adding Elements to Lists

Depending on if you are adding one or multiple elements to a list, you can use different functions. To add one element to a list, you can use `append()`. This is one of the most commonly used list functions.

```
# Appending to a list
my_fav_artists = ["Michael Jackson", "Metallica", "Guns N Roses"]
my_fav_artists.append("Billy Idol")
print(my_fav_artists)
```

Now if we want to add multiple artists to a list, we can use the `extend()` function. Notice that the `extend()` function only takes one list as an argument.

```
# Extending a list
my_fav_artists.extend(["Journey", "Bon Jovi", "Duran Duran", "Depeche Mode"])
print(my_fav_artists)
```

You can also specify what index you'd prefer to add an element to using the `insert()` function. The first argument of `insert()` is the index you'd like to add the element to and the second argument is what you're adding to the list.

```
# Insert item at a certain index of a list
my_fav_artists.insert(0, "Prince")
print(my_fav_artists) 
```

#### Changing Elements in Lists

In order to change an element in a list, we can access the index and reset the value.

```
# Change list element
my_fav_artists[0] = "Billy Joel"
print(my_fav_artists)
```

#### Removing Elements from Lists

Removing a list element can be done using the `del()` command and the index of the element.

```
# Delete element
del(my_fav_artists[0])
print(my_fav_artists)
```

You can also remove the last item of a list using the `pop()` command. Note that the `pop()` command outputs the last element, but it removes the element from the original list. It's like cutting the value from the list and pasting it to a different variable.

```
# Remove last item in list
my_fav_artists_popped = my_fav_artists.pop()
print(my_fav_artists)

# Access popped value
print(my_fav_artists_popped)
```

I'd like to note that the list does contain my favorite artists, but the replacements and removals are not reflective of my true opinions. Sorry Billy Joel, Prince, and Depeche Mode.

#### Turning Strings into Lists

We can convert a string to a list using `split()`. `split()` converts every group of characters separated by a space into an element of a list.

```
my_str = "Jack and Jill went up the hill"
split_str = my_str.split()
print(split_str)
```

The split function uses a default delimiter of a space, but we can specify a different delimiter, such as a comma, by using it as an argument in the `split()` function:

```
# Split using delimiter
alph = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
split_alph = alph.split(",")
print(split_alph)
```

#### Aliasing Lists

This is very similar to aliasing files using UNIX language. You can alias a list, meaning that if you change an element in one list, it also changes the other list. You can do so using the assignment operator `=`.

```
# Alias a list
listA = [1, 2, 3, 4, 5]
listB = listA
print(f'List A is originally {listA} and List B is originally {listB}')
# Add an element to listA but don't explicitly change listB
listA.append(6)
print(f'We changed List A and now it is {listA}. Since List B reflects this change as an aliased list, List B is also {listB}.')
```

#### Cloning Lists

Once again, similar to UNIX, cloning a list means that the lists will not be linked and therefore you can work independently on either list. You use the same notation as aliasing, but put a colon in square brackets after the list name.

```
# Clone a list
listC = listA[:]

# Change listA again but not listC
listA.append(7)
print(listA)
print(listC)
```

#### Simple Statistics with Lists of Numbers

Using a list of numbers, you can perform simple statistics.

```
# Perform simple statistics
listD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find the minimum in the list
print(min(listD))

# Find the maximum in the list
print(max(listD))

# Find the sum of the list
print(sum(listD))
```

#### For-Loops

For-loops are an entire discussion on their own and they can apply to other data types, so while we won't be covering them today, I wanted to note that for-loops can be applied to lists, and this is ultimately what makes lists as powerful as they are.

#### A Last Note About Lists

There are several miscellaneous functions you can use to manipulate lists. I couldn't cover them all in one session if I tried, so my advice is that if you want to know if you can manipulate a list in a certain way, Google "how to do X to a list in Python." You'll usually get an answer! 

### Ranges

The last sequencing type is a range. The `range()` function returns a sequence of numbers. Ranges become immensely useful in for-loops (which we'll learn in a later session). For now, we'll take a quick look at what it does. Make a new file called `ranges.py`.

```
#!/usr/bin/env python3

# Turn our range into a list
numbers = list(range(1,6))
print(numbers)
```

Let's take a look at our output more closely. Notice that our list starts with "1" and ends with "5." This is the same behavior we notice with indexing; our last digit has an off-by-one behavior. This means we have to add one to the last digit to get the range we want. For example, if we want the numbers 1-20 in a list, we have to use the following:

```
# Turn our range into a list containing numbers 1-20
range1_20 = list(range(1,21))
print(range1_20)
```

We can also tell Python to skip numbers in a given range. This is very similar in notation to the strides we learned about when we learned about strings. Essentially, the notation is `(first number in range, last number in range + 1, every Xth value you want)`. Now let's put this in action. Let's try to view all even numbers in the range 1 through 10.

```
# Even numbers from 1-10
even_numbers=list(range(2,11,2))
print(even_numbers)
```

If we look more closely at the information in the range function, we see that we start at 2. Why not 1? This is because adding a value to skip other values accounts for the first value already. This command is basically us saying "Starting at 2 and ending at 11, skip every 2nd number." In this case, beginning our range with 1 means that our second element, 2, would be skipped instead. Be mindful of how indexes and ranges work, as they're not as intuitive as they sound.

## Exit Ticket

Update your `README.md` and Git push all your work from this session. Try pushing changes for files individually so you can customize comments.

Congratulations, you finished Session 8! 

## Extra Practice

This section is not intended to be part of the lesson, but rather extra practice after the session to help solidify some of the concepts learned.

### Exercise

Make a script that does the following:

1. TBD, will update after session

### Solution

Your solution may look a little different, so as long as you get the proper outputs, you're good to go! Here is one potential solution:

```
TBD
```
