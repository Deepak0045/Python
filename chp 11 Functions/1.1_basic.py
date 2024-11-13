# Defining a Function
# A function is a reusable block of code designed to perform a specific task. 
# To define a function, Python provides the 'def' keyword. 
# The code block inside a function is executed only when the function is called.

# Declaring and Calling a Function
# Defining a function is called declaring a function.
# Invoking a function is known as calling or executing the function. 
# Functions can be defined with or without parameters.

# Syntax:
# Declaring a function
# def function_name():
#     code block
# Calling a function
# function_name()

# Function without Parameters
# Functions can be declared without parameters.

def generate_full_name():
    first = 'Deepak'
    last = 'Yadav'
    space = ' '
    full_name = first + space + last
    print(full_name)

generate_full_name()

# Function Returning a Value
# Functions can return values using the return statement. 
# If a function lacks a return statement, it implicitly returns None.

def generate_full_name():
    first = 'DK'
    last = "Yadav"
    space = ' '
    full_name = first + space + last
    return full_name 

print(generate_full_name())
