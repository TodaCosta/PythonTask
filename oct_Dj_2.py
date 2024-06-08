import os
x = ["flower", "flow", "flight"]
print(os.path.commonprefix(x))



d=["flower", "flow", "flight"]
d1=d[0]
for i in range(1, len(d)):
    while d[i].find(d1) != 0:
        d1 = d1[:-1]
print(d1)


x = ["flower", "flow", "flight"]
y = x[0]
for i in range(len(x)):
    while x[i].find(y) != 0:
        y = y[:-1]
print(y)

aaa = ["дельце", "дела", "дел", "дела", "делавой"]
aaa1 = aaa[0]
print(aaa1.find("дела"))
for i in range(len(aaa)):
    while aaa[i].find(aaa1) != 0:
        aaa1 = aaa1[:-1]
print(aaa1)
