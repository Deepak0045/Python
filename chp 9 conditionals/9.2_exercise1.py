# ==========================
# Exercise 1: Age and Driving Eligibility
# ==========================
# Get user input for age. If 18 or older, give feedback they can drive.
# If below 18, calculate and display how many years are left until eligible.

# Input: Enter your age: 30
# Output: You are old enough to learn to drive.
# Input: Enter your age: 15
# Output: You need 3 more years to learn to drive.

age = int(input("Enter your age: "))
minimum_age = 18
remaining_years = minimum_age - age

if age >= minimum_age:
    print('You are old enough to learn to drive.')  # Output for age >= 18
else:
    print(f'You need {remaining_years} more years to learn to drive.')  # Output for age < 18

print('')  # Blank line for better readability


# ==========================
# Exercise 2: Age Comparison
# ==========================
# Compare the values of `computer_age` and `user_age`. Determine who is older.
# Use a nested condition to print 'year' for a 1-year difference, 'years' for more,
# and a custom message for equal ages.

# Input: Enter computer age: 25
# Input: Enter user age: 30
# Output: User is 5 years older than computer.


computer_age = int(input('Enter Computer age: '))
user_age = int(input('Enter User age: '))

if computer_age > user_age:
    difference = computer_age - user_age
    print(f'Computer is {difference} {"year" if difference == 1 else "years"} older than the user.')
elif user_age > computer_age:
    difference = user_age - computer_age
    print(f'User is {difference} {"year" if difference == 1 else "years"} older than the computer.')
else:
    print('Both are the same age.')  # Output for equal ages

print('')  # Blank line for better readability


# ==========================
# Exercise 3: Comparing Two Numbers
# ==========================
# Get two numbers from the user and compare them. Print whether one is greater,
# smaller, or if they are equal.

# Input: Enter number one: 4
# Input: Enter number two: 3
# Output: 4 is greater than 3.

a = int(input('Enter A: '))
b = int(input('Enter B: '))

if a > b:
    print(f'{a} is greater than {b}')  # Output for a > b
elif a < b:
    print(f'{a} is smaller than {b}')  # Output for a < b
else:
    print(f'{a} and {b} are the same')  # Output for a == b


print('')  # Blank line for better readability

# ==========================
# Exercise 4: Grading System
# ==========================
# Assign grades based on scores.
# 80-100: Grade A
# 70-79: Grade B
# 60-69: Grade C
# 50-59: Grade D
# 0-49: Grade F

# Method 1: Explicit Conditions
grade = int(input("Enter the grade: "))

if grade >= 80 and grade <= 100:
    print('Grade A')
elif grade >= 70 and grade <= 79:
    print('Grade B')
elif grade >= 60 and grade <= 69:
    print('Grade C')
elif grade >= 50 and grade <= 59:
    print('Grade D')
elif grade >= 0 and grade <= 49:
    print('Grade F')
else:
    print('Enter a valid grade between 0 and 100')  # Output for invalid grades

print('')  # Blank line for readability

# Method 2: Simplified Range Conditions
grade = int(input("Enter the grade: "))

if 80 <= grade <= 100:
    print('Grade A')
elif 70 <= grade <= 79:
    print('Grade B')
elif 60 <= grade <= 69:
    print('Grade C')
elif 50 <= grade <= 59:
    print('Grade D')
elif 0 <= grade <= 49:
    print('Grade F')
else:
    print('Enter a valid grade between 0 and 100')  # Output for invalid grades
