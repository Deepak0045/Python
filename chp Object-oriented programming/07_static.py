print('')
print('add a static method to the car class that return a general description of a car')

# a static method is a type of method defined within a class that does not depend on an instance of the class and 
# cannot access or modify instance-level (object-specific) data.



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
    
    @staticmethod
    def general_desciption():
        return 'I Love mustang'



class ElectricCar(Car):
    
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery_size = battery

    def fuel_type(self):
        return 'Electric Charge'


my_car = Car('Tata', 'Harrier')
print(my_car.modelname)
print(my_car.fuel_type())

#print(my_car.general_desciption())
print(Car.general_desciption())




# A static method is defined within a class but is not tied to any specific instance of the class. 
# It can be called using the class name directly without needing to create an object.
# Static methods cannot access or modify instance-level data or methods (like self or instance attributes).
# They are typically used for utility or general-purpose methods related to the class.

class Car:

    total_car = 0  # Class-level variable to count total cars (shared by all instances)

    def __init__(self, brand, model):
        self.__brandname = brand  # Private attribute for brand name
        self.modelname = model    # Model name of the car
        Car.total_car += 1        # Increment total car count when a new car is created

    def get_brandname(self):
        # Instance method to return the brand name with some formatting
        return self.__brandname + ' !!!!!!!!!!!!!!!'
    
    def name(self):
        # Instance method to return a formatted string with brand and model name
        return f'{self.__brandname} and {self.modelname}'

    def fuel_type(self):
        # Instance method that returns the default fuel type for cars
        return 'petrol or diesel'
    
    @staticmethod
    def general_desciption():
        # Static method: Does not depend on any instance-level data.
        # It can be called using the class name directly.
        return 'I Love mustang'  # Returns a general description of a car


# ElectricCar inherits from Car
class ElectricCar(Car):
    
    def __init__(self, brand, model, battery):
        # Calls the parent class's constructor to initialize brand and model
        super().__init__(brand, model)
        self.battery_size = battery  # Additional attribute specific to ElectricCar

    def fuel_type(self):
        # Overrides the fuel_type method in the parent class
        return 'Electric Charge'


# Create an instance of Car
my_car = Car('Tata', 'Harrier')
print(my_car.modelname)  # Access the model name of the car instance
print(my_car.fuel_type())  # Calls the instance method to get the fuel type

# Demonstrating the use of the static method
# Static methods are called using the class name
print(Car.general_desciption())  # Output: I Love mustang
