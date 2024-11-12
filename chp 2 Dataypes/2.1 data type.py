# Checking Data types and Casting

Name = "Deepak Yadav"
Age = 23
is_married = False
skills = ['HTML', "CSS", 'Javascript', 'Python']
personal_info = {
    'Name' : 'Deepak',
    'Age' : 23,
    'is_married' : False,
    'sklls' : ['HTML', "CSS", 'Javascript', 'Python']
}

print('First Name : ', Name)
print(type(Name))

print('Age : ', Age)
print(type(Age))

print('Married : ', is_married)
print(type(is_married))

print('Skills : ', skills)
print(type(skills))

print('Personal Information : ', personal_info)
print(type(personal_info))

print('')
print('')

# Casting: Converting one data type to another data type. We use int(), float(), str(), list, set
# When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error.
# If we concatenate a number with a string, the number should be first converted to a string. 
# We will talk about concatenation in String section.

# int to float

num = 10
num_float = float(num)
print(num_float)

print('')

# float to int

nummm = 10.5
print(int(nummm))


print('')
# int to str

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  
print(type(num_str))


print('')

new_str = 10

num_strrr = int(new_str)
print(num_strrr)
print(type(num_strrr))

num_foatttt = float(new_str)
print(num_foatttt)
print(type(num_foatttt))



