# Task 1

def geometric_progression(start, stop, q):
    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(q, int):
        raise TypeError("Data must be int")
    if not start or not stop or not q or q == 1:
        raise ValueError
    n = start
    while n <= stop:
        index = yield n
        if index == "123":
            return "Finish"
        n = n*q
    
'''
x = geometric_progression(11, 1000, 2)    # Revise
print(next(x))
while True:
    n = input("n = ")
    print(x.send(n))
'''


# Task 2

def range_funct(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError("Invalid arguments")
    if (start >= stop and step < 0) or not step:
        raise ValueError 
    while start < stop:
        yield start
        start += step


print(f"{[x for x in range_funct(11, 50)]}\n")     # Revise


# Task 3

def prime_numbers(n):
    if not isinstance(n, int):
        raise TypeError("Data must be int")
    if n <= 0:
        raise ValueError("Must be greater than zero")
    for i in range(1, n + 1):
        for j in range (2, i):
            if not i%j:
                break
        else: yield i

print(f"{[x for x in prime_numbers(25)]}\n")     # Revise


# Task 4

n = 11
x = (x**3 for x in range(1, n))
print(x)
print(list(x))