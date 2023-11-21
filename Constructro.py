class Item:
    pay_rate = 0.8 # The pay rate after 20% count
    all=[]
    def __init__(self, name:str,price:float,quantity:int) -> None:
        # Run validation to the received arguments
        assert price >=0, f'Price{price} is not equal or greater than zero!'
        assert quantity>=0, f'quantity{quantity} is not equal or greater than zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
        
    
    def calculate_total_price(self):
        return self.name*self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"
    

item1 = Item('Phone',100,5)
item2 = Item('Laptop',1000,5)
item3 = Item('Cable',100,5)
item4 = Item('Mouse',1000,5)
item5 = Item('Keyboard',100,5)
item6 = Item('Monitor',1000,5)

print(Item.all)

