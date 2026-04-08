#!/usr/bin/env python3

# Make a dictionary called `my_dict` where the keys are `confusion, recording, organization, complaints, soup` and the values are `True, No, 57, [1, 2, 3], alphabet`, respectively.
my_dict = {"confusion": True,
           "recording": "No",
           "organization": 57,
           "complaints": [1, 2, 3],
           "soup": "alphabet"}

# Print the key corresponding the `recording`.
print(my_dict["recording"])

# Add the key and value set `catastrophe` and `False`, respectively.
my_dict["catastrophe"] = False
print(my_dict)

# Delete the `recording` entry and its corresponding value.
del(my_dict["recording"])
print(my_dict)

# Check if "soup" is in the dictionary.
print(f'{"soup" in my_dict}')

# Print all the keys in the dictionary.
print(my_dict.keys())

# Print all the values in the dictionary.
print(my_dict.values())

# Make a list containing the following: `Balalaika, Bouqet, Outlook, Petticoat, Summit, Chime, Labourer, Patty, Persimmon, Sample`.
my_list = ['Balalaika', 'Bouqet', 'Outlook', 'Petticoat', 'Summit', 'Chime', 'Labourer', 'Patty', 'Persimmon', 'Sample']
print(my_list)

# Turn the list into a set called `my_set1`.
my_set1 = set(my_list)
print(my_set1)

# Add `Nucleotidase` to the set.
my_set1.add("Nucleotidase")
print(my_set1)

# Remove `Summit` from the set.
my_set1.remove("Summit")

# Check if `Violin` is in the set.
print(f'{"Violin" in my_set1}')

# Make another set called `my_set2` containing the following: `Alias, Assist, Belfry, Sideboard, Soap, Balalaika, Persimmon`.
my_set2 = {'Alias', 'Assist', 'Belfry', 'Sideboard', 'Soap', 'Balalaika', 'Persimmon'}
print(my_set2)

# Find the elements that intersect the two sets.
print(f'{my_set2 & my_set1}')

# Find the elements unique to `my_set2`.
print(f'{my_set2.difference(my_set1)}')

# Combine `my_set1` and `my_set2`. 
combined_set = my_set1.union(my_set2)
print(combined_set)

# Assign `a = 16653509` and `b = 2448111` and determine if the values are equal.
a = 16653509
b = 2448111
print(f'The variables a and b are equal: {a == b}')

# Use a comparison or logic operator to determine which is greater.
print(f'Variable a is greater than b: {a > b}')