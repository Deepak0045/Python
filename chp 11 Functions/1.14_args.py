print('*Args')
print('Write a function that takes variable number of arguments and returns their sum')

# Function that uses *args to accept a variable number of arguments
# *args allows the function to take any number of positional arguments, which are passed as a tuple.
print('solution')

def sum_all(*args):  
    # Asterisk (*) is compulsory to allow multiple arguments. 'args' will be a tuple containing all the passed values
    return sum(args)  # Sum up all the values in the args tuple

print(sum_all(5, 5))        # Output: 10 (sum of 5 + 5)
print(sum_all(5, 5, 8))     # Output: 18 (sum of 5 + 5 + 8)
print(sum_all(5, 5, 100))   # Output: 110 (sum of 5 + 5 + 100)

# Investigation: Demonstrates the internal representation of *args
# *args will unpack the values as individual arguments, but inside the function, it's stored as a tuple.
print('Investigation')

def sum_all(*args):     # Again, *args allows multiple arguments
    print(*args)        # This will print each argument as individual items (not as a tuple)
    print(args)         # This will print args as a tuple (showing how all arguments are stored)
    return sum(args)    # Return the sum of all values in args

print(sum_all(1, 2, 3))  # Output: 
# First print will show: 1 2 3 (individual values)
# Second print will show: (1, 2, 3) (the tuple storing the values)
# Output of sum: 6 (sum of 1 + 2 + 3)
