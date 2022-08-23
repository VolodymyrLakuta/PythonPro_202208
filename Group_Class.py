'''
This module includes classes Group and GroupIter
'''

from Students_Class import Students

from My_exceptions_Class import My_exceptions

class Group:
    def __init__(self, title):
        self.title = title
        self.__group_list = []

    def add_new_student (self, student : Students, MAX_GR = 10):
        if len(self.__group_list) == MAX_GR:
            raise My_exceptions("The group is already dialed")
        for item in self.__group_list:
            if item.surname.lower() == student.surname.lower() and \
                item.name.lower() == student.name.lower() and \
                item.year_birth == student.year_birth:
                raise My_exceptions("This student is already in the group")
        
        self.__group_list.append(student)
        
    def search_student (self, student_name):         # Пошук студентів за призвіщем
        for item in self.__group_list:
            if item.surname.lower() == student_name.lower():
                return item
        raise My_exceptions("Not found")

    def del_student (self, student_name):              # Видалення студента (пошук за призвіщем)
        for item in self.__group_list:
            if item.surname.lower() == student_name.lower():
                self.__group_list.remove(item)
                return
        raise My_exceptions("Not found")
     
    def __str__ (self):
        return f'{self.title}\n' + '\n'.join(map(str, self.__group_list))

    def __iter__(self):
        return GroupIter(self.__group_list)


class GroupIter:
    def __init__(self, group_list):
        self.group_list = group_list
        self.index = 0

    def __next__(self):
        if self.index < len(self.group_list):
            self.index += 1
            return self.group_list[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


