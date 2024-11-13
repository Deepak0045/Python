print('Lambda Function')
print('Create a lambda function to compute the cube of a number')

# Using normal functions
def cube(a):
    return a ** 3

print(cube(2))  # too lazy to do this every time

# Now using lambda function
cube = lambda X: X ** 3
print(cube(2))
