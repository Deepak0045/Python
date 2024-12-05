# List Comprehension
# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. 
# List comprehension is considerably faster than processing a list using the for loop.


# syntax
# [i for i in iterable if expression]
# Example:1

# there are two ways to create a list 



print('********** EXAMPLE 1 *****************')


# Method 1

language = 'Java'
print(language)
print(type(language))

print('')

lst = list(language)
print(lst)
print(type(lst))

print('')

# Method 2 : List comprehension

language2 = 'Python'

lst2 = [i for i in language2]
print(type(lst2))
print(lst2)
print('')


print('********** EXAMPLE 2 *****************')
print('')


# Method 1
team1 = 'Australia'

winner = []

for i in team1:
    winner.append(i)

print(winner)

# Method 2

team2 = 'India'

winner2 = [i for i in team2]

print(winner2)


print("------------------------------------------------")

# Method 1: Using a for loop to create a list of characters from a string
team1 = 'Australia'  # A string representing the team name

# Initialize an empty list to store the characters
winner = []

# Iterate over each character in the string 'team1'
for i in team1:
    winner.append(i)  # Append each character to the list 'winner'

# Print the list containing characters of the string 'Australia'
print(winner)  # Output: ['A', 'u', 's', 't', 'r', 'a', 'l', 'i', 'a']

# Method 2: Using list comprehension to achieve the same result
team2 = 'India'  # A string representing another team name

# Create a list of characters directly using list comprehension
winner2 = [i for i in team2]  # For each character in 'team2', add it to the list

# Print the list containing characters of the string 'India'
print(winner2)  # Output: ['I', 'n', 'd', 'i', 'a']

