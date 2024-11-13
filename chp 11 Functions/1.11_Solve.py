# 1. Function to Calculate and Return the Square of a Number

# Approach 1: Printing the result directly
def square(number):
    print(number ** 2)

square(4)  # Output: 16

print()

# Approach 2: Returning the result
def square(number):
    return number ** 2

result = square(5)
print(result)  # Output: 25

print()

# 2. Function with Multiple Parameters
# Creating a function that takes two numbers as parameters and returns their sum.

def add(num1, num2):
    return num1 + num2

print(add(100, 100))  # Output: 200

print()

# 3. Polymorphism in Functions
# Writing a function "multiply" that multiplies two numbers,
# but can also multiply strings (polymorphism).

def multiply(p1, p2):
    return p1 * p2

print(multiply(4, 4))      # Output: 16
print(multiply('a', 4))    # Output: 'aaaa'
print(multiply(4, 'a'))    # Output: 'aaaa'
