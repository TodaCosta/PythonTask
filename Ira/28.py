s = "Hello"
n = int(input())
try:
    print(s[n])
    s[n]
except:
    print("Нет такого индекса")
