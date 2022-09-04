class Buyers:
    def __init__(self, surname, name, phonenumber):
       self.surname = surname
       self.name = name
       
    def  __str__(self):
        return f"\nBuyer: {self.surname} {self.name}"