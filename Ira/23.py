class Vehicle:
    pass
class Car(Vehicle):
    pass
class RaceCar(Car):
    pass
class Plane(Vehicle):
    pass
class Boat(Vehicle):
    pass

class NewInt(int):
    def repeat(self, n=2):
        return int(str(self)*n)
    def to_bin(self):
        c = bin(self)
        return int(str(c[2:]))

t = NewInt(33)
print(t.repeat(3))
print(t.to_bin())
a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35
