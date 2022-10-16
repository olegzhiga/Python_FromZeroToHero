def maxArr(*numbers):
    x = numbers[0]
    for i in numbers:
        if x < i:
            x = i
    return x


def minArr(*numbers):
    x = numbers[0]
    for i in numbers:
        if x > i:
            x = i
    return x


def sumArr(*numbers):
    x = 0
    for i in numbers:
        x += i
    return x


'''
1) Создайте свой модуль и подключите его в основном файле.
2) Напишите в модули 3 функции, каждая из которых принимает список. Первая функция – получение максимального значения, вторая – получение минимального значения, третья – получение суммы всех элементов.
3) Проверьте работу этих функций в основном файле.
'''
