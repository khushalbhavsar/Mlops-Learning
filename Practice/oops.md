# Python OOP Concepts (Interview Cheat Sheet)

These are the **6 most important OOP concepts** asked in Python, Java, C++, DevOps, Automation, and SRE interviews.

---

## 1. Class 

### Short Definition

A **Class** is a blueprint or template used to create objects.

### Syntax

```python
class Student:

    def display(self):
        print("Hello Student")
```

### Create Object

```python
s = Student()

s.display()
```

### Output

```text
Hello Student
```

### Real-Life Example

```text
Class = Car Design

Object = BMW, Audi, Tesla
```

---

## 2. Object 

### Short Definition

An **Object** is an instance of a class.

### Syntax

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

student1 = Student("Khushal")

student1.display()
```

### Output

```text
Khushal
```

### Real-Life Example

```text
Class = Student

Objects

Khushal

Rahul

Amit
```

---

## 3. Inheritance 

### Short Definition

**Inheritance** allows one class (child) to inherit properties and methods from another class (parent).

### Syntax

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def bark(self):
        print("Dog Bark")

d = Dog()

d.sound()

d.bark()
```

### Output

```text
Animal Sound

Dog Bark
```

### Real-Life Example

```text
Animal

↓

Dog

↓

Labrador
```

### Benefits

* Code Reusability
* Less Code
* Easy Maintenance

---

## 4. Polymorphism 

### Short Definition

**Polymorphism** means **one method, many forms**.

The same method behaves differently in different classes.

### Syntax

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

### Output

```text
Bark

Meow
```

### Real-Life Example

```text
Vehicle.start()

↓

Car.start()

Bike.start()

Bus.start()
```

---

## 5. Encapsulation 

### Short Definition

**Encapsulation** means **hiding data** and allowing controlled access through methods.

### Syntax

```python
class Bank:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

b = Bank()

print(b.get_balance())
```

### Output

```text
1000
```

### Cannot Access Directly

```python
print(b.__balance)
```

### Output

```text
AttributeError
```

### Real-Life Example

```text
ATM Machine

↓

Cannot directly access bank data

↓

Must enter PIN
```

---

## 6. Abstraction 

### Short Definition

**Abstraction** means **showing only essential functionality while hiding implementation details**.

### Syntax

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

c = Car()

c.start()
```

### Output

```text
Car Started
```

### Real-Life Example

```text
Car

↓

Press Start Button

↓

Engine starts

(User doesn't know internal engine mechanism.)
```

---

## OOP Hierarchy

```text
Class
   │
   ▼
Object
   │
   ▼
Inheritance
   │
   ▼
Polymorphism
   │
   ▼
Encapsulation
   │
   ▼
Abstraction
```

---

## Complete Example

```python
from abc import ABC, abstractmethod

# Parent Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child Class
class Dog(Animal):

    def __init__(self, name):
        self.__name = name      # Encapsulation

    def sound(self):            # Polymorphism
        print(self.__name, "says Bark")

dog = Dog("Tom")

dog.sound()
```

### Output

```text
Tom says Bark
```

---

## OOP Summary Table

| Concept           | Short Definition                            | Example                      |
| ----------------- | ------------------------------------------- | ---------------------------- |
| **Class**         | Blueprint for creating objects              | `class Student:`             |
| **Object**        | Instance of a class                         | `s = Student()`              |
| **Inheritance**   | Child class inherits from parent            | `class Dog(Animal)`          |
| **Polymorphism**  | Same method, different behavior             | `sound()` in `Dog` and `Cat` |
| **Encapsulation** | Hide data using private variables           | `self.__balance`             |
| **Abstraction**   | Hide implementation, expose only essentials | `@abstractmethod`            |

---

## Most Asked Interview Questions

### 1. What is a Class?

> A class is a blueprint used to create objects. It defines attributes and methods.

### 2. What is an Object?

> An object is an instance of a class that can access the class's attributes and methods.

### 3. What is Inheritance?

> Inheritance allows a child class to reuse the properties and methods of a parent class, promoting code reuse.

### 4. What is Polymorphism?

> Polymorphism allows the same method name to perform different actions depending on the object that calls it.

### 5. What is Encapsulation?

> Encapsulation hides internal data using private members and provides controlled access through methods.

### 6. What is Abstraction?

> Abstraction hides implementation details and exposes only the necessary functionality to the user.
