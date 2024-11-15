# Set Operations in Python

# 1. Intersection: Common elements between two sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
common_elements = whole_numbers.intersection(even_numbers)
print("Intersection (Common elements):", common_elements)  # Output: {0, 2, 4, 6, 8, 10}



# 2. Subset: Check if a set is a subset of another
is_subset = even_numbers.issubset(whole_numbers)
print("Is subset:", is_subset)  # Output: True



# 3. Superset: Check if a set is a superset of another
is_superset = whole_numbers.issuperset(even_numbers)
print("Is superset:", is_superset)  # Output: True



# 4. Difference: Elements in one set but not in another
odd_numbers = {1, 3, 5, 7, 9}
difference_set = whole_numbers.difference(even_numbers)
print("Difference (whole_numbers - even_numbers):", difference_set)  # Output: {1, 3, 5, 7, 9}



# 5. Symmetric Difference: Elements not shared by both sets
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
sym_diff = python.symmetric_difference(dragon)
print("Symmetric Difference (python ^ dragon):", sym_diff)  # Output: {'p', 'y', 't', 'd', 'r', 'a', 'g', 'h'}



# 6. Disjoint: Check if two sets have no common elements
are_disjoint = even_numbers.isdisjoint(odd_numbers)
print("Are even_numbers and odd_numbers disjoint:", are_disjoint)  # Output: True



# Additional Examples:
# Intersection between python and dragon
common_chars = python.intersection(dragon)
print("Common characters between 'python' and 'dragon':", common_chars)  # Output: {'o', 'n'}



# Difference between python and dragon
python_diff_dragon = python.difference(dragon)
print("Characters in 'python' but not in 'dragon':", python_diff_dragon)  # Output: {'p', 'y', 't'}



# Difference between dragon and python
dragon_diff_python = dragon.difference(python)
print("Characters in 'dragon' but not in 'python':", dragon_diff_python)  # Output: {'d', 'r', 'a', 'g'}
