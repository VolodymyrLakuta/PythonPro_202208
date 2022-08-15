class Goods:
    def __init__(self, name : str, price : float):
        self.name = name
        self.price = price
       
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}\n"

class Price_exceptions (Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message 

def is_number(s):
    try:
        float(s)
        return True 
    except ValueError: 
        return False

name = input("Enter the goods name: ")
price = input ("Enter the goods price: ")
try:
    if not is_number (price) or not float(price):
        raise Price_exceptions ("Invalid price characters")
except Price_exceptions as err:
    print(err.get_exception_message())
else:
    price = round(float(price), 2)
    good_1 = Goods (name, price)
    print (good_1)

