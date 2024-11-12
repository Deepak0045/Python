# Boolean
# A boolean data type represents one of the two values: True or False. The use of these data types will be clear once we start 
# using the comparison operator. The first letter T for True and F for False should be capital unlike JavaScript. 

# Example: Boolean Values

print(True)
print(False)

print()


# Assignment Operators in Python
# Assignment operators are used to assign values to variables. The most basic assignment operator is =.

# Basic Assignment
# Python
# x = 10  # Assigns the value 10 to the variable x


x = 5

# Increment x by 3
x += 3
print(x)  # Output: 8

# Multiply x by 2
x *= 2
print(x)  # Output: 16

# Divide x by 4
x /= 4
print(x)  # Output: 4.0
print()
print()


# Arithmetic Operators in Python
# Arithmetic operators are used to perform mathematical operations on numerical values.
# Python supports the following arithmetic operators:   

# List of Arithmetic Operators
# Operator	Description	Example
# +	    Addition	    x + y
# -	    Subtraction	    x - y
# *	    Multiplication	x * y
# /	    Division	    x / y
# //	Floor division (returns the integer quotient)	x // y
# %	    Modulus (returns the remainder)	x % y
# **	Exponentiation	x ** y


print('Addition', 1 + 2)
print('Subtraction', 7-5)
print('multiplication', 5 * 5)
print('division', 9 / 6)    # Division in Python gives floating number

print('Divion without decimal', 7 // 2)  # gives without the floating number or without the remaining
print('Divion without decimal', 7 // 3)
print('Modulus', 3 % 2) 
print('Exponentiation', 2 ** 3)


print()
print()

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

print()


# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

print()


# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print()
print()



print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)



# Q1) Calculating area of a triangle

radius = 10
pi = 3.14
area_of_triangle = pi * radius ** 2
print('Area of triangle is : ', area_of_triangle) 

print()

# Calculating area of a rectangle

length = 10
width = 10

area_of_rectangle = length * width
print('area of rectangle is ', area_of_rectangle)
