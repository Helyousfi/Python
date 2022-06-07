"""
The super() function has two major use cases:
    To avoid the usage of the super (parent) class explicitly.
    To enable multiple inheritances​.
"""

##### avoid the usage of the parent class explicitly ##### 
class Computer():
    def __init__(self, computer, ram, storage):
        self.computer = computer
        self.ram = ram
        self.storage = storage

# Class Mobile inherits Computer
class Mobile(Computer):
    def __init__(self, computer, ram, storage, model):
        super().__init__(computer, ram, storage)
        self.model = model

Apple = Mobile('Apple', 2, 64, 'iPhone X')
print('The mobile is:', Apple.computer)
print('The RAM is:', Apple.ram)
print('The storage is:', Apple.storage)
print('The model is:', Apple.model)



##### multiple inheritance ##### 
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

# Mammal inherits Animal
class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a mammal.')
    super().__init__(mammalName)
    
# CannotFly inherits Mammal
class CannotFly(Mammal):
  def __init__(self, mammalThatCantFly):
    print(mammalThatCantFly, "cannot fly.")
    super().__init__(mammalThatCantFly)

# CannotSwim inherits Mammal
class CannotSwim(Mammal):
  def __init__(self, mammalThatCantSwim):
    print(mammalThatCantSwim, "cannot swim.")
    super().__init__(mammalThatCantSwim)

# Cat inherits CannotSwim and CannotFly
class Cat(CannotSwim, CannotFly):
  def __init__(self):
    print('I am a cat.');
    super().__init__('Cat')

# Driver code
cat = Cat()
print('')
bat = CannotSwim('Bat')