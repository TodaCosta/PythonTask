#Создайте класс Money, у которого есть: конструктор __init__, принимающий
# 2 аргумента: dollars, cents. По входным аргументам вам необходимо создать атрибут
# экземпляра total_cents. свойство геттер dollars, которое возвращает количество имеющихся
# долларов;свойство сеттер dollars, которое принимает целое неотрицательное число - количество
# долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при
# этом значение центов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее
# условию, нужно печатать на экран сообщение "Error dollars"; свойство геттер cents, которое
# возвращает количество имеющихся центов; свойство сеттер cents, которое принимает целое
# неотрицательное число меньшее 100 - количество центов и устанавливает при помощи него новое
# значение в атрибут экземпляра total_cents, при этом значение долларов должно сохранятся. В случае,
# если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error
# cents"; метод __str__ (информация по данному методу), который возвращает строку вида "Ваше
# состояние составляет {dollars} долларов {cents} центов". Для нахождения долларов и центов в
# методе __str__ пользуйтесь свойствами. В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents
    @property
    def dollars(self):
        return self.total_cents // 100
    @dollars.setter
    def dollars(self, new_dolars):
        if isinstance(new_dolars, int) and new_dolars >= 0:
            self.total_cents = new_dolars * 100 + self.total_cents % 100
        else:
            print("Error dollars")
    @property
    def cents(self):
        return self.total_cents % 100
    @cents.setter
    def cents(self, new_cents):
        if isinstance(new_cents, int) and 0 < new_cents < 100:
            self.total_cents = (self.total_cents - self.total_cents % 100) + new_cents
        else:
            print("Error cents")
    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"
Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
Bill.dollars = 7
print(Bill.dollars)
print(Bill.total_cents)