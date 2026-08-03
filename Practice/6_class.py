# What is class in Python?
# A class is a blueprint for creating objects. 
# It defines a set of attributes and methods that the created objects will have. Classes allow for encapsulation, inheritance, and polymorphism, which are key concepts in object-oriented programming.

# Create a Student class.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age :", self.age)

s = Student("Khushal", 22)
s.display()

# class creates a blueprint.
# __init__() is the constructor and runs automatically when an object is created.
# self refers to the current object and is passed automatically by Python.
# self.name = name stores the value in the object's attribute.
# Student("Khushal") creates a new object and calls __init__().
# s.display() calls the display() method on that object, where self refers to s.
# Each object has its own copy of instance variables like self.name.

# Create an Employee class.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name  :", self.name)
        print("Salary:", self.salary)

e = Employee("Khushal", 50000)
e.display()

# Create a Car class.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print("Make :", self.make)
        print("Model:", self.model)

c = Car("Toyota", "Camry")
c.display()


# Create a BankAccount class.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance       :", self.balance)

b = BankAccount("123456789", 1000.50)
b.display()

# Create a Laptop class.
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

l = Laptop("Dell", 800)
l.display()
