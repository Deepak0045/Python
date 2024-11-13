print('Function with **Kwargs')
print('Create a function that accepts any number of keyword arguments and prints them in the format Key : Value')

# **kwargs allows a function to accept any number of keyword arguments. These arguments are passed as a dictionary where
# the keys are the argument names, and the values are the argument values.
print('Need of **Kwargs')
print('')

# A basic function that requires predefined parameters for 'name' and 'power'.
def SuperHero(name, power):
    print('Name = ', name, 'Power = ', power)

# This works fine as both 'name' and 'power' are passed explicitly.
SuperHero(name='Superman', power='Super-Human Strength')

# However, trying to pass an additional argument (enemy) results in an error since the function doesn't accept keyword arguments by default.
# SuperHero(name='Superman', power='Super-Human Strength', enemy = 'batman')  # This will raise an error.

print('')
print('Now using **kwargs')
print('')

# With **kwargs, we can accept any number of keyword arguments. 
# The function receives them as a dictionary, allowing flexibility in the number and type of arguments passed.

def SuperHero(**kwargs):

    # kwargs is a dictionary containing all the keyword arguments passed to the function

    for key, value in kwargs.items():
        print(f'{key} : {value}')

# This will work fine as the function can now accept any number of keyword arguments.
SuperHero(name='Superman', power='Super-Human Strength')

# Adding an additional argument 'enemy' does not result in an error as **kwargs is used.
SuperHero(name='Superman', power='Super-Human Strength', enemy = 'batman')


# output:

# Function with **Kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format Key : Value
# Need of **Kwargs

# Name =  Superman Power =  Super-Human Strength

# Now using **kwargs

# name : Superman
# power : Super-Human Strength

# name : Superman
# power : Super-Human Strength
# enemy : batman
