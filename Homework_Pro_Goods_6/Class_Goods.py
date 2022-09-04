import Class_My_exceptions

class Goods:
    def __init__(self, name : str, price : int | float):
        self.name = name
        if not isinstance(price, (int, float)) or price <= 0:
            raise Class_My_exceptions.My_exceptions ("Invalid price characters")
        else:
            self.price = round(price, 2)
                       
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}"