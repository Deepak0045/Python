# 1. Single Inheritance (ElectricCar inherits from Car)
# In single inheritance, a child class inherits from a single parent class. Let's use the ElectricCar class which inherits from Car.



print('Inheritence')
print('create an electric car class that inherits Car class and has an additional attributes - battery_size')
print('')

print('Single Inheritence')

class Car:

    def __init__(self, Brand, Model):

        self.brandname = Brand
        self.modelname = Model

    def Full_name(self):
        return f'the name of the brand is {self.brandname} and model name is {self.modelname}'
    

class ElectricCar(Car):

    def __init__(self, Brand, Model, Battery):

        super().__init__(Brand, Model)
        self.battery_size = Battery



My_tesla =  ElectricCar('Tesla', 'Model S', '90 KWH')

print(My_tesla.brandname)
print(My_tesla.modelname)
print(My_tesla.battery_size)
print(My_tesla.Full_name())



print('*********************************************** Explantion ************************************************************')


# Print statement to describe the purpose of the code
print('Class inheritance and self')
print('Create an ElectricCar class that inherits from Car class and adds an additional attribute - battery_size')
print()

# Defining the Car class
class Car:

    # The __init__ method is the constructor to initialize attributes (brand and model)
    def __init__(self, Brand, Model):
        # Instance variables (attributes) to store brand and model of the car
        self.brandname = Brand
        self.modelname = Model

    # Method to display the full name of the car (brand and model)
    def Full_name(self):
        # Returns the formatted string showing the brand and model names
        return f'the name of the brand is {self.brandname} and model name is {self.modelname}'

# Defining the ElectricCar class that inherits from the Car class
class ElectricCar(Car):

    # The __init__ method initializes the brand, model, and battery size attributes
    def __init__(self, Brand, Model, Battery):

        # Using super() to call the constructor of the parent (Car) class
        super().__init__(Brand, Model)
        
        # Adding an additional attribute for battery size specific to ElectricCar
        self.battery_size = Battery


# Creating an object of the ElectricCar class with 'Tesla' as the brand, 'Model S' as the model, and '90 KWH' as the battery size
My_tesla = ElectricCar('Tesla', 'Model S', '90 KWH')

# Printing individual attributes of the electric car object (brand, model, and battery size)
print(My_tesla.brandname)     # Output: Tesla
print(My_tesla.modelname)     # Output: Model S
print(My_tesla.battery_size)  # Output: 90 KWH

# Calling the Full_name method from the parent Car class to display the brand and model together
print(My_tesla.Full_name())   # Output: the name of the brand is Tesla and model name is Model S
