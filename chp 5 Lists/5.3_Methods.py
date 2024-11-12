# Adding Items to a List
# The append() method adds an item to the end of the list.

# syntax
# lst = list()
# lst.append(item)

players = ['rohit', 'kohli', 'sachin', 'dhoni']
print(players)  # Output: ['rohit', 'kohli', 'sachin', 'dhoni']

# Adding an item to the end of the list
players.append('Bhumrah')
print(players)  # Output: ['rohit', 'kohli', 'sachin', 'dhoni', 'Bhumrah']

# Inserting Items into a List
# The insert() method inserts an item at a specified index. Other items shift to the right.

# syntax
# lst = ['item1', 'item2']
# lst.insert(index, item)

players = ['rohit', 'kohli', 'sachin', 'dhoni']
players.insert(1, 'Babar Azam')
print(players)  # Output: ['rohit', 'Babar Azam', 'kohli', 'sachin', 'dhoni']

# Removing Items from a List
# The remove() method removes a specified item from the list.

# syntax
# lst = ['item1', 'item2']
# lst.remove(item)

players = ['rohit', 'Babar Azam', 'kohli', 'sachin', 'dhoni']
players.remove('Babar Azam')
print(players)  # Output: ['rohit', 'kohli', 'sachin', 'dhoni']

# Removing Items Using Pop
# The pop() method removes an item at a specified index or the last item if index is not specified.

players = ['rohit', 'Babar Azam', 'kohli', 'sachin', 'dhoni']
players.pop(1)  # Removes 'Babar Azam' at index 1
print(players)  # Output: ['rohit', 'kohli', 'sachin', 'dhoni']

# Removing Items Using Del
# The del keyword removes an item at a specified index or a range of items, or it can delete the entire list.

# syntax
# lst = ['item1', 'item2']
# del lst[index]  # removes a single item
# del lst         # deletes the entire list

players = ['rohit', 'Babar Azam', 'kohli', 'sachin', 'dhoni']
del players[1]  # Removes 'Babar Azam' at index 1
print('After using del:', players)  # Output: ['rohit', 'kohli', 'sachin', 'dhoni']

# Deleting the entire list
del players
# print(players)  # This would cause an error since 'players' list is deleted

print()

# Clearing List Items
# The clear() method empties the list, making it an empty list.

# syntax
# lst = ['item1', 'item2']
# lst.clear()

players = ['rohit', 'Babar Azam', 'kohli', 'sachin', 'dhoni']
players.clear()
print(players)  # Output: []

print('')

# Joining Lists
# We can join multiple lists using the '+' operator.

# syntax
# list3 = list1 + list2

neg_num = [-5, -4, -3, -2, -1]
zero = [0]
posi_num = [1, 2, 3, 4, 5]

# Joining lists with '+' operator
integers = neg_num + zero + posi_num
print(integers)  # Output: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Another way to directly print concatenated lists
print(neg_num + zero + posi_num)  # Output: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

print('')

# Joining Using extend() Method
# The extend() method allows adding elements from another list to the end of an existing list.

# syntax
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2)

num1 = [4, 5, 6]
num2 = [1, 2, 3]
num1.extend(num2)  # Appends elements of num2 to num1
print(num1)  # Output: [4, 5, 6, 1, 2, 3]

print()

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

# Extending with multiple lists
negative_numbers.extend(zero)               # Adds zero list to negative_numbers
negative_numbers.extend(positive_numbers)  # Adds positive_numbers list to negative_numbers
print(negative_numbers)  # Output: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
