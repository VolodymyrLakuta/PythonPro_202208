from Students_Class import Students

from Group_Class import Group, GroupIter

from My_exceptions_Class import My_exceptions
        
        
def create_students_list(filename):                 # Використовується текстовий файл (є дубльовані студенти)
    list_students = []
    for line in open(filename):
        line = line.rstrip()
        if not line: break
        surname, name, year_birth, phone_num = line.split()
        student = Students(surname, name, year_birth, phone_num)
        list_students.append(student)
    return list_students

list_student = create_students_list("students")       # Створення списку студентів (Class Students) з файлу
for item in list_student:
    print(item)

print()

title = "Python Pro"                                   # Створення групи (Class Group) із списку студентів
group_1 = Group(title)
for item in list_student[0:8]:
    group_1.add_new_student(item)
print(group_1)

print()

st_1 = Students("Lakuta", "Volodymyr", "1999", "0349876543") # Додавання студента в групу
group_1.add_new_student(st_1)
print(group_1)

print()

print (group_1.search_student("mazur"), "\n")    # Пошук студента в групі

group_1.del_student("mazur")      # Видалення студента з групи

print(group_1)

for item in group_1:
    item.phone_num = "0"
print(group_1)