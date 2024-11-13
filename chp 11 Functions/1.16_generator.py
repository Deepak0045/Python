print('Normal function with return')
print('Write a function that returns even numbers up to a specific limit')

def even_generator_normal(limit):
    even_numbers = []  # Create an empty list to store even numbers
    for i in range(2, limit + 1, 2):
        even_numbers.append(i)  # Append even number to the list
    return even_numbers  # Return the entire list of even numbers

even_numbers = even_generator_normal(10)

for number in even_numbers:
    print(number)  # Print each even number

print('')
print('-------------------------------------------------------------------------------------------------------------')
print('')

print('Generator function with Yield')
print('Write a generator function that yields even numbers up to a specific limit')

def even_generator_yield(limit):
    for i in range(2, limit + 1, 2):
        yield i  # Yield each even number one by one

# Create a generator object
even_numbers = even_generator_yield(10)

# Iterate over the generator to get even numbers
for number in even_numbers:
    print(number)  # Print each even number yielded by the generator
