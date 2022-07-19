import re


class User:
    def __init__(self, login, pswrd):
        self.__login = login
        self.password = pswrd

    # PASSWORD
    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_number(pswrd):
        count_digit = 0
        for i in pswrd:
            if i.isdigit():
                count_digit += 1
        if count_digit > 1:
            return True
        return False

    @staticmethod
    def is_include_all_register(pswrd):
        count_reg = 0
        for i in pswrd:
            if i.isupper() == True:
                count_reg += 1
        if count_reg >= 2:
            return True
        return False

    @staticmethod
    def is_include_only_latin(pswrd):
        if re.search(r'[^a-zA-Z0-9]', pswrd):
            return False
        return True

    @staticmethod
    def check_password_dictionary(pswrd):
        with open("easy_password.txt", "r") as file:
            if pswrd in file.read():
                return False
            return True

    @password.setter
    def password(self, pswrd):
        if not isinstance(pswrd, str):
            raise TypeError('Пароль должен быть строкой')
        if len(pswrd) < 4:
            raise ValueError('Пароль короткий')
        if len(pswrd) > 14:
            raise ValueError('Пароль слишком длинный')
        if not User.is_include_number(pswrd):
            raise ValueError('Пароль должен содержать цифры')
        if not User.is_include_all_register(pswrd):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not User.is_include_only_latin(pswrd):
            raise ValueError('Пароль должен содержать только латинские буквы')
        if not User.check_password_dictionary(pswrd):
            raise ValueError('Пароль слишком легкий')

        self.__password = pswrd

    # LOGIN
    @property
    def login(self):
        return self.__login

    @staticmethod
    def is_log_valide(email):
        count_dot = 0
        count_email_sight = 0
        for i in email:
            if i == '@':
                count_email_sight += 1
            if i == '.':
                count_dot += 1
        if count_dot < 1 or count_email_sight != 1:
            return False
        return True

    @login.setter
    def login(self, email):
        if not User.is_log_valide(email):
            raise ValueError('В логине должна быть хотя бы одна точка и один знак @')
        self.__login = email

"""
test
a = User('Ivan@dsf.com', 'MMini1980')
a.password = 'dsgjFFFFsa42F'
print(a.password)
a.login = "grmany@gmail.com"
print(a.login)
"""
