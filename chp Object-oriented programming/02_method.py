print('Class method and self')
print('add a method to the car class that displays the name of the car (brand and model)')
print()



class Car:

    def __init__(self, Brand, Model):

        self.brandname = Brand
        self.modelname= Model

    def Full_name(self):
        return f'the name of the brand is {self.brandname} and model name is {self.modelname}'
    

My_car = Car('Tata', 'harrier')

print(My_car.brandname)
print(My_car.modelname)
print(My_car.Full_name())


print('*********************************************** Explantion ************************************************************')



print('Class method and self')
print('add a method to the car class that displays the name of the car (brand and model)')
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


# Creating an object of the Car class with 'Tata' as the brand and 'harrier' as the model
My_car = Car('Tata', 'harrier')

# Printing individual attributes of the car object (brand and model)
print(My_car.brandname)  # Output: Tata
print(My_car.modelname)  # Output: harrier

# Calling the Full_name method to display the brand and model together
print(My_car.Full_name())  # Output: the name of the brand is Tata and model name is harrier
