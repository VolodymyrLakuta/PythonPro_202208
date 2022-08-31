# Task 2

import timeit

'''
This function defines the Fibonacci numbers by Recursion
'''
def fibonachi_recursion(n):                   
    if n == 1: return 0
    elif n == 2: return 1  
    else:
        return fibonachi_recursion(n - 2) + fibonachi_recursion(n - 1)

f = fibonachi_recursion       # Revise
print (f(9))
print(timeit.timeit("fibonachi_recursion(9)", setup="from __main__ import fibonachi_recursion", number=20))


'''
This function defines the Fibonacci numbers by Closure & Memoization
'''
def fibonachi_closure():                     
    res = [0, 1]
    def get_next(n):
        if n < len(res):
            return res[n - 1]
        for i in range(len(res), n):
            first_number = res[i - 2]
            second_number = res[i - 1]
            next_number = second_number + first_number
            res.append(next_number)
        return res[-1]
    return get_next

f = fibonachi_closure()     # Revise
print (f(9))
print(timeit.timeit("fibonachi_closure()", setup="from __main__ import fibonachi_closure", number=20))

'''
This function defines the Fibonacci numbers by Memoization & Recursion
'''

def fibonachi_memo(func):                     
    res = [0, 1]
    def get_next(n):
        if n < len(res):
            return res[n - 1]
        else:
            value = func(n)
            res.append(value)
            print(res)
        return value
    return get_next

f = fibonachi_memo(fibonachi_recursion)       # Revise
print (f(9))
print(timeit.timeit("fibonachi_memo(fibonachi_recursion(9))", setup="from __main__ import fibonachi_memo, fibonachi_recursion", number=20))



