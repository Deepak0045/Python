print('Polymorphism')
print('Demonstrating polymorphism by defining a method `fuel_type` in both `Car` and `ElectricCar` classes with different behaviors.')
print('')

class Car:
    def __init__(self, brand, model):
        self.__brandname = brand
        self.modelname = model

    def get_brandname(self):
        return self.__brandname + ' !!!!!!!!!!!!!!!'

    def name(self):
        return f'{self.__brandname} and {self.modelname}'

    def fuel_type(self):
        return 'Petrol or Diesel'


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery_size = battery

    def fuel_type(self):
        return 'Electric Charge'


# Demonstrating Polymorphism
# Car Instance
safari = Car('Tata', 'Safari')
print(f'{safari.name()} - Fuel Type: {safari.fuel_type()}')  # Output: Tata Safari - Fuel Type: Petrol or Diesel

# ElectricCar Instance
tesla = ElectricCar('Tesla', 'Model S', '85 KWH')
print(f'{tesla.name()} - Fuel Type: {tesla.fuel_type()}')  # Output: Tesla Model S - Fuel Type: Electric Charge
