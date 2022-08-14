from datetime import datetime

n = 10**6

def timeit(func):  # принимает некоторую функцию, название в скобках можно любое
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)  # вызов полученной функции из timeit
        print(datetime.now() - start)
        return result  # возвращает некий рез-т
    return wrapper  # возвращает функцию wrapper(можно дать любое название)

@timeit
def one(n):
    #start = datetime.now()
    l1 = []
    for i in range(n):
        if i % 2 == 0:
            l1.append(i)
    #print(datetime.now() - start)
    return l1
one(n) #0:00:00.087803

@timeit
def two(n):
    l = [x for x in range(n) if x%2==0]
    return l
two(n) #0:00:00.072804