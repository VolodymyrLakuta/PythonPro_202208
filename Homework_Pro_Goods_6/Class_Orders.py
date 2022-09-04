import Class_Goods

import Class_Buyers

import Class_My_exceptions

class Orders:
    def __init__(self, buyer: Class_Buyers.Buyers):
        self.order = []
        self.quantities = []
        self.buyer = buyer
          
    def add_item (self, item: Class_Goods.Goods, quantity: int):
        if not isinstance(quantity, int) or quantity <= 0:
            raise Class_My_exceptions.My_exceptions("Invalid quantity")
        else:
            self.order.append([item, quantity])
            
    
    def total(self):
        res = 0
        for item in self.order:
            res += item[0].price * item[1]
        return res 
    
    def __str__(self):
        order_str = f"Your order: \n{self.buyer}\n"
        for i, item in enumerate(self.order):
            order_str += f"\nItem {i+1}: {item[0]}, Q-ty: {item[1]}\n"
        order_str += f"\nTotal: {len(self.order)} Item (-s) on ${self.total()}"
        return order_str
    
    def __iter__(self):
       return OrderIter(self.order)

    def __getitem__(self, index : int | slice):
        if isinstance(index, slice):
            if index.stop and index.stop > len(self.order):
                raise IndexError
            return self.order[index]
        if isinstance(index, int) and index < len(self.order):
            return self.order[index]
        else:
            raise IndexError
   
    def __len__(self):
        return len(self.order)


class OrderIter:
    def __init__(self, order : Orders):
        self.order = order
        self.index = 0

    def __next__(self):
        if self.index < len(self.order):
            self.index += 1
            return self.order[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

    
        
         
      
 
