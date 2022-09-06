# Task 4
import time

def timer(n : int, file_name : str):
    if not isinstance(n, int): return TypeError
    def wrapper(func):
        start = time.time()
        t_start = time.localtime(start)
        for i in range(n):
            def get_ans(*args, **kwargs):
                return func(*args, **kwargs)
        end = time.time()
        t_end = time.localtime(end)
        with open(file_name, "a") as file_obj:
            file_obj.write(f"\nThe function {func.__name__.upper()} had called {n} times\n"
                           f"Start {t_start}\n End {t_end}\n Total runtime {end - start} sec.\n")
        return get_ans
    return wrapper


''' Revice '''

n = 1000000
file_name = "Timer.txt"

@timer (n, file_name)
def sum_sequince(sequince, pov_func = lambda x: x**2):
    if not all(isinstance(x, (int, float)) for x in sequince):
        return TypeError
    res = 0
    for elem in sequince:
        res += pov_func(elem)
    return res


seq = [0, 1, 2, 3]

t = sum_sequince(seq)
print(t)









