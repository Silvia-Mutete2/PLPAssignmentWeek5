# PLPAssignmentWeek5
# 🐍 Python OOP Assignment  

## 📌 Overview  
This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python through two activities:  

### 1. Design Your Own Class  
- A `Smartphone` base class with attributes, methods, encapsulation (private attributes), and inheritance.  
- A subclass `iPhone` that overrides methods to show **polymorphism**.  

### 2. Polymorphism Challenge  
- An example with animals where the same method `move()` behaves differently for `Dog`, `Bird`, and `Fish`.  

---

## 🏗️ Activity 1: Design Your Own Class  

**Class Created:** `Smartphone`  
- **Attributes:** brand, model, price (encapsulated with private variable `__price`)  
- **Methods:** `call()`, `info()`, `get_price()`, `set_price()`  
- **Inheritance:** `iPhone` subclass inherits from `Smartphone`  
- **Polymorphism:** `iPhone` overrides the `call()` method  
- **Encapsulation:** Price is private and modified only using getter and setter  

### ✅ Example Usage  
```python
s1 = Smartphone("Samsung", "Galaxy S23", 800)
s2 = iPhone("14 Pro", 1200, True)

s1.call("0712345670")   # Uses Smartphone call
s2.call("0787654321")   # Uses iPhone FaceTime call
