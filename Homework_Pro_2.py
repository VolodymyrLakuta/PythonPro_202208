class Human:
    def __init__(self, surname : str, name : str, year_birth : str):
        self.surname = surname
        self.name = name
        self.year_birth = year_birth
      
    def  __str__(self):
        return f"{self.surname} {self.name}, {self.year_birth}\n"

class Students(Human):
    
    def __init__(self, surname : str, name : str, year_birth : str, phone_num : str):
       super().__init__(surname, name, year_birth)
       self.phone_num = phone_num
              
    def  __str__(self):
        return f"{super().__str__().rstrip()}, phone {self.phone_num}"

class Group:
    def __init__(self, title):
        self.title = title
        self.group_list = []

    def add_new_student (self, student : Students, MAX_GR = 10):
        if len(self.group_list) == MAX_GR:
            raise My_exceptions("The group is already dialed")
        for item in self.group_list:
            if item.surname.lower() == student.surname.lower() and \
                item.name.lower() == student.name.lower() and \
                item.year_birth == student.year_birth:
                raise My_exceptions("This student is already in the group")
        
        self.group_list.append(student)
        
    def search_student (self, student_name):         # Пошук студентів за призвіщем
        for item in self.group_list:
            if item.surname.lower() == student_name.lower():
                return item
        raise My_exceptions("Not found")

    def del_student (self, student_name):              # Видалення студента (пошук за призвіщем)
        for item in self.group_list:
            if item.surname.lower() == student_name.lower():
                self.group_list.remove(item)
                return
        raise My_exceptions("Not found")
     
    def __str__ (self):
        return f'{self.title}\n' + '\n'.join(map(str, self.group_list))

class My_exceptions (Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return f"{self.message}"            
        
def create_students_list(filename):                 # Використовується текстовий файл (є дубльовані студенти)
    list_students = []
    with open (filename, "r") as list_file:
        lines = list_file.readlines()
        del (lines[-1])                    # Видалення знаку переносу рядка
        for item in lines:
            item = item.rstrip()            # Видалення знаку переносу рядка
            surname, name, year_birth, phone_num = item.split()
            student = Students(surname, name, year_birth, phone_num)
            list_students.append(student)
    return list_students

list_student = create_students_list("students")                       # Створення списку студентів (Class Students)
for item in list_student:
    print(item)

print()

title = "Python Pro"                                   # Створення групи (Class Group) із списку студентів
group_1 = Group(title)
for item in list_student[0:9]:
    group_1.add_new_student(item)
print(group_1)

print()

st_1 = Students("Lakuta", "Volodymyr", "1999", "0349876543")
group_1.add_new_student(st_1)
print(group_1)

print()

print (group_1.search_student("mazur"), "\n")

group_1.del_student("mazur")

print(group_1)