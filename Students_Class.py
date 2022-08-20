import Human_Class as H_cl

class Students(H_cl.Human):
    
    def __init__(self, surname : str, name : str, year_birth : str, phone_num : str):
       super().__init__(surname, name, year_birth)
       self.phone_num = phone_num
              
    def  __str__(self):
        return f"{super().__str__().rstrip()}, phone {self.phone_num}"

