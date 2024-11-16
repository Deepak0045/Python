# Adding Items to a Dictionary
# We can add new key-value pairs to a dictionary.

# Example 1: Adding a new key-value pair
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key5'] = 'value5'
print("After adding 'key5':", dct)


# Example 2: Adding to a nested dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Adding a new key-value pair
person['job_title'] = 'Instructor'

# Adding a skill to the skills list
person['skills'].append('React')

# Display the updated dictionary
print("\nUpdated 'person' dictionary after additions:")
print(person)

# Modifying Items in a Dictionary
# Example: Changing a value in a nested dictionary
person['address']['zipcode'] = 400705
print("\nUpdated 'person' dictionary after modifying 'zipcode':")
print(person)

# Checking Keys in a Dictionary
# Using the 'in' operator to check for a key's existence.

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print("\nChecking if keys exist in the dictionary:")
print('key2' in dct)  # True
print('key5' in dct)  # False

# Removing Key-Value Pairs from a Dictionary
# Example of `pop()`, `popitem()`, and `del`

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Removing using pop
person.pop('first_name')  # Removes 'first_name'

# Removing the last item using popitem
person.popitem()  # Removes the last key-value pair (likely 'address')

# Removing using del
del person['is_married']  # Removes 'is_married'

print("\nUpdated 'person' dictionary after removals:")
print(person)

# Changing Dictionary to a List of Items
# Using the `items()` method to get a list of key-value tuples.

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print("\nDictionary as a list of items:", list(dct.items()))

# Clearing a Dictionary
# Using the `clear()` method to empty the dictionary.

dct.clear()
print("\nDictionary after clearing:", dct)

# Copying a Dictionary
# Using the `copy()` method to create a duplicate.

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()
print("\nOriginal dictionary:", dct)
print("Copied dictionary:", dct_copy)

# Getting Dictionary Keys and Values
# Example: Retrieving keys and values as lists.

keys = dct.keys()
values = dct.values()
print("\nKeys in the dictionary:", list(keys))
print("Values in the dictionary:", list(values))

# Advanced Example
# Working with nested dictionaries and performing all operations

nested_dict = {
    'item1': {'name': 'Apple', 'price': 120},
    'item2': {'name': 'Banana', 'price': 80},
    'item3': {'name': 'Cherry', 'price': 150}
}

# Adding a new item
nested_dict['item4'] = {'name': 'Date', 'price': 200}
print("\nNested dictionary after adding a new item:", nested_dict)

# Modifying an existing item
nested_dict['item2']['price'] = 85
print("\nNested dictionary after modifying 'item2':", nested_dict)

# Checking if a key exists
print("\nDoes 'item3' exist in the dictionary?", 'item3' in nested_dict)

# Removing an item
nested_dict.pop('item1')
print("\nNested dictionary after removing 'item1':", nested_dict)

# Getting keys and values
print("\nKeys in the nested dictionary:", list(nested_dict.keys()))
print("Values in the nested dictionary:", list(nested_dict.values()))
