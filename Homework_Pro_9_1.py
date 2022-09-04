# Task 1
counter = {}

def count_func_call(func):
    count = 0
    name_func = func.__name__
    def count_call(*args):
        nonlocal count
        nonlocal name_func
        func(*args)
        count += 1
        counter[name_func] = count
        return
    return count_call
    

@count_func_call
def hello(text):
    print(f"Hello {text}")

text = "world"

for i in range(1, 5):
    hello(text)

print (counter)









