class Person:
    name = "Ivan"
    age = "30"


    def drive():
        print('Let is go')
print(Person.name)
print(Person.__dict__)
print(getattr(Person, 'name'))
print(Person.__name__)
Person.drive()


def go():
    print("Yes")
go() # выводится без принт Yes


class Cat:
    def hello():
        print("Hello world from kitty!")
# hello() - оштбка, потому что это уже не ф-ция, а метод класса

class Cat:
    def hello(*args):
        print("Hello world from kitty!", args)
jim = Cat()
jim.hello() # Hello world from kitty! (<__main__.Cat object at 0x0000020D812F3FD0>,)


class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty!", args)
    def show_breed(instance):
        print(f'my breed is {instance.breed}')
walt = Cat()
walt.show_breed() # my breed is pers


class Cat:
    def show_name(instance):
        if hasattr(instance, "name"):
            print(f'my name is {instance.name}')
        else:
            print("nothing")
mary = Cat()
mary.show_name() # nothing
# присваиваем атрибуту имя и всё заработает
mary.name = "Mary"
mary.show_name() # my name is Mary


class Cat:
    breed = 'pers'
    def show_breed(self):
        print(f'my breed is {self.breed}')
    def show_name(self):
        if hasattr(self, "name"):
            print(f'my name is {self.name}')
        else:
            print("nothing")
    def set_value(self, value, age = 10):
        self.name = value
        self.age = age
tom = Cat()
tom.set_value('Tom', 5)
tom.show_name()
print(tom.age) #5

# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
# В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент
# - значение, с которого начинается подсчет, по умолчанию равно 0
# Также нужно создать метод increment, который увеличивает счетчик на 1.
# Затем необходимо создать метод display, который печатает фразу "Текущее значение
# счетчика = <value>" и метод reset, который обнуляет экземпляр счетчика
class Counter:
    def start_from(self, x= 0):
        self.x = x
    def increment(self):
            self.x += 1
    def display(self):
        print(f"Текущее значение счетчика = {self.x}")
    def reset(self):
        self.x = 0

c1 = Counter()
c1.start_from()
c1.increment()
c1.display() # Текущее значение счетчика = 1
c1.increment()
c1.display() # "Текущее значение счетчика = 2"
c1.reset()
c1.display() # "Текущее значение счетчика = 0"
# _____________________________________________________


# Создайте класс Point. У этого класса должны быть
# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса
# соответственно в атрибуты x и y метод get_distance, который обязательно принимает
# экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора.
# В случае, если в данный метод передается не экземпляр класса Point необходимо вывести "Передана не точка"
class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, point):
        if isinstance(point, Point):
            return ((point.x-self.x)**2+(point.y-self.y)**2)**0.5
            # если после return поставить print, распечатается 5.0
        print("Передана не точка")

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
# ___________________________________________________________________________

class Cat:
    def __init__(self):
        print('hello')
tom = Cat() # hello
print(tom.__dict__) # {}
#__________________________

class Cat:
    def __init__(self, name, breed = 'pers', age = 1, color = 'white'):
        print(self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
Cat('Tom', 'siam', 2, 'bleack')
hoj = Cat('Hoj', age = 4)
jim = Cat('Jim', color = 'orange')
print(hoj.__dict__)
print(jim.__dict__)


class Laptop:
    def __init__(self, brand, model=None, price=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = str(brand) + ' ' + str(model)
laptop1 = Laptop('acer')
laptop2 = Laptop('asus')

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)
print(hp.laptop_name)
print(laptop1.laptop_name)

# ________________________

class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists
    def score(self, goals = 1):
        self.goals += goals
    def make_assist(self, assists=1):
        self.assists += assists
    def statistics(self):
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")

leo = SoccerPlayer('Leo', 'Brido', 1, 0)
leo.score(2)
leo.make_assist()
leo.statistics()
# Brido Leo - голы: 3, передачи: 1

# ___________________________________________

class Zebra:
    def __init__(self, a=0):
        self.a = a
    def which_stripe(self):
        self.a += 1
        if self.a%2 == 0:
            print("Полоска черная")
        else:
            print("Полоска белая")

z1 = Zebra()
z1.which_stripe() # Полоска белая
z1.which_stripe() # Полоска черная
z1.which_stripe() # Полоска белая
z2 = Zebra()
z2.which_stripe() # Полоска белая

# решение лучше:
class Zebra:
    flag = True
    def which_stripe(self):
        print('Полоска белая' if self.flag else 'Полоска черная')
        self.flag = not self.flag

z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
# _________________________________

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f"{self.last_name} {self.first_name}"
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())

# ____________________________________________________

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        self.sound = sound
        return f"{self.name} says {self.sound}"

jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'

# _______________________________________________

class Stack:
    def __init__(self):
        self.values = []
    def push(self,item):
        self.values.append(item)
    def pop(self):
        if self.is_empty():
            return print("Empty Stack")
        else:
            return self.values.pop()
    def peek(self):
        if self.is_empty(): # по умолчанию если == True
            return print("Empty Stack"), None
        else:
            return self.values[-1]
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.values)
s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2
# _______________________________________________________________________



