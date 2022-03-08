class Item:
    # class attribute
    pay_rate = 0.8 # 
    def __init__(self, name: str, price: float, quantity=0):
        # validations 
        assert price >= 0, f"The price : {price} is lesser than zero!"
        assert quantity >= 0, f"The quantity : {quantity} is lesser than zero!"
        # assigning instance attributes
        print(f"An instance created for : {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 500, 10)

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

#print(item1.calculate_total_price())
#print(Item.pay_rate)
#print(item1.pay_rate) #First it checks the instance level then the class level
#print(item1.__dict__) # display all instances