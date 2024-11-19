# Life is full of routines. In programming, we also handle many repetitive tasks.
# Python provides loops to simplify repetitive tasks:
# - while loop
# - for loop

# A `for` loop is used for iterating over sequences (lists, tuples, dictionaries, sets, or strings).

# --- For Loop with List ---
# Looping through a list and printing its items

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("For Loop with List:")
for num in numbers:  # Temporary variable `num` holds each item in the list
    print(num)


print('')  # Blank line for better output readability

# --- For Loop with String ---
# Looping through a string and printing each character
language = "python"

print("For Loop with String:")
for letter in language:  # Each character of the string is printed
    print(letter)


print('')


# Looping using the index of the string
for i in range(len(language)):
    print(language[i])


print('')


# --- For Loop with Dictionary ---
Person = {
    'Name': 'Deepak',
    'age': 23,
    'country': 'India',
    'is_married': False,
    'Skills': ['Html', 'Css', 'Js', 'Python', 'Django'],
    'address': {
        'City': 'Navi Mumbai',
        'Pin code': 500705,
    }
}


print("For Loop with Dictionary Keys:")
# Looping through keys
for key in Person:
    print(key)


print('')
print("Accessing Dictionary Values Directly:")
# Accessing values directly using .values()
for value in Person.values():
    print(value)

print('')


print("For Loop with Dictionary Keys and Values:")
# Looping through keys and values using .items()
for key, value in Person.items():
    print(f"{key}: {value}")


print('')


my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}


print("Accessing Dictionary Values by Key:")
# Accessing values using keys
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")


print('')


print("Accessing Dictionary Values Directly:")
# Accessing values directly using .values()
for value in my_dict.values():
    print(value)

print('')

# --- For Loop with Nested Dictionary ---

nested_dict = {
    'user1': {'name': 'Alice', 'age': 25},
    'user2': {'name': 'Bob', 'age': 30}
}

print("For Loop with Nested Dictionary:")

# Looping through nested dictionary

for key, details in nested_dict.items():
    print(f"{key}:")  # Outer dictionary key (e.g., 'user1', 'user2')

    # Looping through the inner dictionary
    for detail_key, detail_value in details.items():
        print(f"    {detail_key}: {detail_value}")  # Indented for clarity
