class Item:
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
    

item1 = Item('Phone',100,5)

print(item1.calculate_total_price())

item2 = Item('Laptop',1000,5)

print(item2.calculate_total_price())