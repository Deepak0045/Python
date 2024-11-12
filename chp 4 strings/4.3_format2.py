# capitalize(): Converts the first character of the string to capital letter

challenge = '30 Days Of python'
print(challenge.capitalize())  # Output: 30 days of python

print()

# count(): Returns occurrences of substring in string, count(substring, start=.., end=..)

challenge2 = 'thirty Days Of python'
print(challenge2.count('th'))  # Output: 2

print(challenge2.count('th', 0, 5))  # Output: 1

print()

# endswith(): Checks if a string ends with a specified ending

challenge3 = 'thirty days of python'
print(challenge3.endswith('on'))  # Output: True

print(challenge3.endswith('py'))  # Output: False

print()
print()

# find(): Returns the index of the first occurrence of a substring, if not found returns -1

challenge4 = 'thirty days of python'
print(challenge4.find('r'))  # Output: 2

print(challenge4.find('y'))  # Output: 5

print()

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1

challenge5 = 'thirty days of python'
print(challenge5.rfind('h'))  # Output: 21

print(challenge5.rfind('y'))  # Output: 16

print()

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314