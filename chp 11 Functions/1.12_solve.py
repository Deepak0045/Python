# Function Returning Multiple Values
# Creating a function that returns both the area and circumference of a circle given its radius

import math

def circle_stats(radius):

    # Calculate area and circumference using the math module for accurate pi value

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Calling the function and unpacking its returned values
a, c = circle_stats(3)

# Printing outputs with and without formatting
print('Area:', a, 'Circumference:', c)                  # Output: Raw values
print(f'Area is {a:.2f} and circumference is {c:.2f}')  # Output: Formatted to 2 decimal places

print()  

# Function with Default Parameter Value
# This function greets a user. If no name is provided, it uses a default parameter value.

def greet(name='User'):
    return 'Hello, ' + name + '!'

print(greet('Deepak'))   # Output: Hello, Deepak!
print(greet())           # Output: Hello, User!
