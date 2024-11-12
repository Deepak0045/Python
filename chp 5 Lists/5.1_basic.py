# A list is a collection of different data types, which is ordered and modifiable (mutable).
# A list can be empty, or it may contain items of various data types.

# How to Create a List
# In Python, we can create lists in two ways:

# 1. Using the list built-in function
# Syntax:
lst = list()
empty_list = list()  # This is an empty list with no items.
print(len(empty_list))  # Output: 0

# 2. Using square brackets, []
# Syntax:
lst = []
empty_list = []  # This is an empty list with no items.
print(len(empty_list))  # Output: 0

# Example list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print('Number of Fruits is', len(fruits))  # Output: Number of Fruits is 4
print(type(fruits))  # Output: <class 'list'>

print()  # For separation in output

# Lists can have items of different data types
# Example of a list with mixed data types
lst = ['Deepak', 23, False, {'country': 'India', 'city': 'Mumbai'}, [1, 2, 3], None]
print(lst)  # Output: ['Deepak', 23, False, {'country': 'India', 'city': 'Mumbai'}, [1, 2, 3], None]

# Accessing List Items Using Positive Indexing
# We access each item in a list using their index. A list index starts from 0.

fruits = ['banana', 'orange', 'mango', 'lemon']

# Accessing the first item
first = fruits[0]
print(first)  # Output: banana

# Accessing the last item using the length of the list
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)  # Output: lemon

print('')  # For separation in output

# Accessing the last item using negative indexing
last_fruit = fruits[-1]
print(last_fruit)  # Output: lemon

# Unpacking List Items
players = ['Rohit', 'Virat', 'Rahul', 'Surya', 'Rishabh', 'Bumrah']
# Unpacking the first three items and the rest of the list
first_player, second_player, third_player, *rest = players

print(first_player)  # Output: Rohit
print(second_player)  # Output: Virat
print(third_player)  # Output: Rahul
print(rest)  # Output: ['Surya', 'Rishabh', 'Bumrah']

print('')  # For separation in output

# Example with unpacking and different placeholders
countries = ['india', 'america', 'russia', 'japan', 'pakistan', 'bangladesh', 'srilanka', 'France']

# Unpacking items with placeholders for clarity

frnd1, frnd2, frnd3, frnd4, *others_countires, frnd5 = countries
# Here, *others_countries collects the remaining countries in the list


print(frnd1)  # Output: india
print(frnd2)  # Output: america
print(frnd3)  # Output: russia
print(frnd4)  # Output: japan
print(others_countires)  # Output: ['pakistan', 'bangladesh', 'srilanka']
print(frnd5)  # Output: France
