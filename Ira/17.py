from string import ascii_letters
a = "DD44gfr"
# count = 0
# tount = 0
# for i in a:
#     if i.isupper():
#         count += 1
#     else:
#         tount += 1
# print(count, tount)

# for i in a:
#     if i in ascii_letters:
#         print("da")
g = ""
for i in a:
    if i.isalpha():
        g += i
print(g)
if all(map(lambda i: i in ascii_letters, g)):
    print("латинские")
else:
    print("Не лат")

