# Multilevel Inheritance (Truck inherits from ElectricCar, which inherits from Car)
# In multilevel inheritance, a class inherits from a child class, forming a chain of inheritance. 
# Let’s create a Truck class that inherits from ElectricCar, which in turn inherits from Car.

print('Multilevel Inheritence')

class Car:

    def __init__(self, brand, model):
        self.brandname = brand
        self.modelname = model

    def Full_name(self):
        return f'The Name of the brand is {self.brandname} and model is {self.modelname}'
    
class ElectricCar(Car):

    def __init__(self, brand, model, battery):

        super().__init__(brand, model)
        self.battery_size = battery

    def battery_info(self):
        return f'Battery capacity is {self.battery_size}'
    
class Truck(ElectricCar):

    def __init__(self, brand, model, battery, load):
        
        super().__init__(brand, model, battery)
        self.load_capacity = load


    def load_info(self):
        return f'The load capacity of Truck is {self.load_capacity}'

my_Truck = Truck('Tata', 'Supreme', '1000KWH', '100TON')


print(my_Truck.brandname)
print(my_Truck.modelname)
print(my_Truck.battery_size)
print(my_Truck.Full_name())
print(my_Truck.battery_info())
print(my_Truck.load_info())



print('*********************************************** Explantion ************************************************************')



print('Multilevel Inheritance')

# Base class: Car
class Car:

    # Constructor (__init__) to initialize the brand and model of the car
    
    def __init__(self, brand, model):
        self.brandname = brand   # Instance variable to store brand name
        self.modelname = model   # Instance variable to store model name

    # Method to return full name of the car including brand and model
    def Full_name(self):
        return f'The Name of the brand is {self.brandname} and model is {self.modelname}'

# Derived class: ElectricCar inherits from Car
class ElectricCar(Car):
    # Constructor to initialize brand, model, and battery size
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  # Call constructor of the parent class (Car)
        self.battery_size = battery    # Instance variable to store battery size

    # Method to return battery information
    def battery_info(self):
        return f'Battery capacity is {self.battery_size}'

# Further derived class: Truck inherits from ElectricCar
class Truck(ElectricCar):
    # Constructor to initialize brand, model, battery, and load capacity
    def __init__(self, brand, model, battery, load):
        super().__init__(brand, model, battery)  # Call constructor of ElectricCar class
        self.load_capacity = load   # Instance variable to store load capacity

    # Method to return load capacity information
    def load_info(self):
        return f'The load capacity of Truck is {self.load_capacity}'

# Create an object of the Truck class with brand, model, battery, and load
my_Truck = Truck('Tata', 'Supreme', '1000KWH', '100TON')

# Output details of the Truck
print(my_Truck.brandname)     # Output: Tata
print(my_Truck.modelname)     # Output: Supreme
print(my_Truck.battery_size)  # Output: 1000KWH
print(my_Truck.Full_name())   # Output: The Name of the brand is Tata and model is Supreme
print(my_Truck.battery_info())# Output: Battery capacity is 1000KWH
print(my_Truck.load_info())   # Output: The load capacity of Truck is 100TON
