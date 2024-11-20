# Break and Continue - Part 2

# Short reminder:
# Break: Used to stop the loop before it is completed.

# Syntax:
# for iterator in sequence:
#     code goes here
#     if condition:
#         break

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in numbers:       # Loop iterates over each number in the tuple `numbers`.
    print(num)            # Print the current number.
    if num == 6:          # Check if the number equals 6.
        break             # Stop the loop if the condition is met.
# Output: 1, 2, 3, 4, 5, 6

print('In the above example, the loop stops when it reaches 6.')

print('')

# Continue: Used to skip some steps in the iteration of the loop.

for num in numbers:       # Loop iterates over each number in the tuple `numbers`.
    if num == 6:          # Check if the number equals 6.
        num += 1          # Increment `num` (though this has no effect on the iteration since `for` loops use the iterator value).
        continue          # Skip the remaining code and proceed to the next iteration.
    print(num)            # Print the number if it is not skipped by `continue`.

print('')  # Output: 1, 2, 3, 4, 5, 7, 8, 9, 10 (6 is skipped)

print('Example 2')
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in numbers:   # Loop iterates through each number in the tuple `numbers`.
    print(num)        # Print the current number.

    if num == 7:      # Check if the current number is " 7 ". "# THALA FOR A REASON"
        continue      # If true, skip the remaining code in the loop and proceed to the next iteration.

    print('Next Number should be', num + 1) if num != 9 else print("Loop's End")
    # Conditional expression:
    # - If `num` is not 9, print "Next Number should be <num + 1>".
    # - If `num` is 9, print "Loop's End".
    
print('outside the loop')  # This is executed after the loop is complete.


# Output:
# 1, 
# Next Number should be 2
# 2, 
# Next Number should be 3
# 3, 
# Next Number should be 4
# 4, 
# Next Number should be 5
# 5, 
# Next Number should be 6
# 6, 
# Next Number should be 7
# 7
# 8, 
# Next Number should be 9
# 9, 
# Loop's End
# 10
# outside the loop
