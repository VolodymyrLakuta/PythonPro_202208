
# Task 1

def progression_func(start : int | float, n : int, func):
    if not isinstance(start, (int, float)) or not isinstance(n, int):
        raise TypeError("Invalid data type")
    if abs(start) < 2:
        raise ValueError("Invalid data")
    elem = start
    for i in range(1, n + 1):
        index = yield elem
        if index == "123":
            return "Finish"
        elem = func(elem)
    

f = lambda x: x**2                   # User function

x = progression_func(2, 5, f)        # Revise
print(next(x))
while True:
    ans = input("Input 123 for finish or turn Enter for continue: ")
    print(x.send(ans))



    





