
class Goods:

    taxfee = 20

    def __init__(self, name : int, price : int):
        self.name = name
        self.price = price
    
    def __getattribute__(self, atr_name):
        try:
            return object.__getattribute__(self, atr_name)
        except AttributeError:
            return

    def __setattr__ (self, atr_name, atr_value):
        if not isinstance(atr_value, int):
            raise TypeError
        else:
            self.__dict__[atr_name] = atr_value

                  
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}"

    

''' Revise '''

t = Goods(200, 1)
print(t)

Goods.taxfee = 10
print(t.taxfee)

t.taxfee = 8.8
print(t.taxfee)
print(Goods.taxfee)
