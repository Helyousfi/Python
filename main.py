from ast import Pass
from asyncore import read
import csv
import argparse
from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
from traceback import print_tb
from unicodedata import name

required_parser = 1
if required_parser:
    # Create a parser for item 
    parser_item = argparse.ArgumentParser(description="Instantiate from command line")
    parser_item.add_argument('--name', '--n', type = str, required = True, help = "name of the object")
    parser_item.add_argument('--price', '--p', type = float, required = True, help = "Price of the object")
    parser_item.add_argument('--quantity', '--q', type = int, required = True, help = "quantity of the Items")
    args_item = parser_item.parse_args()
    # Create a parser for phone
    parser_phone = argparse.ArgumentParser(description="Instantiate from command line")
    parser_phone.add_argument('--name', '--n', type = str, required = True, help = "name of the object")
    parser_phone.add_argument('--price', '--p', type = float, required = True, help = "Price of the object")
    parser_phone.add_argument('--quantity', '--q', type = int, required = True, help = "quantity of the Items")
    parser_phone.add_argument('--is_broken', '--ib', type = int, required = True, help = "how many phones are broken")
    args_phone = parser_phone.parse_args()
    # Create a parser for laptop
    parser_laptop = argparse.ArgumentParser(description="Instantiate from command line")
    parser_laptop.add_argument('--name', '--n', type = str, required = True, help = "name of the object")
    parser_laptop.add_argument('--price', '--p', type = float, required = True, help = "Price of the object")
    parser_laptop.add_argument('--quantity', '--q', type = int, required = True, help = "quantity of the Items")
    parser_laptop.add_argument('--operating_sys', '--os', type = int, required = True, help = "Operating system")
    parser_laptop.add_argument('--size', '--s', type = int, required = True, help = "Size of the laptop")
    args_laptop = parser_laptop.parse_args()
    
class Item:
    # class attribute
    pay_rate = 0.8 # 
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # validations 
        assert price >= 0, f"The price : {price} is lesser than zero!"
        assert quantity >= 0, f"The quantity : {quantity} is lesser than zero!"
        # assigning instance attributes
        #print(f"An Item instance created for : {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__disc = 0.2
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate # self = Item
    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get(' price')),
                quantity=int(item.get(' quantity')),
            )
        #following lines for while loop
        if 0:
            idx = 0
            while idx < len(items): 
                Item(
                    name=items[idx].get('name'),
                    price=float(items[idx].get(' price')),
                    quantity=int(items[idx].get(' quantity')),
                )
                idx+=1
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}','{self.quantity}')"

class Phone(Item):
    all_phones = []
    def __init__(self, name: str, price: float, quantity: int, is_broken: int):
        super().__init__(name, price, quantity)
        self.is_broken = is_broken
        # validations 
        assert quantity>0, f"The quantity {quantity} is lesser than zero!" 
        print(f"A Phone instance created for {name}")
        Phone.all_phones.append(self)
    @classmethod
    def instantiate_from_csv(cls, file):
        print("ok")
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Phone(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
                is_broken=int(item.get('is_broken')),
            )
    def __repr__(self):
        return f"Phone('{self.name}', '{self.price}','{self.quantity}')"

class laptop(Item):
    all_laptops = []
    def __init__(self, name: str, price: float, quantity: int, operating_system: str, size: str):
        super().__init_(name, price, quantity)
        self.operating_system = operating_system
        self.size = size
        assert quantity >= 0, f"The quantity {quantity} is lesser than zero"
        print(f"An instance ")
    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                laptop(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity = int(item.get('quantity')),
                    operating_system = item.get('operating_system'),
                    size = item.get('size')
                )
    def __repr__(self):
        return f"laptop('{self.name}', '{self.price}','{self.quantity}')"


file = "phones.csv"
Phone.instantiate_from_csv(file)
print(Phone.all_phones)
phone1 = Phone.all_phones[0]


if required_parser:
    item1 = Item(args.name, args.price, args.quantity)
    print(item1.name)


"""
file = "items.csv"
Phone.instantiate_from_csv(file)
#print(Phone.all_phones)

phone1 = Phone("Huawei", 10, 1, 1)
print(phone1.name)
print(phone1.all)


file = "items.csv"
Item.instantiate_from_csv()
print(Item.all)
"""


"""
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 500, 10)
item3 = Item("Cable", 6, 20)
item4 = Item("Charger", 8, 60)
item5 = Item("USB", 4, 70)

print(Item.all)
"""
#item1.apply_discount()
#print(item1.price)

#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)

#print(item1.calculate_total_price())
#print(Item.pay_rate)
#print(item1.pay_rate) #First it checks the instance level then the class level
#print(item1.__dict__) # display all instances