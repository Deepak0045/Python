# 1. Function Without Parameters and Without Return Value
# This function takes no parameters and doesn't return any value. It simply performs an action.

def greet():
    print('Hello World')

greet()  # Output: Hello World

print()

# 2. Function Without Parameters but Returning a Value
# This function returns a value but takes no parameters.

def get_pi():
    return 3.14

print(get_pi())  # Output: 3.14

print('')

# 3. Function With Parameters but Without Return Value
# Takes parameters but does not return anything, just performs an action.

def greet(name):
    print(f'Hello, {name}')

greet('Deepak')  # Output: Hello, Deepak

print()

# 4. Function With Parameters and Returning a Value
# Takes parameters and returns a result based on the parameters.

def add(a, b):
    return a + b

total = add(4, 4)
print(total)  # Output: 8

print('OR')

print(add(5, 5))  # Output: 10

print()

# 5. Function With Default Parameters
# Has default values for parameters, which are used if no argument is provided.

def greet(name='deepak'):
    return name + ' Hello'

print(greet())          # Output: deepak Hello
print(greet('Suraj'))   # Output: Suraj Hello

print()

# 6. Function With Variable-Length Arguments (*args)
# Takes any number of positional arguments and treats them as a tuple.

def add(*nums):
    return sum(nums)

print(add(5, 5, 5))  # Output: 15

print()

# 7. Function With Variable-Length Keyword Arguments (**kwargs)
# Takes any number of keyword arguments and treats them as a dictionary.

def user_info(**kwargs):
    info = ''
    for key, value in kwargs.items():
        info += f'{key} : {value}\n'
    return info

print(user_info(name='Deepak', age=20))
# Output:
# name : Deepak
# age : 20

print()

# 8. Function to Get the Maximum of Two Numbers
# This function compares two numbers and returns the greater of the two.

def getmax(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(getmax(8, 9))  # Output: 9
