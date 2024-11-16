# Dictionaries
# A dictionary is a collection of unordered, modifiable (mutable) paired (key: value) data.

# Creating a Dictionary
# To create a dictionary, we use curly brackets `{}` or the `dict()` built-in function.

# Syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Example Dictionary
person = {
    'Name': 'Deepak',
    'age': 23,
    'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django'],
    'address': {
        'city': 'Navi Mumbai',
        'state': 'Maharashtra'
    }
}

print("Person Dictionary:")
print(person)

# Dictionary Length
# The `len()` function checks the number of key-value pairs in a dictionary.

# Syntax
print("\nDictionary Type:", type(person))
print("Dictionary Length:", len(person))

# Accessing Dictionary Items
# We can access dictionary items by referring to their key name.

# Syntax
# Example Dictionary
cricketer = {
    'first_name': 'Rohit',
    'last_name': 'Sharma',
    'age': 36,
    'country': 'India',
    'is_married': True,
    'skills': ['Batting', 'Captaincy', 'Fielding', 'Leadership'],
    'address': {
        'street': 'XYZ Road',
        'zipcode': '400001'
    }
}

print("\nCricketer Dictionary:")
print(cricketer)

# Access specific values
print("\nAccessing specific values:")
print("First Name:", cricketer['first_name'])
print("Skills:", cricketer['skills'])
print("Street:", cricketer['address']['street'])

# Accessing non-existent keys safely
# Accessing an item by key name raises an error if the key does not exist. 
# To avoid this error, we can check if a key exists or use the `get()` method.

print("\nUsing `get()` method:")
print("First Name (using `get`):", cricketer.get('first_name'))
print("Address (using `get`):", cricketer.get('address'))

# Access nested keys with `get()` and a default value
street = cricketer['address'].get('street', 'Not Available')
print("Street (from nested dictionary):", street)

# Access non-existent key with a default value
unknown = cricketer['address'].get('number', 'N/A')
print("Non-existent key (default value):", unknown)
