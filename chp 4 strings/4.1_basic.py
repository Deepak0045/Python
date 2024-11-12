# Creating a String

letter = 'P'
print(letter)  # Output: P
print(len(letter))  # Output: 1 (length of the string 'P')

greetings = 'Hello World!!!'
print(greetings)  # Output: Hello World!!!

sentence = 'This is a Python Coding challenge'
print(sentence)  # Output: This is a Python Coding challenge

print('')

multiline_string = '''I am a teacher
thers nothing that enjoy mpore then teaching
thats why i created this challenge '''

print(multiline_string)
# Output:
# I am a teacher
# thers nothing that enjoy mpore then teaching
# thats why i created this challenge

print()

# Concatenating Strings

first_name = 'Deepak'
last_name = "yadav"
space = ' '

full_name = first_name + space +  last_name
print(full_name)  # Output: Deepak yadav

print(len(first_name))  # Output: 6 (length of 'Deepak')
print(len(last_name))  # Output: 5 (length of 'yadav')
print(len(first_name) < len(last_name))  # Output: False (6 < 5 is False)
print(len(full_name))  # Output: 12 (length of 'Deepak yadav')

print()

# Escape Sequences in Strings

print('I hope Everyone is enjoying the python challenge. \nAre You ?')
# Output:
# I hope Everyone is enjoying the python challenge.
# Are You ?

print('Days\tTopics\tExercises')
print('Day1\t2\t5')
print('Day2\t4\t8')
print('Day3\t6\t9')
print('Day4\t8\t16')
# Output:
# Days    Topics    Exercises
# Day1    2         5
# Day2    4         8
# Day3    6         9
# Day4    8         16

print("This is a backslash (\\)' symbol")  
# Output: This is a backslash (\)' symbol

print("Every programming language starts with \"Hello, World!!!\"")
# Output: Every programming language starts with "Hello, World!!!"
