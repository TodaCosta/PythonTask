#замыкание
def decator(func):
    def inner():
        print("start")
        func()
        print("finish")
    return inner
def say():
    print("hello")
decator(say)() # или d = decator(say) и потом d()
#start
#hello
#finish
# _____________________

from datetime import datetime
n = 10
def timeit(arg):
    print(arg)
    def outer(func):
        def wrapper(n):
            start = datetime.now()
            result = func(n)
            print(datetime.now()-start)
            return result
        return wrapper
    return outer
@timeit('name')
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

two(n) #0:00:00
print(two(n)) #0:00:00 \ [0, 2, 4, 6, 8]
print(timeit(two)) #<function timeit.<locals>.wrapper at 0x000001A910EDB370>
print(timeit(two)(n)) # 0:00:00 \ 0:00:00 \ [0, 2, 4, 6, 8]
print(timeit('name')(two)(n)) # name \ name \ 0:00:00 \ 0:00:00 \ [0, 2, 4, 6, 8]
print(two(n)) #0:00:00 \ [0, 2, 4, 6, 8]