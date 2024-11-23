
print('Property Decorators')
print('Demonstrating the use of a property decorator in the `Car` class to make the `model` attribute read-only.')
print('')

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brandname = brand  # Private attribute for brand name
        self.__modelname = model  # Private attribute for model name
        Car.total_car += 1

    def get_brandname(self):
        return f'Brand: {self.__brandname}'

    def name(self):
        return f'{self.__brandname} {self.__modelname}'

    def fuel_type(self):
        return 'Petrol or Diesel'

    @staticmethod
    def general_description():
        return 'I love Ford Mustang'

    @property
    def model(self):
        """Getter for the model attribute to make it read-only."""
        return self.__modelname


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  # Initialize parent class attributes
        self.battery_size = battery  # Additional attribute for ElectricCar

    def fuel_type(self):
        return 'Electric Charge'


# Demonstrating Property Decorators
my_car = Car('Tata', 'Nexon')

# Access the `model` attribute using the property
print(f"Car Model (read-only): {my_car.model}")  # Output: Nexon

# Attempt to modify the read-only `model` attribute
try:
    my_car.model = 'Hexa'  # This should raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: can't set attribute


# Demonstrating Polymorphism with ElectricCar
my_tesla = ElectricCar('Tesla', 'Model S', '85 KWH')
print(f"Electric Car Model: {my_tesla.model}")  # Output: Model S
print(f"Electric Car Fuel Type: {my_tesla.fuel_type()}")  # Output: Electric Charge

# Display a static method
print(Car.general_description())  # Output: I love Ford Mustang
