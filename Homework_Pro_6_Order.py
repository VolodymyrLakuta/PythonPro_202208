class Buyers:
    def __init__(self, surname, name):
       self.surname = surname
       self.name = name
       
    def  __str__(self):
        return f"\nBuyer: {self.surname} {self.name}"


class Goods:
    def __init__(self, name : str, price : float):
        self.name = name
        if not is_number_float(price) or float(price) <= 0:
            raise My_exceptions ("Invalid price characters")
        self.price = round(float(price), 2)
                           
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}\n"


class My_exceptions(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return f"{self.message}"


class Orders:
    def __init__(self, buyer: Buyers):
        self.order = []
        self.quantities = []
        self.buyer = buyer
          
    def add_item (self, item: Goods, quantity: int):
        self.order.append(item)
        self.quantities.append(quantity)

    def total(self):
        res = 0
        for i, item in enumerate(self.order):
            res += item.price * self.quantities[i]
        return res 

    def __str__(self):
        order_str = f"Your order: \n{self.buyer}\n"
        for i, item in enumerate(self.order):
            order_str += f"\nItem {i+1}: {item}, Q-ty: {self.quantities[i]}\n"
        order_str += f"\nTotal: {len(self.order)} Item (-s) on ${self.total()}"
        return order_str

def is_number_float (val):
    try:
        float(val)
        return True 
    except ValueError: 
        return False

name = input("Enter the goods name: ")
price = input ("Enter the goods price($ or $.cents): ")
good_1 = Goods(name, price)

print(good_1)
