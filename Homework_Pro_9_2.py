# Task 2

list_func_sequence_name = []
list_func_sequence = []

def list_decor(func):
    name_func = func.__name__
    list_func_sequence_name.append(name_func)
    list_func_sequence.append(func)
    return

@list_decor
def sum_sequince(sequince, pov_func = lambda x: x**2):
    if not all(isinstance(x, (int, float)) for x in sequince):
        return TypeError
    res = 0
    for elem in sequince:
        res += pov_func(elem)
    return res

'''
Revice
'''
print(list_func_sequence_name)
print(list_func_sequence)

seq = [0, 1, 2, 3]
print(list_func_sequence[0](seq))







