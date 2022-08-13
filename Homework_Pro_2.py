class Human:
    def __init__(self, surname, name, gender, year_birth):
        self.surname = surname
        self.name = name
        self.gender = gender
        self.year_birth = year_birth
      
    def  __str__(self):
        return f"{self.surname} {self.name}, {self.gender}, {self.year_birth}\n"

class Students(Human):
    student_list = []

    def __init__(self, surname, name, gender, year_birth, phone_num):
       super().__init__(surname, name, gender, year_birth)
       self.phone_num = phone_num
       self.student_dict = {}
       
    def stud_list (self):     # Список студентів
        self.student_dict = {
                    "Surname" : self.surname, "Name" : self.name, "Gender" : self.gender, 
                    "Year_birth" : self.year_birth, "Phone_num" : self.phone_num
                     }    
        Students.student_list.append(self.student_dict)
        return Students.student_list

    def  __str__(self):
        return f"{self.surname} {self.name}, {self.year_birth}, phone {self.phone_num}"

    def add_new_student ():
        surname, name, gender, year_birth, phone_num = input ("Input the student (5 attr): ").split() 
        # Новий студент
        student = {
                    "Surname" : surname, "Name" : name, "Gender" : gender, 
                    "Year_birth" : year_birth, "Phone_num" : phone_num
                     }
        Students.student_list.append(student)
        return student

class Group:
    def __init__(self, title):
        self.title = title
        self.group_list = []

    def create_group_list (self, student_list): # Створення початкового списку групи із списку студентів
        for student in student_list:
            print ("\n", student)
            ans = input(f'''Add this student to the group "{self.title}"? y/n: ''')
            if len(self.group_list) == 10:
                print ("\nThere should not be more than ten students in a group\n")
                break
            if ans =="y" and student in self.group_list:
                print ("\nThis student is already in the group list\n")
            elif ans =="y":
                self.group_list.append(student)
        return self.group_list

    def add_new_student (self, student):
        if len(self.group_list) == 10:
            print ("\nThere should not be more than ten students in a group\n")
        else:
            if student in self.group_list:
               print ("\nThis student is already in the group list\n")
            else:
               self.group_list.append(student)
        return self.group_list

    def search_student (self, student_name):         # Пошук студентів за прізвищем
        k = 0             
        for i, student in enumerate(self.group_list):
            if student.get("Surname") == student_name:
                k += 1
                print (f"\n{i+1}. {student.get('Surname')} {student.get('Name')}")
                ans = input ("\nContinue? y/n: ")
                if ans != "y":
                    break
        if k:
            print (f"\nStudents found: {k}")
        else:
            print (f'''Student with surname "{student_name}" in the group "{self.title}" not found''')

    def del_student (self, student_name):              # Видалення студента (пошук за призвіщем)
        k = 0
        for i, student in enumerate(self.group_list):
            if student.get("Surname") == student_name:
                print (f"\n{i+1}. {student.get('Surname')} {student.get('Name')}")
                ans = input (f"\nDelete this student? y/n: ")
                if ans == "y":
                    del self.group_list[i]
                    k += 1
                ans = input ("\nContinue? y/n: ")
                if ans != "y":
                    break
        if k:
            print (f"\nDeleted students: {k}")
        else: 
            print (f'''Student with surname "{student_name}" in the group "{self.title}" not found''')

    def __str__ (self):
        print (f"\n{self.title}\n")
        for i, student in enumerate(self.group_list):
            print (f"{i+1}. {student.get('Surname')} {student.get('Name')}")            
        
def create_students_list():                 # Використовується текстовий файл (є дубльовані студенти)
    filename = input("Input the student list file name: ")
    with open (filename, "r") as list_file:
        lines = list_file.readlines()
        del (lines[-1])                    # Видалення знаку переносу рядка
        for item in lines:
            item_1 = item[0:-1]            # Видалення знаку переносу рядка
            surname, name, gender, year_birth, phone_num = item_1.split()
            student = Students (surname, name, gender, year_birth, phone_num)
            student.stud_list()
            print (student)

create_students_list()                        # Створення списку студентів (Class Students)

title = "Python Pro"                           # Створення групи (Class Group) із списку студентів
group_1 = Group(title)
group_1.create_group_list(Students.student_list)
group_1.__str__()
print()

student_1 = Students.add_new_student()         # Додавання нового студента до списку студентів

print ("\n", student_1, "\n")

print(Students.student_list)                   # Перевірка додавання студента до списку студентів (останній)

ans = input (f'''\nAdd this student to the group "{title}"? y/n: ''') # Додавання студента в групу
if ans == "y":
    group_1.add_new_student(student_1)

group_1.__str__()

student_name = input ("\nInput surname of student for search: ")  # Пошук студента за призвіщем
group_1.search_student(student_name)

student_name = input ("\nInput surname of student for delete: ")  # Видалення студента
group_1.del_student(student_name)

group_1.__str__()





