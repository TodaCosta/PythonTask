# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def __add__(self, other):
#         if isinstance(other, Bank):
#             return self.balance + other.balance
#         if isinstance(other, (int, float)):
#             cf = self.balance+other
#             self.balance = cf
#             return cf
#         raise NotImplemented
#
# d = Bank("Jek", 100)
# m = Bank("Meg", 230)
# print(d+100) #200
# print(d.balance) # 200
# print(d+500) # 700
# print(d.balance) # 700
# print(d+m) # 930

class Vector:

    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if len(self.values) > 0:
            return f"Вектор{tuple(self.values)}"
        return f"Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[i + other for i in self.values])
        if isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return print("Сложение векторов разной длины недопустимо")
            return Vector(*[k + v for k,v in zip(self.values, other.values)])
        return print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[i * other for i in self.values])
        if isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return print("Умножение векторов разной длины недопустимо")
            return Vector(*[k * v for k,v in zip(self.values, other.values)])
        return print(f"Вектор нельзя умножать с {other}")

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
v8 = Vector(1, 4, 9)
print(v8.values)
print(v1.__mul__(5)) # Вектор(5, 10, 15)

