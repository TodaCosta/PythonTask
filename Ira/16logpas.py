import re
from string import ascii_letters
from string import digits
r = open("easy_password.txt")
for i in r:
    r = r.read().strip().split()

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @property
    def login(self):
        return self.__login

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def check_password_dictionary(password):
        for i in r:
            if i == password:
                return False
        return True

    @staticmethod
    def is_include_all_register(password):
        count = 0
        tount = 0
        for j in password:
            if j.isupper():
                count += 1
            else:
                tount += 1
        if count >= 2 and tount > 0:
            return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        g = ""
        for h in password:
            if h.isalpha():
                g += h
        if all(map(lambda k: k in ascii_letters, g)):
            return True
        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(value) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_number(value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not Registration.is_include_all_register(value):
            raise ValueError("Пароль должен содержать хотя бы 2 заглавные буквы")
        if not Registration.is_include_only_latin(value):
            raise ValueError("Пароль должен содержать только латинский алфавит")
        if not Registration.check_password_dictionary(value):
            raise ValueError("Ваш пароль содержится в списке самых легких")
        self.__password = value
# для почты использовать:
# if isinstance(email, str) and re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', email):
    @login.setter
    def login(self, value1):
        if not re.findall(r"@", value1):
            raise ValueError("Login must include at least one ' @ '")
        if not re.findall(r"\.", value1):
            raise ValueError("Login must include at least one ' . '")
        self.__login = value1
d = Registration("drqqfr@ff.ru", "tWWFd43")
print(d.login) # drqqfr@ff.ru
print(d.password) # tWWFd43
d.password = "FFas213s"
print(d.password) # FFas213s
