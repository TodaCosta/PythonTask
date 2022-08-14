a=['1', '2', '3']
b=['5', '6', '7']
for i in a:
    for j in b:
        print(i+" + " +j)
d =list(zip(a,b))
print(d)
for i in d:
    print("+".join(i))