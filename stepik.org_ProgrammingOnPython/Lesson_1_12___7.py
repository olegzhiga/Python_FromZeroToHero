'''
Паша очень любит кататься на общественном транспорте, а получая билет,
сразу проверяет, счастливый ли ему попался. Билет считается счастливым,
если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают,
и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
'''

inputValue = input()
x1 = int(inputValue[0])
x2 = int(inputValue[1])
x3 = int(inputValue[2])
x4 = int(inputValue[3])
x5 = int(inputValue[4])
x6 = int(inputValue[5])

if x1 + x2 + x3 == x4 + x5 + x6:
    print("Счастливый")
else:
    print("Обычный")

