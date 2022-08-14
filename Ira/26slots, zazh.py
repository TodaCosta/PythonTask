class React:
    __slots__ = '__width', 'height'
    def __init__(self, a, b):
        self.width = a
        self.height = b
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        print("setter called")
        self.__width = value
c = React(5, 6) # напеч-ся сразу атоматом setter called
print(c.width) # 5 - идет в сеттер, потом в геттер
print(c._React__width) # 5 - достучатся до закрытой переменной