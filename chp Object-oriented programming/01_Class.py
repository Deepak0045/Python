print('Basic class and object')
print('Create a car class with attributes like brand and model. Then create an instance of this class')
print('')



class Car:

    def __init__(self, Brand, model):

        self.Brandname = Brand
        self.Modelname = model


my_car = Car('Toyota', 'Fortuner')

print(my_car)

print(my_car.Brandname)
print(my_car.Modelname)


print('*********************************************** Explantion ************************************************************')


# Define a class named Car. 
# A class is a blueprint for creating objects that share common attributes and behaviors.

class Car:

    # The constructor method, __init__, is used to initialize objects.
    # It is called automatically when an object is created.

    def __init__(self, Brand, model):
        
        # Instance variables (attributes) to store data specific to an object.
        # These variables belong to the object created from this class.
        
        self.Brandname = Brand  # Assigns the value of Brand to the Brandname attribute.
        self.Modelname = model  # Assigns the value of model to the Modelname attribute.

# Create an object (instance) of the Car class.
# An object is a specific instance of a class with defined values for its attributes.
my_car = Car('Toyota', 'Fortuner')

# Print the object. This will output a memory reference unless the __str__ or __repr__ method is defined in the class.
print(my_car)

# Access and print the value of the Brandname attribute of the my_car object.
# This demonstrates how to access the attributes of an object using the dot notation.
print(my_car.Brandname)

# Access and print the value of the Modelname attribute of the my_car object.
# Dot notation is also used here to access another attribute.
print(my_car.Modelname)
