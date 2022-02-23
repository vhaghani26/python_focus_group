#!/usr/bin/env python3

# Examples of strings
str1 = "Hello world"
str2 = "Spring is coming!"
str3 = "My dog ate 3 slices of my pizza"
str4 = "I can't believe my dog did that"

# Escape Sequences
# \n is "Enter" or creates a line break
print("Roses are red,\nViolets are blue")
# \t enters a tab
print("Loading \t Done")
print("Python escape sequences use a backslash: \\")
print('I\'m in such a good mood today!')

# Prints two backslashes using escape sequence
print("Python escape sequences use a backslash: \\\\")
# Prints four backslashes using the 'r' command
print(r"Python escape sequences use a backslash: \\\\")

# String operations
original_str = "Viki is teaching me how to code in Python"
print(original_str)

# Turns everything uppercase
upper_str = original_str.upper()
print(upper_str)

# Turns everything title case
title_str = original_str.title()
print(title_str)

# Turns everything lowercase
lower_str = original_str.lower()
print(lower_str)

# Replace first argument with second argument
replace_str = original_str.replace("Viki", "The internet")
print(replace_str)

# Stripping spaces
spaced_out = " M y N a m e I s V i k i "
right_strip = spaced_out.rstrip()
left_strip = spaced_out.lstrip()
# Function that does not work for some reason ??
all_strip = spaced_out.strip()

print(right_strip)
print(left_strip)
print(all_strip)