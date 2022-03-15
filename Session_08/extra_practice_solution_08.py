#!/usr/bin/env python3

# Make a list named `my_list` containing the following information (you will need to format it properly, but keep it in this order): glasses, canvas, soap, photo album, 5084988, 9.2, 3/11, False
my_list = ["glasses", "canvas", "soap", "photo album", 5084988, 9.2, 3/11, False]
print(my_list)

# Make the list nested by adding a tuple containing the numbers 1-5 in it
my_tuple = (1, 2, 3, 4, 5)
my_list.append(my_tuple)
print(my_list)

# Use indexing to print 5084988 from the list. Use an f-string to print the index in addition to the value in the same print statement.
print(f'At index 4 of my_list, we have the value {my_list[4]}')

# Use indexing to print out the number 3 from within the tuple. Use an f-string to print the index in addition to the value in the same print statement.
print(f'At index 8 and sub-index 2, my_list contains the value {my_list[8][2]}')

# Use indexing to access the "b" in "photo album." Use an f-string to print the index in addition to the value in the same print statement.
print(f'At index 3 and sub-index 8, my_list contains the value {my_list[3][8]}')

# Slice the list such that only strings are present in your sliced data.
print(my_list[0:4])

# Add the word "ideology" between "photo album" and 5084988.
my_list.insert(4, "ideology")
print(my_list)

# Change the word "canvas" to "panel."
my_list[1] = "panel"
print(my_list)

# Delete 9.2 from the list.
del(my_list[6])
print(my_list)

# Print the maximum value present in the tuple. (Hint: Use indexing to access the tuple)
my_max = max(my_list[-1])
print(my_max)

# Use the range function to print the numbers 1-20 ONLY (i.e. do not print 0 or 21)
my_range = list(range(1,21))
print(my_range)