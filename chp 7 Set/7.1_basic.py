# Sets
# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
# The Mathematics definition of a set can be applied also in Python. 
# Set is a collection of unordered and un-indexed distinct elements. 
# In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

# Creating a Set
# We use the set() built-in function.

# Creating an empty set
# # syntax
# st = set()
# Creating a set with initial items
#  syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# Example:

languages = {'hindi', 'marathi', 'english' , 'Japenese'}
print(languages)
print(type(languages))
print('')


# Checking an Item
# To check if an item exist in a list we use in membership operator.

# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
# Example:

languages = {'hindi', 'marathi', 'english' , 'Japenese'}
print('marathi' in languages)


# Adding Items to a Set
# Once a set is created we cannot change any items and we can also add additional items.

# Add one item using add()

print(languages)
languages.add('French')
print(languages)


# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.

languages.update(['bangla', 'bhojpuri', 'punjabi'])
print(languages)
print('')

# Removing Items from a Set
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, 
# so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.

# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item2')


languages = {'english', 'marathi', 'French', 'hindi', 'bangla', 'punjabi', 'Japenese', 'bhojpuri'}
languages.remove('bangla')
print(languages)

# The pop() methods remove a random item from a list and it returns the removed item.

languages.pop()
print(languages)
