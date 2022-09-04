# Task 1

def count_func_call(f):
    count = 0
    def count_call():
        nonlocal count
        f()
        count += 1
        return count
    return count_call
    

@count_func_call
def hello():
    print("hello world")

for i in range(1, 5):
    print(hello())







