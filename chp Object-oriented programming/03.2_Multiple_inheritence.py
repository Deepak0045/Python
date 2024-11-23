# 2. Multiple Inheritance (ElectricCar inherits from both Car and Battery)
# In multiple inheritance, a child class inherits from more than one parent class. 
# Let's add a Battery class and make ElectricCar inherit from both Car and Battery.

print('********** Multiple Inheritence **********')

class Car:

    def __init__(self, brand, model):

        self.brandname = brand
        self.modelname = model

    def Full_name(self):
        return f'the brand name is {self.brandname} and model is {self.modelname}'
    
class Battery:

    def __init__(self, battery):
        self.battery_size = battery

    def battery_info(self):
        return f'the battery Capacity is {self.battery_size}'
    
class ElectricCar(Car, Battery):

    def __init__(self, brand, model, battery):

        Car.__init__(self, brand, model)
        Battery.__init__(self, battery)

my_new_tesla = ElectricCar('Tesla', 'Model S', '95KWH')

print(my_new_tesla.brandname)
print(my_new_tesla.modelname)
print(my_new_tesla.battery_size)
print(my_new_tesla.Full_name())
print(my_new_tesla.battery_info())



print('*********************************************** Explantion ************************************************************')



# Parent class Car
class Car:
    def __init__(self, brand, model):
        # Instance variables for car brand and model
        self.brandname = brand
        self.modelname = model

    def Full_name(self):
        # Method to return the full name of the car
        return f'The brand name is {self.brandname} and model is {self.modelname}'

# Another class Battery
class Battery:
    def __init__(self, battery):
        # Instance variable for battery size
        self.battery_size = battery

    def battery_info(self):
        # Method to return battery information
        return f'The battery capacity is {self.battery_size}'

# Child class ElectricCar inheriting from both Car and Battery
class ElectricCar(Car, Battery):
    def __init__(self, brand, model, battery):
        # Calling parent constructors to initialize brand, model, and battery size
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery)

# Creating an object of the ElectricCar class
my_new_tesla = ElectricCar('Tesla', 'Model S', '95KWH')

# Accessing attributes and methods from both parent classes
print(my_new_tesla.brandname)    # Tesla (from Car)
print(my_new_tesla.modelname)    # Model S (from Car)
print(my_new_tesla.battery_size)  # 95KWH (from Battery)
print(my_new_tesla.Full_name())  # The brand name is Tesla and model is Model S (from Car)
print(my_new_tesla.battery_info())  # The battery capacity is 95KWH (from Battery)
