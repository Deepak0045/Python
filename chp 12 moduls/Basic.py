# What is a Module
# A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

# Creating a Module
# To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py

import mymodule


print(mymodule.generate_name('Deepak', 'Yadav'))

print(mymodule.sum_of_two(9,9))

from mymodule import generate_name as fullname , sum_of_two as total 

print(fullname('Tony', 'Stark'))
print(total(9999 , 9090))