from abc import ABC, abstractmethod

# Abstract Base Class
class Car(ABC):  
    def __init__(self, brand, model):
        self.__brandname = brand  # Private attribute
        self.modelname = model

    def get_brandname(self):
        """Getter for the brand name with a humorous addition."""
        return f"{self.__brandname} - Loan pending"

    def Full_name(self):
        """Returns the full name of the car."""
        return f"The Brand name is {self.__brandname} and model is {self.modelname}"

    @abstractmethod
    def fuel_type(self):
        """Abstract method for defining fuel type."""
        pass


# Derived Class 1
class ElectricCar(Car):  
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery_capacity = battery

    def fuel_type(self):
        """Implementation of the abstract method for ElectricCar."""
        return "Electric Charge"


# Derived Class 2
class DieselCar(Car):  
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        """Implementation of the abstract method for DieselCar."""
        return "Diesel"


# Demonstrating Abstraction
# Abstract class cannot be instantiated
# my_car = Car('Generic', 'Model X')  # This would raise a TypeError

# Creating objects of derived classes
my_tesla = ElectricCar('Tesla', 'Model S', '95 KWH')
print(my_tesla.Full_name())  # Output: The Brand name is Tesla and model is Model S
print(my_tesla.get_brandname())  # Output: Tesla - Loan pending
print(f"Fuel Type: {my_tesla.fuel_type()}")  # Output: Fuel Type: Electric Charge

my_safari = DieselCar('Tata', 'Safari')
print(my_safari.Full_name())  # Output: The Brand name is Tata and model is Safari
print(my_safari.get_brandname())  # Output: Tata - Loan pending
print(f"Fuel Type: {my_safari.fuel_type()}")  # Output: Fuel Type: Diesel
