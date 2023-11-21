import csv

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
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            # print(item)
            Item(
                name = item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_int(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num,float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
    
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int,broken_phones=0) -> None:
        super().__init__(name, price, quantity) 

        # Run validations to the received arguments
        assert broken_phones >=0, f"Broken phones {broken_phones} is not greater or equal than zero!"
        
        # Assign to self object
        self.broken_phone = broken_phones



phone1 = Phone("jscPhonev10", 500,5,1)
print(phone1.calculate_total_price())

phone2 = Phone("jscPhonev20",700,5)

print(Item.all)
print(Phone.all)

