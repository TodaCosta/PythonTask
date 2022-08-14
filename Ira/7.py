a = int(input())
c = []
count = 0
for i in range(a+1):
    i = int(input())
    c.append(i)
for i in range(len(c)-1):
    for j in range(i+1,len(c)-1):
        if c[i]*c[j]==c[-1]:
            count += 1
if count > 0:
    print('ДА')
else:
    print('НЕТ')