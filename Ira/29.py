# 1 # import collections
# a = input()
# c = collections.Counter(a)
# print(max(c, key = c.get))


# 2 # a = input()
# r = [i for i in a.split("О")]
# f = []
# for i in r:
#     f.append(len(i))
# if "Р" not in a:
#     print(0)
# else:
#     print(max(f))
# ООРРРОООО


# c = [input() for i in range(int(input()))]
# for j in c:
#     r = "".join([i for i in j if i.isalpha()])
#     if r.startswith("anton"):
#         print(c.index(j)+1, end=" ")

# a = [input() for i in range(int(input()))]
# s = []
# st = ""
# d = {}
# ant = "anton"
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         for k in ant:
#             if a[i][j] == k:
#                 s += [i+1]
# s.append(st)
# print(s)#искать по 1 подстроке и менять отрезки


a = [input() for i in range(int(input()))]
for i in a:
    if i.find("a") or i.find("n") or i.find("t") or i.find("o") or i.rfind("n") != -1:
        if i.find("a") < i.find("n", i.find("a")) < i.find("t", i.find("n")) < i.find("o", i.find("t")) < i.rfind("n"):
            print(a.index(i) + 1, end=" ")


# лучше:

for i in range(int(input())):
    s = input()
    ant = 'anton'
    ind = 0
    for j in s:
        if j == ant[ind]:
            ind += 1
        if ind == 5:
            print(i + 1, end=' ')
            break
