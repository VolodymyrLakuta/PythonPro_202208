class MyDescriptor:
    def __init__(self, value):
        self.value = value
    
    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        raise AttributeError("Field is read-only")

    def __delete__(self, instance_self):
        raise AttributeError("Cannot delete field")



class Goods:

    taxfee = MyDescriptor(20)

    def __init__(self, name : str, price : int | float):
        self.name = name
        if not isinstance(price, (int, float)) or price <= 0:
            raise TypeError ("Invalid price characters")
        else:
            self.price = round(price, 2)
                       
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}"

    

''' Revise '''

t = Goods("banana", 45)
print(t)
print(t.taxfee)
del t.taxfee