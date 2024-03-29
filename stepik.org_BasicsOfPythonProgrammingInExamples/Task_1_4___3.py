'''
Задача
По номеру года найти число дней в этом году (вывести 365, если это не високосный год, или 366, если високосный).

Указание. В современном (григорианском) календаре каждый год, номер которого делится на 4, является високосным,
за исключением тех, которые делятся на 100 и при этом не делятся на 400. Например, 1900 год - не високосный, 2000 год - високосный.

Григорианский календарь был введен в 1582 году, поэтому если пользователь введет значение, меньшее 1582, то вывести "error".
'''

year = int(input())

if year < 1582:
    print("error")
elif year % 4 == 0 and year % 100 != 0:
    print(366)
elif year % 400 == 0:
    print(366)
else:
    print(365)
