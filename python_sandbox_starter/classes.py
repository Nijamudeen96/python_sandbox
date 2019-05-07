# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create Class
class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name}, {self.age} and I can be contacted at {self.email}'

#Extend Class
class Customer(User):
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance += balance

    def greeting(self):
        return f'My name is {self.name}, {self.age} and I can be contacted at {self.email} with balance: {self.balance}'

#Init object
nijam = Customer('Nijamudeen', 'test@test.com', 23)
print(nijam.greeting())
