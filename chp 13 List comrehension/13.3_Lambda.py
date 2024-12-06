# Lambda Functions in Python
# Lambda functions are anonymous functions created using the `lambda` keyword.
# They can take any number of arguments but can only have one expression, which is implicitly returned.

print('Normal Function')

# A normal function to add two numbers
def add(a, b):
    return a + b

# Call the function with arguments 7 and 7
print(add(7, 7))  # Output: 14

print('')

print('Lambda Function')

# A lambda function to add two numbers
x = lambda a, b: a + b

# Call the lambda function with arguments 7 and 7
print(x(7, 7))  # Output: 14

print('')

print('Self-Invoking Lambda Function')

# A lambda function that is immediately invoked with arguments 7 and 77
print((lambda a, b: a + b)(7, 77))  # Output: 84

print('')

print('Square')

# A lambda function to calculate the square of a number
square = lambda x: x * x

# Call the lambda function to find the square of 2
print(square(2))  # Output: 4

print('')

print('Cube')

# A lambda function to calculate the cube of a number
cube = lambda x: x ** 3

# Call the lambda function to find the cube of 2
print(cube(2))  # Output: 8
