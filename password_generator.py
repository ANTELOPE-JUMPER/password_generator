import random

digits = '0123456789'
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = '!#$%&*+-=?@^_'
symbols = 'il1Lo0O'

chars = 0


def start_password_generator():
    charset = ""
    passwords = int(input('Какое количество паролей нужно: '))
    length = int(input('Введи длину пароля: '))
    if 1 == int(input('Нужны ли числа? ')):
        charset += digits
    if 1 == int(input('Нужны ли буквы нижнего регистра? ')):
        charset += lowercase_letters
    if 1 == int(input('Нужны ли буквы верхнего регистра? ')):
        charset += uppercase_letters
    if 1 == int(input('Включать ли символы !#$%&*+-=?@^_? ')):
        charset += punctuation
    if 1 == int(input('Исключать ли неоднозначные символы il1Lo0O? ')):
        for i in symbols:
            charset = charset.replace(i, '')
    password_generator(passwords=passwords, length=length, chars=charset)


def password_generator(passwords, length, chars):
    for i in range(1, passwords + 1):
        password = random.sample(chars, length)
        password = ''.join(password)
        print(f'{i}. {password}')


if __name__ == "__main__":
    start_password_generator()
