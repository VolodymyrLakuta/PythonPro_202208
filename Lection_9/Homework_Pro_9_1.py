# Task 1
counter = {}

def count_func_call(f):
    count = 0
    name_f =f.__name__
    def count_call(*args):
        nonlocal count
        nonlocal name_f
        f(*args)
        count += 1
        counter[name_f] = count
        return
    return count_call
    

@count_func_call
def hello(text):
    print(f"Hello {text}")

text = "world"

for i in range(1, 5):
    hello(text)

print (counter)









