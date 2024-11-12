# Old Style String Formatting (% Operator)

first_name = 'Deepak'
last_name = 'Yadav'
language = 'Python'

formatted_string = 'I am %s %s and I teach %s.' % (first_name, last_name, language)
print(formatted_string)  # Output: I am Deepak Yadav and I teach Python.

print('')

radius = 10
pi = 3.14
area = pi * radius ** 2

area_of_circle = 'Area of circle with the radius %d is %.2f.' % (radius, area)
print(area_of_circle)  # Output: Area of circle with the radius 10 is 314.00.

print('')

# New Style String Formatting (str.format)

first = 'Deepak'
last = 'Yadav'
lang = 'Python'

new_string = 'I am {} {} and I teach {}'.format(first, last, lang)
print(new_string)  # Output: I am Deepak Yadav and I teach Python.

print('')

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))       # Output: 4 + 3 = 7
print('{} - {} = {}'.format(a, b, a - b))       # Output: 4 - 3 = 1
print('{} / {} = {:.2f}'.format(a, b, a / b))   # Output: 4 / 3 = 1.33
print('{} * {} = {}'.format(a, b, a * b))       # Output: 4 * 3 = 12
print('{} % {} = {}'.format(a, b, a % b))       # Output: 4 % 3 = 1
print('{} // {} = {}'.format(a, b, a // b))     # Output: 4 // 3 = 1
print('{} ** {} = {}'.format(a, b, a ** b))     # Output: 4 ** 3 = 64

print()

radius = 10
pi = 3.14
area = pi * radius ** 2

area_of_circle = 'The area of circle with the radius {} is {:.2f}.'.format(radius, area)
print(area_of_circle)  # Output: The area of circle with the radius 10 is 314.00.

print('')

# String Interpolation / f-Strings (Python 3.6+)

x = 5
y = 4

print(f'{x} + {y} = {x + y}')  # Output: 5 + 4 = 9
print(f'{x} - {y} = {x - y}')  # Output: 5 - 4 = 1
print(f'{x} * {y} = {x * y}')  # Output: 5 * 4 = 20
print(f'{x} / {y} = {x / y}')  # Output: 5 / 4 = 1.25
print(f'{x} % {y} = {x % y}')  # Output: 5 % 4 = 1

print()

# Python Strings as Sequences of Characters

language = 'Python'
a, b, c, d, e, f = language

print(a)  # Output: P
print(b)  # Output: y
print(c)  # Output: t
print(d)  # Output: h
print(e)  # Output: o
print(f)  # Output: n

print('')

# Accessing Characters in Strings by Index

abcdef = 'Python'

first_letter = abcdef[0]
print(first_letter)  # Output: P

second_letter = abcdef[1]
print(second_letter)  # Output: y

last_index = len(abcdef) - 1
last_letter = abcdef[last_index]
print(last_letter)  # Output: n

last_index = len(abcdef) - 2
last_letter = abcdef[last_index]
print(last_letter)  # Output: o

print()

# Slicing Python Strings

name = 'Python'
first_three = name[0:3]
print(first_three)  # Output: Pyt

last_three = name[3:6]
print(last_three)  # Output: hon

# another way

last_three = name[-3:]
print(last_three)  # Output: hon

last_three = name[3:]
print(last_three)  # Output: hon

print('')

greetings = 'Hello World!!!'
print(greetings)  # Output: Hello World!!!
print(greetings[::-1])  # Output: !!!dlroW olleH

print()

# Skipping Characters While Slicing

name = 'Language'

pto = name[0:7:2]
print(pto)  # Output: Lnug
