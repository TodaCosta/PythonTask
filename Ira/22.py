class Quadrilateral:
    def __init__(self, width, height=0):
        self.width = width
        self.height = height
        if height == 0:
            self.width = width
            self.height = self.width
    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        return f"Прямоугольник размером {self.width}х{self.height}"
    def __bool__(self):
        return self.height == self.width

q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q1 == True)  # печатает "False"

while True: print(eval(input('>>>')))

