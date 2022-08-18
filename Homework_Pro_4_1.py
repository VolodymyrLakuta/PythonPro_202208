
class Rectangle:

    def __init__(self, a : int, b : int):
        self.a = a
        self.b = b

    def __str__(self):
        return f'a = {self.a}, b = {self.b}'

    def squre (self):                            # Визначення площі прямокутника
        return self.a * self.b

    '''
    Методи порівняння
    '''

    def __lt__(self, other):
        return Rectangle.squre(self) < Rectangle.squre(other)

    def __le__(self, other):
        return Rectangle.squre(self) <= Rectangle.squre(other)

    def __gt__(self, other):
        return Rectangle.squre(self) > Rectangle.squre(other)

    def __ge__(self, other):
        return Rectangle.squre(self) >= Rectangle.squre(other)

    def __eq__(self, other):
        return Rectangle.squre(self) == Rectangle.squre(other)

    def __ne__(self, other):
        return Rectangle.squre(self) != Rectangle.squre(other)
    
    '''
    Додавання прямокутників (cтворюється новий із стороною 1)
    '''
    def __add__(self, other, D = 1): 
        return Rectangle((Rectangle.squre(self) + Rectangle.squre(other)), D)

    def __iadd__(self, other, D = 1): 
        return Rectangle((Rectangle.squre(self) + Rectangle.squre(other)), D)
    
    '''
    Множення прямокутника на число
    '''
    def __mul__(self, other: int):
        if isinstance(other, int):
            return Rectangle(self.a*other, self.b*other)
        else:
            return NotImplemented
            
        
a_1 = int(input("Input length of rectangle 1: "))   # Прямокутник 1
b_1 = int(input("Input width of rectangle 1: "))
ab_1 = Rectangle(a_1, b_1)
print ("\n", ab_1, "\n")
print ("squre =", ab_1.squre(), "\n")

a_2 = int(input("Input length of rectangle 2: "))   # Прямокутник 2
b_2 = int(input("Input width of rectangle 2: "))
ab_2 = Rectangle(a_2, b_2)
print ("\n", ab_2, "\n")
print ("squre =", ab_2.squre(), "\n")

print (ab_2, " > ", ab_1, "\n", ab_2 > ab_1)

ab_3 = ab_1 + ab_2
print (ab_3)

n = int(input("Input number: "))
ab_4 = ab_1 * n
print (ab_4)
