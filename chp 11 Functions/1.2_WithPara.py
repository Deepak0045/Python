# Function with Parameters
# Functions can accept different data types (number, string, boolean, list, tuple, dictionary, or set) as parameters.

# Single Parameter
# If a function takes a single parameter, it should be called with a corresponding argument.

# Syntax:
# Declaring a function
# def function_name(parameter):
#     code block
# Calling the function
# print(function_name(argument))

print('')

def greetings(name):
    msg = 'Hello ' + name + ', Welcome to this challenge'
    return msg

# Calling the function and printing the output
print(greetings('Deepak'))  
# Output: Hello Deepak, Welcome to this challenge

print('')

def add_ten(num):
    ten = 10
    return num + ten

# Calling the function and printing the output
print(add_ten(90))  
# Output: 100

print('')

def area_of_circle(r):
    Pi = 3.14
    return Pi * r * r

# Calling the function and printing the output
print(area_of_circle(10))  
# Output: 314.0

print()

# Two Parameters
# Functions can also take multiple parameters.
# If a function has multiple parameters, call it with the respective arguments.

# Syntax:
# Declaring a function
# def function_name(param1, param2):
#     code block
# Calling the function
# print(function_name(arg1, arg2))

def generate_full_name(first, last):
    space = ' '
    return first + space + last

# Calling the function and printing the output
print(generate_full_name(first='Deepak', last='Yadav'))  
# Output: Deepak Yadav
