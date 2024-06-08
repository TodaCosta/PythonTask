a, b, c= 'Ira,', 'Yasya,', 'Tanya.'
print(a, b, c)

#сразу присваивает
a = 5
b = 6
c = a
a = b
b = c
print(a, b)
#или
a = 5
b = 6
a, b = b, a
print(a, b)