# Python String Manipulation and Formatting

# --- 1. String Creation and Display ---

# Single-character string
letter = 'P'
print(letter)                     # Output: P
print(len(letter))                # Output: 1

# Multiline string
multiline_string = '''I am a teacher
There’s nothing I enjoy more than teaching
That’s why I created this challenge.'''
print(multiline_string)


# --- 2. String Concatenation ---

first_name = 'Deepak'
last_name = "Yadav"
space = ' '
full_name = first_name + space + last_name
print(full_name)                  # Output: Deepak Yadav

# String length comparison
print(len(first_name) < len(last_name))  # Output: True


# --- 3. Escape Sequences ---

# Using escape sequences
print('Days\tTopics\tExercises')  # Adds a tab space
print('Day1\t2\t5\nDay2\t4\t8')  # New line and tab spaces


# --- 4. String Formatting ---

# Old Style Formatting (% Operator)
formated_string = 'I am %s %s and I teach %s.' % (first_name, last_name, 'Python')
print(formated_string)

# New Style Formatting (str.format)
new_string = 'I am {} {} and I teach {}'.format(first_name, last_name, 'Python')
print(new_string)

# f-String Formatting (Python 3.6+)
x, y = 5, 4
print(f'{x} + {y} = {x + y}')     # Output: 5 + 4 = 9


# --- 5. Indexing and Slicing ---

language = 'Python'
print(language[0])                # Output: P
print(language[1:3])              # Output: yt
print(language[-3:])              # Output: hon
print(language[::-1])             # Output: nohtyP


# --- 6. String Methods ---

# capitalize(): Capitalizes the first character of the string
challenge = '30 days of python'
print(challenge.capitalize())     # Output: 30 days of python

# count(): Counts occurrences of a substring
print(challenge.count('th'))      # Output: 1

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))   # Output: True

# find() and rfind(): Finds first or last occurrence of a substring
print(challenge.find('r'))        # Output: -1
print(challenge.rfind('y'))       # Output: 6

# isalnum(): Checks if all characters are alphanumeric
print('ThirtyDaysPython'.isalnum())  # Output: True
print('thirty days'.isalnum())       # Output: False

# isalpha(): Checks if all characters are alphabetic
print('ThirtyDaysPython'.isalpha())  # Output: True
print('123'.isalpha())               # Output: False

# isdecimal() and isdigit(): Checks if all characters are numeric
print('123'.isdecimal())             # Output: True
print('\u00B2'.isdigit())            # Output: True

# islower() and isupper(): Checks if all characters are lowercase or uppercase
print(challenge.islower())           # Output: True
print('THIRTY DAYS'.isupper())       # Output: True

# join(): Concatenates a list of strings with a separator
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)                        # Output: HTML CSS JavaScript React

# strip(): Removes specified characters from start and end of string
challenge = 'thirty days of pythonnn'
print(challenge.strip('noth'))       # Output: irty days of pyth

# replace(): Replaces substring with a new string
print(challenge.replace('python', 'coding'))  # Output: thirty days of coding

# split(): Splits string into a list based on separator
challenge = 'thirty, days, of, python'
print(challenge.split(', '))         # Output: ['thirty', 'days', 'of', 'python']
