from accessify import private, protected


class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @private
    def print_priv(self):
        print(self.name, self.balance)


acc1 = Bank("Jen", 10000)
print(acc1.__dict__)
# acc1.print_priv() - ошибка доступа

# _____________________________________

import re
class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email
    def get_email(self):
        return self.__email
    def set_email(self, email):
        if isinstance(email, str) and re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', email):
            self.__email = email
        else:
            print('Ошибочная почта')
    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3]  # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
