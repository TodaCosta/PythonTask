def find_top_20(*args):
    a = {}
    b = []
    lli = []
    ff = []
    vv = []
    for i in args:
        for j in i:
            c = j.values()
            #print(c)
            for h in c:
                b.append(h)
    print(b)
    for i in range(len(b)):
        if i % 3 == 0:
            a[b[i]] = 0
    for j in range(1,len(b),3):
        g = sum(b[j].values())
        lli.append(g)
    print(lli)
    for k in range(2,len(b),3):
        ff.append(b[k])
    ccc = list(int(i) + int(j) for i, j in zip(lli, ff))
    jj = dict(zip(a, ccc)) #lli

    #ss = sum(zip(a, ccc))
    print(jj)
    #print(ss)
    #print(ff)
    jj = dict(sorted(jj.items(), reverse=True, key=lambda x: x[1]))
    for k,v in list(jj.items())[:20]:
        vv.append(k)
    print(vv)

find_top_20([{"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}])