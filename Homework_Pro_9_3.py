# Task 3

def file_dekor(func):
    def wrapper(*args, **kwargs):
        file_name = f"{func.__qualname__.split('.')[0]}.txt"
        res = func(*args, *kwargs)
        with open(file_name, "a") as file_obj:
            file_obj.write(func(*args, *kwargs))
        return res
    return wrapper

class Group:
    def __init__(self, title):
        self.title = title
        self.group_list = []
                  
    @file_dekor
    def __str__ (self):
        return f'{self.title}\n' + '\n'.join(map(str, self.group_list))     


''' Revise '''

t = Group("Start")
t.group_list = ["Ivanov", "Petrov", "other"]
print(t)











