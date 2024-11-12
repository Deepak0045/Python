# Slicing Items from a List
# Positive Indexing: We can specify a range of positive indexes by specifying the start, end, and step.
# The return value will be a new list.
# (default values for start = 0, end = len(lst) - 1 (last item), step = 1)

Web_technologies = ['HTML', 'CSS', 'JS', 'Git', 'Github', 'Python', 'Django']
print(Web_technologies)  # Output: ['HTML', 'CSS', 'JS', 'Git', 'Github', 'Python', 'Django']

# Slicing all items using full range
all_technologies = Web_technologies[0:7]  # Returns all items from index 0 to 6
print(all_technologies)  # Output: ['HTML', 'CSS', 'JS', 'Git', 'Github', 'Python', 'Django']

# Slicing from start to end without specifying end index
all_technologies2 = Web_technologies[0:]  # Returns all items starting from index 0
print(all_technologies2)  # Output: ['HTML', 'CSS', 'JS', 'Git', 'Github', 'Python', 'Django']

# Slicing specific range (from third to fifth items)
third_to_fifth = Web_technologies[2:5]  # Returns items from index 2 to 4
print(third_to_fifth)  # Output: ['JS', 'Git', 'Github']

# Slicing with step, skips every other item
skip = Web_technologies[::2]  # Returns every second item
print(skip)  # Output: ['HTML', 'JS', 'Github', 'Django']

print('')  # Separator

# Negative Indexing: Slicing with negative indexes to start from the end
print('Negative indexing')

# Slicing all items using full range with negative indexing
all_negative = Web_technologies[-7:]  # Returns all items starting from -7 (first item)
print(all_negative)  # Output: ['HTML', 'CSS', 'JS', 'Git', 'Github', 'Python', 'Django']

print('')

# Example list of fruits to demonstrate positive indexing slicing
fruits = ['banana', 'orange', 'mango', 'lemon']

# Slicing all items
all_fruits = fruits[0:4]  # Returns all items from index 0 to 3
print(all_fruits)  # Output: ['banana', 'orange', 'mango', 'lemon']

# Alternative way to slice all items
all_fruits = fruits[0:]  # Returns all items starting from index 0
print(all_fruits)  # Output: ['banana', 'orange', 'mango', 'lemon']

# Slicing from the second to the third item
orange_and_mango = fruits[1:3]  # Returns items from index 1 to 2
print(orange_and_mango)  # Output: ['orange', 'mango']

# Slicing from the second item to the end
orange_mango_lemon = fruits[1:]  # Returns items from index 1 to the end
print(orange_mango_lemon)  # Output: ['orange', 'mango', 'lemon']

# Slicing every second item
orange_and_lemon = fruits[::2]  # Returns every second item
print(orange_and_lemon)  # Output: ['banana', 'mango']

print('---------------------------------------------------------------------------------------------------------------------------')

# Modifying Lists
# Lists are mutable, so we can change individual items by index.

fruits = ['banana', 'orange', 'mango', 'lemon']

# Changing the first item
fruits[0] = 'Apple'
print(fruits)  # Output: ['Apple', 'orange', 'mango', 'lemon']

# Changing the second item
fruits[1] = 'Pineapple'
print(fruits)  # Output: ['Apple', 'Pineapple', 'mango', 'lemon']

# Changing the last item
last_index = len(fruits) - 1
fruits[last_index] = 'Lime'
print(fruits)  # Output: ['Apple', 'Pineapple', 'mango', 'Lime']

print('')

# Checking Items in a List
# Checking if an item is in a list using the 'in' operator.

fruits = ['banana', 'orange', 'mango', 'lemon']
# Check if 'banana' is in the list
does_exist = 'banana' in fruits
print(f"'banana' is in fruits: {does_exist}")  # Output: 'banana' is in fruits: True

# Check if 'lime' is in the list
does_exist = 'lime' in fruits
print(f"'lime' is in fruits: {does_exist}")  # Output: 'lime' is in fruits: False

# Additional Checks for Modified List

# Check if 'Apple' is in the modified list
does_exist = 'Apple' in fruits
print(does_exist)  # Output: False (since 'Apple' isn't in the unmodified list)
