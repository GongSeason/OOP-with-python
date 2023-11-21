class Item:
    def __init__(self, name,price,quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"An instance created:{name}")
    
    def calculate_total_price(self):
        return self.name*self.quantity
    

item1 = Item('Phone',100,5)

print(item1.calculate_total_price())

item2 = Item('Laptop',1000,5)

print(item2.calculate_total_price())