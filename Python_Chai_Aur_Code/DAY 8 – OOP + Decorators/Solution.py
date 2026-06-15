# ================================
# Complete OOP Example in Python
# ================================

# Battery class (for Multiple Inheritance)
class Battery:
    def battery_info(self):
        return "Lithium-ion Battery"


# Engine class (for Multiple Inheritance)
class Engine:
    def engine_info(self):
        return "Electric Motor Engine"


# Base Car class
class Car:
    # 6️⃣ Class Variable
    total_cars = 0

    def __init__(self, brand, model):
        # 4️⃣ Encapsulation (private variable)
        self.__brand = brand
        self._model = model   # protected for property
        Car.total_cars += 1

    # 2️⃣ Instance Method using self
    def full_name(self):
        return f"{self.__brand} {self._model}"

    # 4️⃣ Getter method
    def get_brand(self):
        return self.__brand

    # 5️⃣ Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"

    # 7️⃣ Static Method
    @staticmethod
    def description():
        return "A car is a four-wheeled vehicle used for transportation."

    # 8️⃣ Read-only property
    @property
    def model(self):
        return self._model


# 3️⃣ Inheritance + 🔟 Multiple Inheritance
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    # 5️⃣ Polymorphism (method override)
    def fuel_type(self):
        return "Electric"


# ================================
# Creating Objects
# ================================

car1 = Car("Toyota", "Innova")
car2 = Car("BMW", "X5")

my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")

# ================================
# Outputs
# ================================

print("---- Car Details ----")
print(car1.full_name())
print(car2.full_name())

print("\n---- Electric Car Details ----")
print(my_tesla.full_name())
print("Battery Size:", my_tesla.battery_size)

print("\n---- Encapsulation ----")
print("Brand (using getter):", my_tesla.get_brand())

print("\n---- Polymorphism ----")
print("Car Fuel Type:", car1.fuel_type())
print("Electric Car Fuel Type:", my_tesla.fuel_type())

print("\n---- Class Variable ----")
print("Total Cars Created:", Car.total_cars)

print("\n---- Static Method ----")
print(Car.description())

print("\n---- Property Decorator (Read-only) ----")
print("Model:", my_tesla.model)
# my_tesla.model = "Model X"  # ❌ Not allowed

print("\n---- isinstance() Check ----")
print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Car))          # True

print("\n---- Multiple Inheritance ----")
print(my_tesla.battery_info())
print(my_tesla.engine_info())
