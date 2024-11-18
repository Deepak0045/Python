# By default, statements in Python scripts are executed sequentially from top to bottom.
# If the processing logic requires so, the sequential flow of execution can be altered in two ways:

# 1. **Conditional Execution:** A block of one or more statements will execute if a certain condition is true.
# 2. **Repetitive Execution:** A block of one or more statements will execute repetitively as long as a condition is true.

# In this section, we will cover if, else, and elif statements. The comparison and logical operators
# we learned earlier will be useful here.

# ==========================
# If Condition
# ==========================
# In Python and other programming languages, the `if` keyword checks if a condition is true 
# and executes the block of code that follows. Remember the indentation after the colon.

# Syntax:
# if condition:
#     this part of the code runs for truthy conditions

a = 0
if a < 3:
    print('Hello')  # Output: Hello

print('')  # Prints a blank line for spacing

# ==========================
# If-Else
# ==========================
# If the condition is true, the first block executes; if not, the `else` block executes.

# Syntax:
# if condition:
#     this part of the code runs for truthy conditions
# else:
#     this part of the code runs for false conditions

a = 5
if a < 0:
    print('A is a negative integer')
else:
    print('A is a positive integer')  # Output: A is a positive integer

print('')  # Prints a blank line for spacing

# ==========================
# If-Elif-Else
# ==========================
# In daily life, we make decisions based on multiple conditions. Similarly, in programming,
# we use `elif` for multiple conditions.

# Syntax:
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

a = 0

if a < 0:
    print('A is a negative integer')
elif a == 0:
    print('A is zero')  # Output: A is zero
else:
    print('A is a positive integer')


# ==========================
# Nested Conditions
# ==========================
# Conditions can be nested within each other.

# Syntax:
# if condition:
#     code
#     if condition:
#         code


a = -1

if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive and odd integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative integer')  # Output: A is a negative integer


print('')  # Prints a blank line for spacing

# ==========================
# If Condition with Logical Operators
# ==========================
# Syntax:
# if condition and condition:
#     code


a = 12
if a > 0 and a % 2 == 0:
    print('A is a positive and even integer')  # Output: A is a positive and even integer
elif a > 0 and a % 2 != 0:
    print('A is a positive and odd integer')
else:
    print('A is zero')


print('')  # Prints a blank line for spacing


# ==========================
# If with `or` Logical Operator
# ==========================
# Syntax:
# if condition or condition:
#     code

user = 'james'
access_level = 4

if user == 'admin' or access_level >= 4:
    print('Access granted')  # Output: Access granted
else:
    print('Access denied')
