import Class_Goods
    
import Class_Buyers
    
import Class_Orders


goods_1 = Class_Goods.Goods("Dumbbells Set 10 kg", 50.0)
goods_2 = Class_Goods.Goods("Dumbbells Set 15 kg", 70.0)
goods_3 = Class_Goods.Goods("Dumbbells Set 5 kg", 25.0)

buyer_1 = Class_Buyers.Buyers("Ivanov", "Petro", "+380991234567")

order_1 = Class_Orders.Orders(buyer_1)

order_1.add_item(goods_1, 1) 
order_1.add_item(goods_2, 2)
order_1.add_item(goods_3, 3)  

print (order_1)

buyer_2 = Class_Buyers.Buyers("Petrov", "Ivan", "+380997654321")

order_2 = Class_Orders.Orders(buyer_2)

order_2.add_item(goods_1, 4)

print()
print (order_2, "\n")

for i in order_1:           # Перевірка ітераційного протоколу
    print(f"{i[0]}, q-ty: {i[1]}")

print(order_1[:3])

print(len(order_2))

