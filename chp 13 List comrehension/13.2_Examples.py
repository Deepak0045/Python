
print('Generate a list of numbers')

numbers = [i for i in range(11)]
print(numbers)

print('')

print('It is possible to do mathematical operations during iteration')

squares = [i * i for i in range(11)]
print(squares)
print('')


# It is also possible to make a list of tuples

list_of_tules = [(i, i * i) for i in range(11)]
print(list_of_tules)
print('')


print('table using normal for loop')
num = 10
for i in range(1,11):
    print(f'{num} X {i} = {num * i}')

print('')

print('table using list comprehension')
number = 8
table = [f'{number} X {i} = {number * i}' for i in range(1,11)]
print('\n'.join(table))

print('')

print('List comprehension can be combined with if expression')

print('even numbers using list comprehension')

even_number = [i for i in range(21) if i % 2 == 0]
print(even_number)

print('')

print('even numbers using list comprehension')
odd_number = [i for i in range(21) if i % 2 != 0]
print(odd_number)

print('')

print('Filtering out positive even numbers')
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

positive_even = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even)
print('')

print('flattening a three dimensional array')

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)

print('After')
flattend_list = [number for row in list_of_lists for number in row]
print(flattend_list)

print('Another method')
# the flattend_list is equivalent to following

flattend_list = []

for row in list_of_lists:
    for number in row:
        flattend_list.append(number)

print(flattend_list)