# Session 10: Determining Data Types and Loops 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2022-03-29

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Binary Types (Bytes, Bytearray, Memoryview)

### Bytes

### Bytearray

### Memoryview

## Getting the Data Type

After several sessions of learning about different data types, we'll finally come to a close and move on. There are still some more data types that you may run into over time (e.g. a data frame), but we now have a great basis to work off of for our coding skills. To come to a close with the "Data Types" unit, we'll cover how to differentiate different data types. We've already seen it before, but I'll introduce it formally since it's helpful to check your data type. This will usually be used in response to some sort of type error. To do so, you can use the `type()` function. Let's make some variables containing different data types and determine the types:

```
# Create variables with different data types
type1 = "Hello World"
type2 = 3
type3 = 7.9
type4 = 1j
type5 = ["Dog", "Cat"]
type6 = ("Dog", "Cat")
type7 = range(5)
type8 = {"Name": "Viki", "Age": 23}
type9 = {"Peach", "Apple", "Strawberry"}
type10 = frozenset({"Peach", "Apple", "Strawberry"})
type11 = True
type12 = b"Hello"
type13 = bytearray(5)
type14 = memoryview(bytes(5))

# Check data types
print(type1, type(type1))
print(type2, type(type2))
print(type3, type(type3))
print(type4, type(type4))
print(type5, type(type5))
print(type6, type(type6))
print(type7, type(type7))
print(type8, type(type8))
print(type9, type(type9))
print(type10, type(type10))
print(type11, type(type11))
print(type12, type(type12))
print(type13, type(type13))
print(type14, type(type14))
```

Note that among the data types above, I've only personally had to use strings, integers, floats, lists, ranges, dictionaries, and Boolean types. Your experiences may differ, so not all of the displayed types above may be necessary, but it's helpful to be aware that they exist.

## For-Loops

## While Loops