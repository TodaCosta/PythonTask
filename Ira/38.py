import re

c = input().split('=')
d = input().split('=')
g = input().split('=')
def get_inductees(*args):
    print(args)
    tt = []
    ggg = []
    for i in (args):
        for j in range(1, len(i), 2):
            tt.append(i[j])
    print(tt)
    for k in tt:
        print(k)
        ffff = [k]
        ggg.append(ffff)
    print(ggg)

get_inductees(c, d, g)

    # di = {}
    # ss = []
    # for i, j in args:
    #     di[i] = j
    # for i in di.values():
    #     ss.append(i)
    # print(list(itertools.product(ss)))
