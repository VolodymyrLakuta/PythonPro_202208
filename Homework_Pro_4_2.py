import math

class ProperFraction:

    def __init__(self, a : int, b : int):
        if b < 0:
            self.a = -1 * a
            self.b = -1 * b
        else:
            self.a = a
            self.b = b

    def __str__(self):
        return f'{self.a}/{self.b}'
    
    def __add__(self, other):               # Метод додавання
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        if not a:
            rez = 0
        elif abs(a)/abs(b) == 1:
            rez = int(a/b)
        elif abs(a) > abs(b):
            rez = improper_fraction(a, b)
        else:
            rez = ProperFraction(int(a/math.gcd(a, b)), int(b/math.gcd(a, b)))
        return rez

    def __sub__(self, other):               # Метод віднімання
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        if not a:
            rez = 0
        elif abs(a)/abs(b) == 1:
            rez = int(a/b)
        elif abs(a) > abs(b):
            rez = improper_fraction(a, b)
        else:
            rez = ProperFraction(int(a/math.gcd(a, b)), int(b/math.gcd(a, b)))
        return rez

    def __mul__(self, other):      # Метод множення
        a = self.a * other.a
        b = self.b * other.b
        return ProperFraction(int(a/math.gcd(a, b)), int(b/math.gcd(a, b)))

    '''
    Методи порівняння
    '''
    def __lt__(self, other):
        if (self.b == other.b and self.a < other.a) or (
            self.a == other.a and self.b > other.b) or (
            self.a * other.b < other.a * self.b):
            return True
        else:
            return False

    def __le__(self, other):
        if (self.b == other.b and self.a <= other.a) or (
            self.a == other.a and self.b >= other.b) or (
            self.a * other.b <= other.a * self.b):
            return True
        else:
            return False
    
    def __gt__(self, other):
        if (self.b == other.b and self.a > other.a) or (
            self.a == other.a and self.b < other.b) or (
            self.a * other.b > other.a * self.b):
            return True
        else:
            return False

    def __ge__(self, other):
        if (self.b == other.b and self.a >= other.a) or (
            self.a == other.a and self.b <= other.b) or (
            self.a * other.b >= other.a * self.b):
            return True
        else:
            return False
    
    def __eq__(self, other):
        if (self.b == other.b and self.a == other.a) or (self.a * other.b == other.a * self.b):
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.b != other.b and self.a != other.a) or (self.a * other.b != other.a * self.b):
            return True
        else:
            return False


def improper_fraction(a, b):        # Неправильний дріб
    return f"{a//b} and {int((abs(a)-abs(b))/math.gcd(a, b))}/{int(abs(b)/math.gcd(a, b))}"
              
fr1_a, fr1_b = map(int, input("Input fraction a/b: ").split("/"))
fr1 = ProperFraction (fr1_a, fr1_b)

fr2_a, fr2_b = map(int, input("Input fraction a/b: ").split("/"))
fr2 = ProperFraction (fr2_a, fr2_b)

print (fr1, " + ", fr2, " = ", fr1 + fr2)

print (fr1, " - ", fr2, " = ", fr1 - fr2)

print (fr1, " * ", fr2, " = ", fr1 * fr2)

print (fr1, " < ", fr2, "\n", fr1 < fr2)

print(fr1, " != ", fr2, "\n", fr1 != fr2)