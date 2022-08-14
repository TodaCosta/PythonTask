class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        if len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        if not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance


    def __eq__(self, value):
        if not isinstance(value, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {value}")
        elif self.currency != value.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        elif self.currency == value.currency:
            return self.balance == value.balance

    def __add__(self, value):
        if not isinstance(value, Wallet) or self.currency != value.currency:
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(value.currency, self.balance + value.balance)

    def __sub__(self, value):
        if not isinstance(value, Wallet) or self.currency != value.currency:
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(value.currency, self.balance - value.balance)



c = Wallet("USD", 100)
g = Wallet("USD", 200)
print(c.currency) # USD
print(g.currency) # USD
print(c == g) # False
print(c+g) # <__main__.Wallet object at 0x0000020844023E50>


