 # Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # private attribute (encapsulation)

    def get_price(self):
        """Getter for price (encapsulation)"""
        return self.__price

    def set_price(self, new_price):
        """Setter for price (only if valid)"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("❌ Invalid price!")

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.__price}")


# Subclass (Inheritance + Polymorphism)
class iPhone(Smartphone):
    def __init__(self, model, price, face_id):
        super().__init__("Apple", model, price)  # Always Apple
        self.face_id = face_id

    def unlock(self):
        print(f"Unlocking {self.model} with Face ID 😎")

    # Polymorphism: override call()
    def call(self, number):
        print(f"📱 iPhone {self.model} is FaceTiming {number}...")


# Create objects
s1 = Smartphone("Samsung", "Galaxy S23", 800)
s2 = iPhone("14 Pro", 1200, True)

# Test methods
s1.info()
s1.call("0712345678")

s2.info()
s2.unlock()
s2.call("0787654321")   # Polymorphism in action

# Encapsulation test
print("Original Price:", s2.get_price())
s2.set_price(1500)      # Update price safely
print("Updated Price:", s2.get_price())




#Polymorphism challenge
class Animal:
    def move(self):
        print("This animal moves...")

class Dog(Animal):
    def move(self):
        print("Dog runs on 4 legs!")

class Bird(Animal):
    def move(self):
        print("Bird flies in the sky!")

class Fish(Animal):
    def move(self):
        print("Fish swims in water!")


# Test polymorphism
animals = [Dog(), Bird(), Fish()]

for a in animals:
    a.move()
# OOP Concepts: Inheritance, Encapsulation, Polymorphism
