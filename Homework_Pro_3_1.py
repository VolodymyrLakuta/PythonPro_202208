class Goods:
    def __init__(self, name : str, price : float):
        self.name = name
        self.price = price

    def price_control (name, price):   
        if not is_number_float (price) or float(price) <= 0:
            err = My_exceptions ("Invalid price characters")
            return err.get_exception_message()
        price = round(float(price), 2)
        return Goods(name, price)
                     
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}\n"

class My_exceptions (Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return f"{self.message}"

def is_number_float (val):
    try:
        float(val)
        return True 
    except ValueError: 
        return False

name = input("Enter the goods name: ")
price = input ("Enter the goods price($ or $.cents): ")
good_1 = Goods.price_control (name, price)

print(good_1)
