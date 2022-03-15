#!/usr/bin/env python3

import math

# Variables
# I usually like to put these at the top so our code is modular (i.e. we can change variables easily and rerun the script with different inputs)
var1 = 9.2
var2 = 17
var3 = 3.4
var4 = "19"
var5 = -26
var6 = 83
var7 = 9

# Determines the data type of the following variables: `var1 = "9.2"`, `var2 = 17`, and `var3 = 3.4`.
type_var1 = type(var1)
type_var2 = type(var2)
type_var3 = type(var3)
print(type_var1)
print(type_var2)
print(type_var3)

# Converts `var4 = "19"` to an integer.
my_int = int(var4)
print(my_int, type(my_int))

# Converts `var5 = -26` to a string.
my_string = str(var5)
print(my_string, type(my_string))

# Converts `var6 = 83` to a float.
my_float = float(var6)
print(my_float, type(my_float))

# Calculates the sum of `var4` and `var5`.
sum4_5 = int(var4) + var5
print(sum4_5)

# Calculates the difference between `var2` and `var1`.
dif2_1 = var2 - var1
print(dif2_1)

# Finds the product of `var5` and `var3`.
prod5_3 = var5 * var3
print(prod5_3)

# Raises `var3` to the power of `var1`.
pwr3_1 = var3 ** var1
print(pwr3_1)

# Assign `var7 = 9` and take the square root of it.
# Note that we need to import a module
sqrt7 = math.sqrt(var7)
print(sqrt7)

# Suppose you have a circle with a radius of 10 cm. What is the circumference of the circle? (Hint: Circumference = 2 * pi * radius)
circ = 2 * math.pi * 10
print(f'The circumference of a circle with a radius of 10 cm is {circ} cm.')

# An employee documents their time driving to and from work since they get compensated for it. In the past week, they spent the following amount of time driving: 33, 37, 35, 31, 29, and 39 minutes. How many total hours is this?
total_min = 33 + 37 + 35 + 31 + 29 + 39
total_hr = total_min/60
print(f'The employee spent {total_hr} hours driving.')