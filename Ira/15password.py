from string import digits
r = open("pass.txt")
for i in r:
    r = r.read().strip().split()
print(r) # ['qwerty', '123456789', '12345', 'qwerty123', '1q2w3e', 'password', '12345678', '111111', '1234567890']
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password # было self.__password, но теперь тут св-во из сеттера,
        # потому что на входе тоже нужно проверять пароль
    @property
    def password(self):
        return self.__password
    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False
    @staticmethod
    def is_include_pass(password):
        for i in r:
            if i == password:
                return False
        return True
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 4:
            raise ValueError("Длина пароля должна быть больше 4 символов")
        if len(value) > 12:
            raise ValueError("Длина пароля должна быть меньше 12 символов")
        if not User.is_include_number(value):
            raise ValueError("Пароль должен содержать хотя бы 1 цифру")
        if not User.is_include_pass(value):
            raise ValueError("Пароль в списке частых паролей")
        self.__password = value


f = User("cot", "fffjjjj1")
print(f.password) # fffjjjj1
f.password = "15sfsd6789" # 15sfsd6789
print(f.password)
