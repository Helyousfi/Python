# Dunder __ : Magic methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("The object is being deconstructed")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X : {self.x}, Y:{self.y}"

p1 = Vector(5,4)
p2 = Vector(4,6)
p3 = p1 + p2
print(p3)
