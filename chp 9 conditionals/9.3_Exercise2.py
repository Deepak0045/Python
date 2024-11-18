# The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
# method 1

fruits = ['banana', 'orange', 'mango', 'lemon']

name = str(input("Enter the fruits name : "))


if name in fruits:
    print('The fruit already exists in the list')

elif name not in fruits:
    fruits.append(name)
    print(fruits)

else:
    print('the the correct name')

print('')

# method 2

# Initial list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Take input from the user
new_fruit = input('Enter a fruit name: ')

# Check if the input is a string and contains only alphabetic characters
if new_fruit.isalpha():
    
    # Check if the fruit is already in the list
    if new_fruit in fruits:
        print('That fruit already exists in the list')
    else:
        fruits.append(new_fruit)
        print('Fruit added to the list:', fruits)
else:
    print('Please enter a valid fruit name')
