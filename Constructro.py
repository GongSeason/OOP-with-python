class Item:
    pay_rate = 0.8 # The pay rate after 20% count
    def __init__(self, name:str,price:float,quantity:int) -> None:
        # Run validation to the received arguments
        assert price >=0, f'Price{price} is not equal or greater than zero!'
        assert quantity>=0, f'quantity{quantity} is not equal or greater than zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def calculate_total_price(self):
        return self.name*self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    

item1 = Item('Phone',100,5)

item2 = Item('Laptop',1000,5)
item2.pay_rate = 0.7
print(item2.apply_discount())

print(Item.__dict__)  # All the attributes for Class level
print(item1.__dict__) # all the attributes for instance level

