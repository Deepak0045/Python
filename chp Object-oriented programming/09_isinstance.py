print('Class inheritance and isinstance() Function')
print('Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.')
print('')

# Base Car class
class Car:

    total_car = 0  # Class-level variable

    def __init__(self, brand, model):
        # Private attributes for brand and model
        self.__brandname = brand
        self.__modelname = model
        Car.total_car += 1

    @property
    def modelname(self):
        # Read-only property for the car's model name
        return self.__modelname

    def fuel_type(self):
        # Instance method to return default fuel type
        return 'petrol or diesel'

    @staticmethod
    def general_desciption():
        # Static method to return a general description
        return 'I Love mustang'


# Subclass of Car
class ElectricCar(Car):
    
    def __init__(self, brand, model, battery):
        # Call parent class's constructor
        super().__init__(brand, model)
        self.battery_size = battery  # Additional attribute for battery size

    def fuel_type(self):
        # Override method to specify electric fuel type
        return 'Electric Charge'


# Creating a Car instance
my_car = Car('Tata', 'Harrier')
print(my_car.modelname)  # Output: Harrier
print(my_car.fuel_type())  # Output: petrol or diesel

# Creating an ElectricCar instance
my_tesla = ElectricCar('Tesla', 'Model S', '87 kWh')


# Check if instances belong to specified classes using isinstance()

print('**************Check instance*************')
print(isinstance(my_car, Car))  # Output: True - `my_car` is an instance of the Car class
print(isinstance(my_tesla, ElectricCar))  # Output: True - `my_tesla` is an instance of ElectricCar
print(isinstance(my_tesla, Car))  # Output: True - `my_tesla` is also an instance of Car due to inheritance

