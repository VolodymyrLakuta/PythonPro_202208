def fibonachi_recursion(n, first_number = 0, second_number = 1, count = 1):
    if not isinstance(n, int): return TypeError
    elif n <= 0: return ValueError
    elif n == 1: return 0
    elif n == 2: return 1
    
    if count == n - 1:
        return second_number
    else:
        next_number = second_number + first_number
        first_number = second_number
        second_number = next_number
        count += 1
    return fibonachi_recursion(n, first_number, second_number, count)


f = fibonachi_recursion
print (f(8))


