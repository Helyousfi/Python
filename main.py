from ast import Pass
import csv
from unicodedata import name

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
    def __init__(self, name: str, price: float, quantity: int, is_broken: bool):
        super().__init__(name, price, quantity)
        self.is_broken = is_broken
        # validations 
        assert quantity>0, f"The quantity {quantity} is lesser than zero!" 
        print(f"A Phone instance created for {name}")
        self.all_phones.append(self)

    @classmethod
    def intantiate_from_csv(cls, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Phone(
                name=item.get('name'),
                price=float(item.get(' price')),
                quantity=int(item.get(' quantity')),
                is_broken=bool(item.get(' is_broken')),
            )

    def __repr__(self):
        return f"Phone('{self.name}', '{self.price}','{self.quantity}')"

class laptop(Item):
    def __init__(self, name: str, price: float, quantity: int, operating_system: str, size: str):
        super().__init_(name, price, quantity)
        self.operating_system = operating_system
        self.size = size
        assert quantity >= 0, f"The quantity {quantity} is lesser than zero"
        print(f"An instance ")
    
    @classmethod
    def instantiate_from_csv(cls, file):
        return super().instantiate_from_csv(file)



file = "items.csv"
Phone.instantiate_from_csv(file)
#print(Phone.all_phones)

"""
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