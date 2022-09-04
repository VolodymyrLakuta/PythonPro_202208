class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def  __str__(self):
        return f"\n{self.name} Price: ${self.price}"

class Buyers:
    def __init__(self, surname, name, phonenumber):
       self.surname = surname
       self.name = name
       
    def  __str__(self):
        return f"\nBuyer: {self.surname} {self.name}"

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
   
goods_1 = Goods("Dumbbells Set 10 kg", 50.0)
goods_2 = Goods("Dumbbells Set 15 kg", 70.0)
goods_3 = Goods("Dumbbells Set 5 kg", 30.0)

buyer_1 = Buyers("Ivanov", "Petro", "+380991234567")

order_1 = Orders(buyer_1)

order_1.add_item(goods_1, 1) 
order_1.add_item(goods_2, 2)
order_1.add_item(goods_3, 3)  

print (order_1)

buyer_2 = Buyers("Petrov", "Ivan", "+380997654321")

order_2 = Orders(buyer_2)

order_2.add_item(goods_1, 4)

print()
print (order_2)

