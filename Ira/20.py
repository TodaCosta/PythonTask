class ChessPlayer:
    def __init__ (self,  name, surname, rating):
        self.name = name
        self.surname = surname
        if isinstance(rating, int):
            self.rating = rating
    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        return "Невозможно выполнить сравнение"
    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        return "Невозможно выполнить сравнение"
    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        return "Невозможно выполнить сравнение"


# d1 = ChessPlayer("Jon", "Wik", 50)
# d2 = ChessPlayer("Jin", "Wok", 50)
# print(d1 == d2) # True
# print(d1 == 50) # True
# print(d2 > d1)
magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"
d3 = ('Caren', 'Maus', "28")
print(d3 > ian)