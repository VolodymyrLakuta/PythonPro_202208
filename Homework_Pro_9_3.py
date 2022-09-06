# Task 3

def file_dekor(func):
    file_name = "Group.txt"
    def wrapper(*args):
        with open(file_name, "a") as file_obj:
            file_obj.write(func(*args))
        return file_obj
    return wrapper

class Group:
    def __init__(self, title):
        self.title = title
        self.group_list = []
                  
    @file_dekor
    def __str__ (self):
        return f'{self.title}\n' + '\n'.join(map(str, self.group_list))

def file_dekor(func):
    file_name = f"Group.txt"
    def wrapper(*args):
        with open(file_name, "a") as file_obj:
            file_obj.write(func(*args))
        return file_obj
    return wrapper       


''' Revice '''

t = Group("Start")
t.group_list = ["Ivanov", "Petrov", "other"]
t.__str__()











