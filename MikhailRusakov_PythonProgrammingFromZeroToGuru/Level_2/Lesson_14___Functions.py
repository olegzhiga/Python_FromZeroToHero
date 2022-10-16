
def evenNumber (x):
    if x % 2 == 0:
        return True
    else:
        return False

def maxNumber (*numbers):
    x = numbers[0]
    for i in numbers:
        if x < i:
            x = i
    return x

def middleArifmetic (*numbers):
    x = 0
    for i in numbers:
        x += i
    return x/len(numbers)

print(evenNumber(10))
print(evenNumber(9))
print(maxNumber(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(middleArifmetic(1, 2, 3, 4, 5, 6, 7, 8, 9))

'''
1) Создайте функцию, которая проверяет чётное число передано в параметре или нет. Она должна возвращать True или False.
2) Создайте функцию, которая принимает список и возвращает максимальное значение из списка.
3) Создайте функцию с переменным числом аргументов, внутри которой должно выводиться среднее арифметическое переданных чисел.

Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое на их количество.
'''