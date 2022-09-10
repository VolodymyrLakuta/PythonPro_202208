
class Goods:

    def __init__(self, name : str, price : int | float):
        self.name = name
        if not isinstance(price, (int, float)) or price <= 0:
            raise TypeError ("Invalid price characters")
        else:
            self.price = round(price, 2)

    def getTaxfee(self):
        return 20

    def setTaxfee(self, value):
        raise AttributeError("Field is read-only")

    def delTaxfee(self):
        raise AttributeError("Cannot delete field")
    
    taxfee = property(getTaxfee, setTaxfee, delTaxfee)
                       
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}"

    

''' Revise '''

t = Goods("banana", 45)
print(t)
print(t.taxfee)
print(t.__dict__)
print(Goods.__dict__)
Goods.taxfee = 30
