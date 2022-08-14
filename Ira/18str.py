class Lion:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"объект - {self.name}"
    def __str__(self):
        return f"Lion {self.name}!"

d = Lion("Simba")
print(d.name) # Simba
print(d) # объект - Simba (если нет ф-ции __str__) \ Lion Simba! -если есть __str__
# ____________________________________________________________________________________________
class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        self.gender = gender
    #
    # @property
    # def gender(self):
    #     return self.__gender
    #
    # @staticmethod
    # def is_1gender(gender):
    #     if gender == "male" or gender == "female":
    #         return True
    #     return False
    #
    # @gender.setter
    # def gender(self, value):
    #     if not Person.is_1gender(value):
    #         print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
    #         self.__gender = "male"
    #     self.__gender = value

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        elif self.gender == "female":
            return f"Гражданка {self.surname} {self.name}"
        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"
            return f"Гражданин {self.surname} {self.name}"



p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', "ff")# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"
print(p3.gender)
# ___________________________________________________________________________________________________________

class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if len(self.values) > 0:
            st = ", ".join(str(e) for e in self.values)
            return f"Вектор({st})"
        return f"Пустой вектор"


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"