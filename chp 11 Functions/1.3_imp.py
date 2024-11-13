# Arbitrary Number of Arguments
# Allows passing a variable number of arguments to a function using *args.

# Syntax:
# Declaring a function
# def function_name(*args):
#     code block
# Calling the function
# function_name(param1, param2, param3, ...)

def sums_of_all(*nums):
    total = 0
    for num in nums:
        total += num
    return total

# Example call and output
print(sums_of_all(5, 5, 6, 4))  
# Output: 20


print()

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)

# Example call and output
print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob'))
# Output:
# Team-1
# Asabeneh
# Brook
# David
# Eyob


print()

def example(teams, *args):
    print(teams, args)

# Example call and output
example('Team-1', 'ind', 'aus', 'nz', 'eng')  
# Output: Team-1 ('ind', 'aus', 'nz', 'eng')


print('')


# Passing functions as parameters

def square_num(n):
    return n * n

def do_something(f, x):
    return f(x)

# Example call and output
print(do_something(square_num, 9))  
# Output: 81


print('')


# Function with Default Parameters

def greetings(name='Deepak'):
    return 'Hello ' + name + ' Sir!!!!'

# Example calls and outputs
print(greetings())  

# Output: Hello Deepak Sir!!!!

print(greetings('Tony'))  
# Output: Hello Tony Sir!!!!


print('')


# Check if a number is even

def is_even(n):
    return n % 2 == 0

# Example call and output
print(is_even(19))  
# Output: False


# Generate list of even numbers up to n

def is_even_list(n):
    even_list = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

# Example call and output
print(is_even_list(10))  
# Output: [0, 2, 4, 6, 8, 10]


print('')


# Calculate sum of even and odd numbers up to n

def sum_of_all(n):
    even_sum = 0
    odd_sum = 0

    for i in range(n + 1): 
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    print(f'Sum of even numbers is {even_sum} and sum of odd numbers is {odd_sum}.')

# Example call and output
sum_of_all(10)  
# Output: Sum of even numbers is 30 and sum of odd numbers is 25
