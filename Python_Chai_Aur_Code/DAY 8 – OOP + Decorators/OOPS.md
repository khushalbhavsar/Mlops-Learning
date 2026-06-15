# Object-Oriented Programming (OOP) in Python 🐍

**Object-Oriented Programming (OOP)** is a way of writing programs using **objects** and **classes**. It helps you organize code, reuse it, and model real-world entities.

---

## 🔹 1. Class & Object

### Class

A **class** is a blueprint/template.

### Object

An **object** is an instance of a class.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Khushal", 22)
s1.display()
```

---

## 🔹 2. `__init__` Constructor

* Automatically called when an object is created
* Used to initialize data members

```python
def __init__(self, name):
    self.name = name
```

---

## 🔹 3. Instance Variables & Methods

### Instance Variable

Belongs to a specific object

```python
self.name
```

### Instance Method

Uses object data

```python
def show(self):
    print(self.name)
```

---

## 🔹 4. Four Pillars of OOP

---

## ✅ 1. Encapsulation (Data Hiding)

Wrapping data & methods together and restricting access.

### Example

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance
```

* `__balance` cannot be accessed directly
* Access via methods (getters/setters)

---

## ✅ 2. Inheritance (Code Reusability)

One class acquires properties of another.

### Example

```python
class Person:
    def speak(self):
        print("Speaking")

class Student(Person):
    def study(self):
        print("Studying")

s = Student()
s.speak()
s.study()
```

Types:

* Single
* Multiple
* Multilevel
* Hierarchical
* Hybrid

---

## ✅ 3. Polymorphism (Many Forms)

Same method name, different behavior.

### Example

```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()
```

---

## ✅ 4. Abstraction (Hiding Implementation)

Showing only essential features.

### Example (Abstract Class)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of Square")

s = Square()
s.area()
```

---

## 🔹 5. Class Variables vs Instance Variables

```python
class Company:
    company_name = "Google"   # class variable

    def __init__(self, emp):
        self.emp = emp        # instance variable
```

---

## 🔹 6. Method Types

### Instance Method

```python
def show(self):
    pass
```

### Class Method

```python
@classmethod
def info(cls):
    pass
```

### Static Method

```python
@staticmethod
def help():
    pass
```

---

## 🔹 7. `self` Keyword

* Refers to the **current object**
* Required to access variables & methods inside a class

---

## 🔹 8. Why Use OOP?

✔ Clean & organized code
✔ Reusability
✔ Easy maintenance
✔ Real-world modeling
✔ Better scalability

---

## 🔹 Simple Real-World Example

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand, "is driving")

c1 = Car("BMW")
c1.drive()
```

---

## 📝 Practice Questions

Learn about Object Oriented Programming by answering these questions:

1. **Basic Class and Object**  
   Create a `Car` class with attributes like `brand` and `model`. Then create an instance of this class.

2. **Class Method and Self**  
   Add a method to the `Car` class that displays the full name of the car (brand and model).

3. **Inheritance**  
   Create an `ElectricCar` class that inherits from the `Car` class and has an additional attribute `battery_size`.

4. **Encapsulation**  
   Modify the `Car` class to encapsulate the `brand` attribute, making it private, and provide a getter method for it.

5. **Polymorphism**  
   Demonstrate polymorphism by defining a method `fuel_type` in both `Car` and `ElectricCar` classes, but with different behaviors.

6. **Class Variables**  
   Add a class variable to `Car` that keeps track of the number of cars created.

7. **Static Method**  
   Add a static method to the `Car` class that returns a general description of a car.

8. **Property Decorators**  
   Use a property decorator in the `Car` class to make the `model` attribute read-only.

9. **Class Inheritance and `isinstance()` Function**  
   Demonstrate the use of `isinstance()` to check if `my_tesla` is an instance of `Car` and `ElectricCar`.

10. **Multiple Inheritance**  
    Create two classes `Battery` and `Engine`, and let the `ElectricCar` class inherit from both, demonstrating multiple inheritance.


---

## 📚 Solutions & Explanations

Below is a **step-by-step learning guide to Object-Oriented Programming (OOP) in Python**, where **each concept is explained by directly answering the given questions**.  
You can read it **in order** and see how OOP builds naturally.

---

### 🔹 1. Basic Class and Object

#### Problem

Create a `Car` class with attributes `brand` and `model`, then create an instance.

#### Explanation

* A **class** is a blueprint
* An **object** is a real instance of that class

#### Code

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Fortuner")
print(my_car.brand, my_car.model)
```

---

### 🔹 2. Class Method and `self`

#### Problem

Add a method to display full name of the car.

#### Explanation

* `self` refers to the **current object**
* Instance methods must use `self`

#### Code

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Honda", "City")
print(my_car.full_name())
```

---

### 🔹 3. Inheritance

#### Problem

Create `ElectricCar` that inherits from `Car` and adds `battery_size`.

#### Explanation

* **Inheritance** allows child class to reuse parent class code

#### Code

```python
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")
print(my_tesla.full_name(), my_tesla.battery_size)
```

---

### 🔹 4. Encapsulation (Private Variable)

#### Problem

Make `brand` private and provide a getter.

#### Explanation

* `__variable` makes it **private**
* Access via methods only

#### Code

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand   # private
        self.model = model

    def get_brand(self):
        return self.__brand
```

---

### 🔹 5. Polymorphism

#### Problem

Define `fuel_type()` in both classes with different behavior.

#### Explanation

* Same method name, different implementation

#### Code

```python
class Car:
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"

c = Car()
e = ElectricCar("Tesla", "Model 3", "75 kWh")

print(c.fuel_type())
print(e.fuel_type())
```

---

### 🔹 6. Class Variables

#### Problem

Track number of cars created.

#### Explanation

* Class variable is **shared across all objects**

#### Code

```python
class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

c1 = Car("BMW", "X5")
c2 = Car("Audi", "Q7")

print(Car.total_cars)
```

---

### 🔹 7. Static Method

#### Problem

Add static method returning general car description.

#### Explanation

* Does **not use `self` or `cls`**
* Belongs to class logically

#### Code

```python
class Car:
    @staticmethod
    def description():
        return "A car is a four-wheeled vehicle used for transportation."

print(Car.description())
```

---

### 🔹 8. Property Decorators (Read-Only Attribute)

#### Problem

Make `model` read-only.

#### Explanation

* `@property` allows controlled access
* No setter → read-only

#### Code

```python
class Car:
    def __init__(self, brand, model):
        self._model = model
        self.brand = brand

    @property
    def model(self):
        return self._model

car = Car("Hyundai", "Creta")
print(car.model)

# car.model = "Verna" ❌ Error (read-only)
```

---

### 🔹 9. `isinstance()` Function

#### Problem

Check if `my_tesla` is instance of `Car` and `ElectricCar`.

#### Explanation

* Checks object's class relationship

#### Code

```python
my_tesla = ElectricCar("Tesla", "Model X", "90 kWh")

print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Car))          # True
```

---

### 🔹 10. Multiple Inheritance

#### Problem

Create `Battery` and `Engine`, inherit both in `ElectricCar`.

#### Explanation

* A class can inherit from **multiple parent classes**

#### Code

```python
class Battery:
    def battery_info(self):
        return "Lithium-ion battery"

class Engine:
    def engine_info(self):
        return "Electric motor"

class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model Y", "75 kWh")

print(my_tesla.battery_info())
print(my_tesla.engine_info())
```

---
