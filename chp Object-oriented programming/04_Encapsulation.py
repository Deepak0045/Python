print('Encapsulation')
print('Modify the car class to encapsulate the brand atrribute, making it privatte and provide a getter method for it')
print('')


class Car:

    def __init__(self, brand, model):
        self.__brandname = brand
        self.modelname = model
    
    def name(self):
        return f'{self.__brandname} and {self.modelname}'

    def get_brandname(self):
        return self.__brandname + ' !!!!!!!!!!!!!!!'
    
    def set_brandname(self, new_brand):
        if isinstance(new_brand, str) and new_brand.strip():
            self.__brandname = new_brand
        else:
            return ValueError ('The brand name must be a non-empty string')


class ElectricCar(Car):
    
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery_size = battery



# new_car = Car('toyota', 'corolla')
# print(new_car.brandname)
# print(new_car.modelname)



print('')

tesla = ElectricCar('Tesla', 'model S', '45 KWH')

#print(tesla.__brandname) direcy access isnt allowed
print(tesla.get_brandname())

# Modifying the brandname using the setter method
#tesla.set_brandname(9)    #  ValueError: The brand name must be a non-empty string


# Modifying the brandname using the setter method
tesla.set_brandname('Tesla Motors')
print(tesla.get_brandname())


print('*********************************************** Explantion ************************************************************')



class Car:

    def __init__(self, Brand, Model):
        # Private attribute __brandname, name-mangled to _Car__brandname
        self.__brandname = Brand
        self.modelname = Model


    def get_brandname(self):
        # Getter method to access the private __brandname
        return self.__brandname + '   !!!'


    def set_brandname(self, new_brand):

        # Setter method to modify the private __brandname

        if isinstance(new_brand, str) and new_brand.strip():
            self.__brandname = new_brand
        else:
            raise ValueError('The brand name must be a non-empty string')


    def Full_name(self):
        return f'the name of the brand is {self.__brandname} and model name is {self.modelname}'


class ElectricCar(Car):

    def __init__(self, Brand, Model, Battery):
        super().__init__(Brand, Model)  # Calls the __init__ of the Car class
        self.battery_size = Battery


# Creating an ElectricCar object
My_tesla = ElectricCar('Tesla', 'Model S', '90 KWH')

# Accessing the private variable using the getter method
print(My_tesla.get_brandname())  # Output: Tesla   !!!

# Modifying the brandname using the setter method
#My_tesla.set_brandname(9)    #  ValueError: The brand name must be a non-empty string


# Modifying the brandname using the setter method
My_tesla.set_brandname('Tesla Motors')


# Verifying the updated brandname
print(My_tesla.get_brandname())  # Output: Tesla Motors   !!!

# Accessing the private variable directly using the name-mangled version
print(My_tesla._Car__brandname)  # Output: Tesla Motors
