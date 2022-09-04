class Human:
    def __init__(self, surname : str, name : str, year_birth : str):
        self.surname = surname
        self.name = name
        self.year_birth = year_birth
      
    def  __str__(self):
        return f"{self.surname} {self.name}, {self.year_birth}\n"

