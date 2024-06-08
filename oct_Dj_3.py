a = list(map(str, input())) #CMXC
f = []
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
     'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


def wrapper(a, a1, a2):
    for j in range(len(a)):
        if j+1 < len(a):
            if a[j] == a1 and a[j+1] == a2:
                # if a1 in a and a2 in a:
                #     if a.index(a1) < a.index(a2):
                sum_min_I = a1 + a2
                a.pop(a.index(a1))
                a.pop(a.index(a2))
                return a.append(sum_min_I)

#CMXC
if 'C' and 'M' in a:
    wrapper(a, a1='C', a2='M')
if 'C' and 'D' in a:
    wrapper(a, a1='C', a2='D')
if 'X' and 'C' in a:
    wrapper(a, a1='X', a2='C')
if 'X' and 'L' in a:
    wrapper(a, a1='X', a2='L')
if 'I' and 'X' in a:
    wrapper(a, a1='I', a2='X')
if 'I' and 'V' in a:
    wrapper(a, a1='I', a2='V')

# if 'I' in a and 'V' in a:
#     if a.index('I') < a.index('V'):
#         sum_min_I = 'I'+'V'
#         a.pop(a.index('I'))
#         a.pop(a.index('V'))
#         a.append(sum_min_I)


for i in a:
    f.append(d.get(i))
sum_dict = sum(f)
print(sum_dict)

s = input()

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

prev = values[s[0]]
result = 0

for c in s:
    current = values[c]
    # если значение очередного символа больше, чем значение предыдущего,
    # значит предыдущий должен был вычитаться.
    # Поскольку он до этого уже был прибавлен - вычитаю его в двойном объеме.
    if current > prev:
        result -= prev * 2

    result += current
    prev = current

print(result)






s11 = input()
d11 = {'CM':900, 'M':1000, 'CD':400, 'D':500, 'XC':90, 'C':100, 'XL':40, 'L':50, 'IX':9, 'X':10, 'IV':4, 'V':5, 'I':1}
num = 0
for (k, v) in d11.items():
    if k in s11:
        num += s11.count(k) * v
        s11 = s11.replace(k, '')
        print(s11)
print(num)


#MCMXCIV
arim = input()
drim = {'CM': 900, 'M': 1000, 'CD': 400, 'D': 500, 'XC': 90, 'C': 100, 'XL': 40, 'L': 50, 'IX': 9, 'X': 10,
         'IV': 4, 'V': 5, 'I': 1}
res_rim = 0
for (k, v) in drim.items():
    if k in arim:
        res_rim += arim.count(k) * v
        arim = arim.replace(k, '')
print(res_rim)

