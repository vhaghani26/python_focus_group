#!/usr/bin/env python3

# Integers are only whole numbers with digits 0-9
int1 = 1
print(f'The type for int1 is {type(int1)}')
int2 = 9
int3 = 42
int4 = 558
int5 = 21543215
print(int5, type(int5))

# Adding commas makes our integers turn into tuples
not_int = 21,543,215
print(not_int, type(not_int))

# Floats are not whole numbers; they have decimals and fractions
float1 = 1.0
print(f'The type for float1 is {type(float1)}')
float2 = 3.4
float3 = 74.3
float4 = 9.99999999999
float5 = 1844384.85262
float6 = 3/4
print(float6)
float7 = 9/16
print(float7)
float8 = 2/3
print(float8)

# Complexes

# Simple Complexes
comp1 = 2J
comp2 = 7j

# Complicated Complexes

# Initialize real part
x = 5

# Initialize imaginary part
y = 3

# Convert x and y into a complex and store it in z
z = complex(x, y)

# View the real and imaginary parts:
print("The real part of the complex number is: ", z.real)
print("The imaginary part of the complex number is: ", z.imag)

# Confirm that all are complexes:
print(comp1, type(comp1))
print(comp2, type(comp2))
print(z, type(z))