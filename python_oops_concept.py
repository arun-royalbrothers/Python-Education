class Sample:
    full_name = "Arun Arunisto" #This is class attribute
    def __init__(self, name): #Initializing/creating instance attribute
        self.name = name #instance attribute

obj = Sample("Arun") #Instantiate means creating an object using class

#object can access class attribute and instance attribute like below
print(obj.name) #instance attribute
print(obj.full_name) #class attribute

#you can change attributes value dynamically
obj.name = "Arun Arunisto"
obj.full_name = "Arun"
print(obj.name)
print(obj.full_name)

#so the objects are mutable because it can change dynamically

#### Dunder method __str__ representation ###
class Person:
    species = "Homosapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def details(self):
        return f"Name : {self.name} | Age:{self.age}"

    #Another instance method
    def name_change(self, name):
        self.name = name

    #this will represent the object
    def __str__(self):
        return f"Name: {self.name}"

per1 = Person("Arun", 25)
print(per1.details())
per1.name_change("Arun Arunisto")
print(per1.details())
print(per1) #it will return a crytic type output shows where object saves in memory
#but you can set the print option of an object by creating a __str__() method
print(per1) #printing after the __str__() method

#these type of methods (__init__, __str__) are called dunder methods
#there are lots of dunder methods -> understanding the dunder methods is one of the key for mastering in oops

### Name Mangling ###
class Sample:
    #name mangling is the process declaring methods/attributes public, non-public, or private
    def __init__(self, name):
        self.__name = name #private instance attributes

    def __details(self): #private instance method
        return self.__name

    def __str__(self):
        return self.__name

    def __doc__(self):
        return "Class to demonstrate Name Mangling"


obj = Sample("Aruunisto")
print(obj)
print(vars(obj))
print(vars(Sample))

#you can't access private/non-public attributes/methods
#but they're not strictly private you can access them by their mangled names
print(obj._Sample__name)
print(obj._Sample__details())


"""
class : class is a blueprint for creating objects.
        it defines the attributes (data) and methods
        (function) that the objects will have
object: object is an instance of a class
"""
#sample
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

#creating objects of the class
car_1 = Car("Toyota", "Corolla")
car_2 = Car("Tesla", "Model S")

#calling methods on object
car_1.drive()
car_2.drive()

"""
Inheritance
Inheritance allows a class(sub class) to inherit
attributes and methods from another class (super class)
"""
class Employee_details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def emp_details(self):
        print("Employee name:",self.name)
        print("Employee age:",self.age)

class Employee_designation(Employee_details):
    def __init__(self, name, age, designation, salary):
        Employee_details.__init__(self, name, age)
        self.designation = designation
        self.salary = salary

    def emp_details_with_designation(self):
        print("Employee name:",self.name)
        print("Employee age:",self.age)
        print("Employee designation:",self.designation)
        print("Employee salary:",self.salary)

#calling subclass on object
emp_1 = Employee_designation("Arunisto", 25, "Developer", "$60k")

#accessing child method
emp_1.emp_details_with_designation()
#accessing parent class too
emp_1.emp_details()
print(emp_1.name)

"""
Encapsulation:
Encapsulation is the bundling data and methods on that single unit class
"""
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance #private variable

    def deposit_amount(self, amt):
        self.__balance+=amt

    def withdraw_amount(self, amt):
        self.__balance-=amt

    def get_balance(self):
        return self.__balance

acc_1 = BankAccount("12345", 5000)
print(acc_1.get_balance())
acc_1.deposit_amount(100)
print(acc_1.get_balance())
print(acc_1._BankAccount__balance) #accessing private variable

    
