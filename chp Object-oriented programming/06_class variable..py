
print('class variable')
print('Add a class variable to Car that keeps track of the number of cars created')
print('')



class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brandname = brand
        self.modelname = model
        Car.total_car += 1
    
    
    def get_brandname(self):
        return self.__brandname + ' !!!!!!!!!!!!!!!'
    
    def name(self):
        return f'{self.__brandname} and {self.modelname}'

    def fuel_type(self):
        return 'petrol or diesel'



class ElectricCar(Car):
    
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery_size = battery

    def fuel_type(self):
        return 'Electric Charge'


my_car = Car('Tata', 'Harrier')
print(my_car.modelname)
print(my_car.fuel_type())

my_second_car = Car('Tata', 'safari')
print(my_second_car.modelname)
print(my_second_car.fuel_type())

my_tesla = ElectricCar('Tesla', 'Models s', '85KWH')
print(my_tesla.modelname)
print(my_tesla.fuel_type())

# test = Car('test', 'test')
# print(test.total_car)       not good because it will count  itself

print(my_car.total_car)



print('*********************************************** Explantion ************************************************************')


print('class variable')
print('Add a class variable to Car that keeps track of the number of cars created')
print('')

# Define the Car class

class Car:

    total_car = 0

    # Constructor to initialize the brand and model of the car
    def __init__(self, brand, model):

        self.__brandname = brand  # Private attribute (encapsulated)
        self.modelname = model    # Public attribute
        Car.total_car += 1
    
    # Getter method to access the private brand name
    def get_brandname(self):
        return self.__brandname + ' !!!!!!!!!!!!!!!'
    
    # Method to return the full name of the car (brand and model)
    def name(self):
        return f'{self.__brandname} and {self.modelname}'

    # Fuel type method for the general car, returns 'petrol or diesel'
    def fuel_type(self):
        return 'petrol or diesel'


# Define the ElectricCar class, inheriting from the Car class
class ElectricCar(Car):

    # Constructor to initialize brand, model, and battery size
    def __init__(self, brand, model, battery):
        
        super().__init__(brand, model)  # Calling the parent class constructor
        self.battery_size = battery    # Additional attribute for electric car
    
    # Overriding the fuel_type method for ElectricCar
    def fuel_type(self):
        return 'Electric Charge'  # Different behavior compared to the parent class

# Create an instance of the Car class
my_car = Car('Tata', 'Harrier')

# Accessing private and public attributes
print(my_car._Car__brandname)  # Accessing the private attribute using name mangling
print(my_car.get_brandname())  # Using the getter method to access brand name
print(my_car.modelname)        # Accessing the public model name attribute
print(my_car.fuel_type())      # Calling the fuel_type method (parent class behavior)

# Create an instance of the ElectricCar class
my_tesla = ElectricCar('Tesla', 'Models s', '85KWH')

# Accessing ElectricCar specific methods and attributes
print(my_tesla.get_brandname())  # Using the getter method (inherited)
print(my_tesla.modelname)        # Accessing inherited public attribute
print(my_tesla.fuel_type())      # Calling the overridden fuel_type method (child class behavior)
print(my_car.total_car)