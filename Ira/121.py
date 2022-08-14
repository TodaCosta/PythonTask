from numpy import *
dg = {}
for j in range(1, 13):
    dg[j] = 0
print(dg)
d = []
dl = arange(21,381).reshape(12, 30)
for i in dl:
    i = list(i)
    d.append(i)
print(d)
ch = dict(zip(dg, d))
print(ch)
chis = 243
for k,v in ch.items():
    for i in v:
        if chis == i:
            print(k)
sd={}
fr = list(ch)
fr = fr[9:] + fr[:9]
for i in fr:
    sd[i] = 0
print(sd)

# for value in ch:
#     for i in ch[value]:
#         if chis in ch[value]:
#             print(ch[value])