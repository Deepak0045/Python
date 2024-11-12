# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index
# (default 0 and string length - 1). If the substring is not found it raises a ValueError.

challenge = '30 Days of python'
sub_string = 'Da'

print(challenge.index(sub_string))  # Output: 3
print(challenge.index('Da'))        # Output: 3

print('')

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index 
# (default 0 and string length - 1)

challenge = '30 Days of python Days of python'
print(challenge.rindex('Da'))       # Output: 18

print('')

# isalnum(): Checks alphanumeric characters

challenge = '30 Days of python Days of python'
print(challenge.isalnum())          # Output: False

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())          # Output: True

challenge = '30DaysPython'
print(challenge.isalnum())          # Output: True

challenge = 'thirty days of python'
print(challenge.isalnum())          # Output: False (space is not an alphanumeric character)

challenge = 'thirty days of python 2019'
print(challenge.isalnum())          # Output: False

print('')

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)

challenge = 'thirty days of python'
print(challenge.isalpha())          # Output: False (space is excluded)

challenge = 'ThirtyDaysPython'
print(challenge.isalpha())          # Output: True

num = '123'
print(num.isalpha())                # Output: False

print()

# isdecimal(): Checks if all characters in a string are decimal (0-9)

challenge = 'thirty days of python'
print(challenge.isdecimal())        # Output: False

challenge = '123'
print(challenge.isdecimal())        # Output: True

challenge = '\u00B2'
print(challenge.isdigit())          # Output: False (not a decimal character)

challenge = '12 3'
print(challenge.isdecimal())        # Output: False (space not allowed)

print('')

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)

challenge = 'Thirty'
print(challenge.isdigit())          # Output: False

challenge = '30'
print(challenge.isdigit())          # Output: True

challenge = '\u00B2'
print(challenge.isdigit())          # Output: True

print('')


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