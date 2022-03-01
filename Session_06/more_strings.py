#!/usr/bin/env python3

# Indexing strings
string_to_index = "Index Arrays"

# Single index value
first_A = string_to_index[6]
print(first_A)

another_index = string_to_index[4]
print(another_index)

# Multiple index values
first_word = string_to_index[0:5]
print(first_word)

last_word = string_to_index[6:12]
print(last_word)

# Last index notation
last_index = string_to_index[-1]
print(last_index)

# Strides
every_2nd_value = string_to_index[::2]
print(every_2nd_value)

every_3rd_value = string_to_index[::3]
print(every_3rd_value)

complicated_stride = string_to_index[0:5:2]
print(complicated_stride)

# Length function
my_length = len(string_to_index)
print(my_length)

# Find function
start_index_Arrays = string_to_index.find("Arrays")
print(start_index_Arrays)

# Python prints -1 if the item is not found
not_found = string_to_index.find("I'm not here")
print(not_found)

# Replicating strings
my_bird = "Bird "
total_birds = my_bird * 3
print(total_birds)

# Concatenating strings
first_name = "Viki "
last_name = "Haghani"
full_name = first_name + last_name
print(full_name)

# String formatting
first_name = "Viki"
last_name = "Haghani"
print("Hi, my name is ", first_name, last_name, ".")

# Variables
txt = "Nucleus"
num = 3/11

# Method 1: printf()
print('%s %.3f' % (txt, num))
print('%s %.3f %d %e' % (txt, num, 2.1, .1))

# Method 2: str.format()
print('{} {}'.format(txt, num))
print('{} {:.3f}'.format(txt, num))

# Method 3: f-strings
first_name = "Viki"
last_name = "Haghani"

my_first_f_string = f'My first name is {first_name} and my last name is {last_name}. That makes my full name {first_name + " " + last_name}'
print(my_first_f_string)

decimal_manip = f'The value of 3/11 is {num}. If we round to three decimal places, that makes 3/11 = {num:.3f}'
print(decimal_manip)

pet = "Sunny"
print(f'My pet\'s name is {pet}')