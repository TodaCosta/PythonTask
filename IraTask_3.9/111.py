# def f(x):
#     if getattr(f, "x", None) is None:
#         f.x = x

# f(6)
# f(7)
# print(f.x)  # 1
# setattr(f, "x", 67)
# print(f.x)  # 2
#
# def j(a):
#     j.a = a
#
# j(6)
# j(7)
# print(j.a)

# print(j.a)
# setattr(j, "a", 67)
# print(j.a)


# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# d = {k: d[k] for k in sorted(d, key=d.get, reverse=True)}
# print(d)
# print(sorted(d.values(), reverse=True))

# def ball(n):
#
#     blue = 1
#     red = 0
#
#     b1, r1 = "синий", "красный"
#     b2, r2 = "синих", "красных"
#     if blue % 10 == 1:
#         b = b1
#     else:
#         b = b2
#     if red % 10 == 1:
#         r = r1
#     else:
#         r = r2
#
#     if n < 0:
#         print("Введите n >= 0")
#         return ball(int(input()))
#     else:
#         blue = int((5*n**2-5*n+2)/2)
#         red = int(5 * n)
#         return print(f"{blue} {b} + {red} {r}")
# ball(int(input()))



my_dict = {
    '1': 1,
    '2': 2,
    '3': 3
}


def MYFUNC(**kwargs):
    """ return max """
    try:
        max_value = sorted(kwargs.values())[-1]
        """if need key of maxValie
            for key, values in kwargs.items():
                if values == maxValue:
                    return key"""
        return max_value
    except:
        pass


print(MYFUNC(**my_dict))
a = [1, 2, 3]
flag = True
for i in a:
    if i == 1:
        flag = False
        print("false")
        break
if flag == True:
    print("true")



