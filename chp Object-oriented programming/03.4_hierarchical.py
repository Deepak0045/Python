# 4. Hierarchical Inheritance (Both Car and ElectricCar inherit from Vehicle)
# In hierarchical inheritance, multiple child classes inherit from a single parent class. 
# Let’s add another class, LuxuryCar, which also inherits from Car.

print('Hierarchical Inheritance')

class Car:

    def __init__(self, brand, model):

        self.brandname = brand
        self.modelname = model

    def Full_name(self):
        return f'The Brand name of the car is {self.brandname} The Model of the car is {self.modelname}'
    
class Van(Car):

    def __init__(self, brand, model, seats):

        super().__init__(brand, model)
        self.total_seats = seats

    def seating_capacity(self):
        return f'The seating capacity of the van is {self.total_seats}'
    
class ElectricCar(Car):

    def __init__(self, brand, model, battery):

        super().__init__(brand, model)
        self.battery_power = battery

    def battery_capacity(self):
        return f'the battery capacity of the car is {self.battery_power}'
    
My_van = Van('Suzuki', 'Omni', '20')
print(My_van.brandname)
print(My_van.modelname)
print(My_van.Full_name())
print(My_van.seating_capacity())

my_Tesla = ElectricCar('Tesla', 'model s', '95KWH')
print(my_Tesla.brandname)
print(my_Tesla.modelname)
print(my_Tesla.Full_name())
print(my_Tesla.battery_capacity())





print('*********************************************** Explantion ************************************************************')





# Parent class Car
class Car:
    # Constructor to initialize the brand and model of the car
    def __init__(self, brand, model):
        self.brandname = brand
        self.modelname = model

    # Method to return the full name of the car
    def Full_name(self):
        return f'The Brand name of the car is {self.brandname} The Model of the car is {self.modelname}'

# Child class Van, inherits from Car
class Van(Car):
    # Constructor to initialize the brand, model, and seats (specific to Van)
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)  # Inheriting from Car class
        self.total_seats = seats  # Unique to Van

    # Method to return the seating capacity of the Van
    def seating_capacity(self):
        return f'The seating capacity of the van is {self.total_seats}'

# Child class ElectricCar, inherits from Car
class ElectricCar(Car):
    # Constructor to initialize the brand, model, and battery (specific to ElectricCar)
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  # Inheriting from Car class
        self.battery_power = battery  # Unique to ElectricCar

    # Method to return the battery capacity of the ElectricCar
    def battery_capacity(self):
        return f'the battery capacity of the car is {self.battery_power}'

# Creating an instance of the Van class
My_van = Van('Suzuki', 'Omni', '20')
# Printing details of the Van
print(My_van.brandname)            # Output: Suzuki
print(My_van.modelname)            # Output: Omni
print(My_van.Full_name())          # Output: The Brand name of the car is Suzuki The Model of the car is Omni
print(My_van.seating_capacity())   # Output: The seating capacity of the van is 20

# Creating an instance of the ElectricCar class
my_Tesla = ElectricCar('Tesla', 'model s', '95KWH')
# Printing details of the ElectricCar
print(my_Tesla.brandname)          # Output: Tesla
print(my_Tesla.modelname)          # Output: model s
print(my_Tesla.Full_name())        # Output: The Brand name of the car is Tesla The Model of the car is model s
print(my_Tesla.battery_capacity()) # Output: the battery capacity of the car is 95KWH
