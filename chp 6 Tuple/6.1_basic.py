# Tuples in Python

# A tuple is an ordered, immutable collection of elements, which can hold various data types.
# Once created, the values in a tuple cannot be modified (added, removed, or changed).
# Tuples have limited methods due to their immutability.

# Some common tuple-related methods:

# - tuple(): Creates an empty tuple.
# - count(): Returns the count of a specified element in the tuple.
# - index(): Finds the index of a specified element in the tuple.
# - Concatenation (+): Joins two or more tuples to create a new tuple.

# Creating a Tuple

# Empty tuple (two ways):
empty_tuple = ()
# or using the tuple constructor:
empty_tuple = tuple()
print(empty_tuple)  # Output: ()

# Tuple with initial values:
tpl = ('item1', 'item2', 'item3')
print(tpl)  # Output: ('item1', 'item2', 'item3')

# Example:
fruits = ('banana', 'mango', 'orange', 'grapes')
print(fruits)           # Output: ('banana', 'mango', 'orange', 'grapes')
print(type(fruits))     # Output: <class 'tuple'>
print()

# Accessing Tuple Items
# Like lists, tuples support indexing (positive and negative) for item access.

fruits = ('banana', 'mango', 'orange', 'grapes')
print(fruits[0])        # Output: banana

last_index = len(fruits) - 1
last_fruit = fruits[last_index]  # Accessing the last item
print(last_fruit)       # Output: grapes
print()

# Slicing Tuples
# Tuples can be sliced to extract sub-tuples. The range includes the start index but excludes the end index.

# Range of Positive Indexes
country = ('india', 'america', 'japan', 'russia')
print(country[0:2])     # Output: ('india', 'america')
print(country[0:])      # Output: ('india', 'america', 'japan', 'russia')
print(country[0:4])     # Output: ('india', 'america', 'japan', 'russia')
print(country[0:6])     # Output: ('india', 'america', 'japan', 'russia') - exceeds length; still prints all
print()

# Range of Negative Indexes
print(country[-1])      # Output: russia
print(country[-1:])     # Output: ('russia',)
print(country[-4:-1])   # Output: ('india', 'america', 'japan')
print(country[-4:])     # Output: ('india', 'america', 'japan', 'russia')
print()

# Changing Tuples to Lists
# Tuples are immutable, so to modify their elements, we first convert them to a list, modify, and optionally convert back.

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)           # Output: ('banana', 'orange', 'mango', 'lemon')

# Convert tuple to list, modify, and display result
fruits_list = list(fruits)
fruits_list[0] = 'guava'
print(fruits_list)      # Output: ['guava', 'orange', 'mango', 'lemon']
