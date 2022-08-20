import Students_Class as St_cl

import Group_Class as Gr_cl

import My_exceptions_Class as My_exc
        
        
def create_students_list(filename):                 # Використовується текстовий файл (є дубльовані студенти)
    list_students = []
    with open (filename, "r") as list_file:
        lines = list_file.readlines()
        del (lines[-1])                    # Видалення знаку переносу рядка
        for item in lines:
            item = item.rstrip()            # Видалення знаку переносу рядка
            surname, name, year_birth, phone_num = item.split()
            student = St_cl.Students(surname, name, year_birth, phone_num)
            list_students.append(student)
    return list_students

list_student = create_students_list("students")       # Створення списку студентів (Class Students) з файлу
for item in list_student:
    print(item)

print()

title = "Python Pro"                                   # Створення групи (Class Group) із списку студентів
group_1 = Gr_cl.Group(title)
for item in list_student[0:9]:
    group_1.add_new_student(item)
print(group_1)

print()

st_1 = St_cl.Students("Lakuta", "Volodymyr", "1999", "0349876543")
group_1.add_new_student(st_1)
print(group_1)

print()

print (group_1.search_student("mazur"), "\n")

group_1.del_student("mazur")

print(group_1)