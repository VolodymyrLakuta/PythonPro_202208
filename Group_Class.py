import Students_Class as St_cl

import My_exceptions_Class as My_exc

class Group:
    def __init__(self, title):
        self.title = title
        self.group_list = []

    def add_new_student (self, student : St_cl.Students, MAX_GR = 10):
        if len(self.group_list) == MAX_GR:
            raise My_exc.My_exceptions("The group is already dialed")
        for item in self.group_list:
            if item.surname.lower() == student.surname.lower() and \
                item.name.lower() == student.name.lower() and \
                item.year_birth == student.year_birth:
                raise My_exc.My_exceptions("This student is already in the group")
        
        self.group_list.append(student)
        
    def search_student (self, student_name):         # Пошук студентів за призвіщем
        for item in self.group_list:
            if item.surname.lower() == student_name.lower():
                return item
        raise My_exc.My_exceptions("Not found")

    def del_student (self, student_name):              # Видалення студента (пошук за призвіщем)
        for item in self.group_list:
            if item.surname.lower() == student_name.lower():
                self.group_list.remove(item)
                return
        raise My_exc.My_exceptions("Not found")
     
    def __str__ (self):
        return f'{self.title}\n' + '\n'.join(map(str, self.group_list))

