
'''
Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки,
но пересыпать тоже вредно и не стоит спать более BB часов. Сейчас Аня спит HH часов в сутки.
Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
Если Аня спит менее AA часов, выведите “Недосып”, если же более BB часов, то выведите “Пересып”.

Получаемое число AA всегда меньше либо равно BB.

На вход программе в три строки подаются переменные в следующем порядке: AA, BB, HH.

Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному в задании,
т. е. если программа должна вывести "Пересып", выводы программы "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться верными.
'''

'''
A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print("Это нормально")
elif H < A:
    print("Недосып")
elif H > B:
    print("Пересып")
'''


'''
Требуется определить, является ли данный год високосным.

Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4, 
но при этом не кратен 100, либо кратен 400 
(например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).

Программа должна корректно работать на числах 1900≤n≤3000.

Выведите "Високосный" в случае, если считанный год является високосным и "Обычный" в обратном случае 
(не забывайте проверять регистр выводимых программой символов).
'''

YYYY = int(input())

if YYYY % 4 == 0 and YYYY % 100 != 0:
    print("Високосный")
elif YYYY % 400 == 0:
    print("Високосный")
else:
    print("Обычный")