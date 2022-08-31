# Task 3

import random

def sum_sequince(sequince, pov_func):
    for elem in sequince:
        if not isinstance(elem, (int, float)):
            return TypeError
    res = 0
    for elem in sequince:
        res += pov_func(elem)
    return res

n = 10
numbers_list = [random.randint(1,100) for i in range (n)]

f = lambda x: x**2

print(numbers_list)

print(f"Sum = {sum_sequince(numbers_list, f)}")
    





