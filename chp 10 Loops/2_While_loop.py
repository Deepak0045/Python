# While Loop
# The `while` loop is used to execute a block of code repeatedly as long as a specified condition is true.
# Once the condition becomes false, the loop ends, and the program continues executing the code after the loop.

# Syntax:
# while condition:
#     code to execute

# Example:

count = 0

while count < 5:  # The loop runs as long as `count` is less than 5.
    print(count)  # Print the current value of `count`.
    count += 1    # Increment `count` by 1 in each iteration.
# Output: 0, 1, 2, 3, 4

print('')

# You can include an `else` block with a `while` loop.
# The `else` block executes when the condition becomes false, unless the loop is exited with a `break` statement.

# Syntax:
# while condition:
#     code goes here
# else:
#     code goes here

# Example:

count = 0

while count < 5:  # The loop runs as long as `count` is less than 5.
    print(count)  # Print the current value of `count`.
    count += 1    # Increment `count` by 1 in each iteration.
else:
    print('Loop Ended')  # This prints when the loop condition becomes false.
# Output: 0, 1, 2, 3, 4, "Loop Ended"

print('')

# Break: The `break` statement is used to exit a loop prematurely, regardless of the condition.
print('Break: We use break when we like to get out of or stop the loop.')

count = 0

while count < 6:     # The loop runs as long as `count` is less than 6.
    print(count)     # Print the current value of `count`.
    count += 1       # Increment `count` by 1.
    if count == 4:   # When `count` equals 4:
        break        # Exit the loop immediately.
# Output: 0, 1, 2, 3

print('')

# Continue: The `continue` statement skips the current iteration and moves to the next iteration of the loop.

# Syntax:
# while condition:
#     code goes here
#     if another_condition:
#         continue

# Example:

count = 0

while count < 10:   # The loop runs as long as `count` is less than 10.
    if count == 5:  # When `count` equals 5:
        count += 1  # Increment `count` to avoid an infinite loop.
        continue    # Skip the remaining code in the loop and go to the next iteration.
    
    print(count)    # Print the current value of `count` (not equal to 5).
    count += 1      # Increment `count` by 1 in each iteration.
# Output: 0, 1, 2, 3, 4, 6, 7, 8, 9 (skips 5)

