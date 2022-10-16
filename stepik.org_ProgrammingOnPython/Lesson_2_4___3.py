'''
Узнав, что ДНК не является случайной строкой,
только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия,
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку,
кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод.
Кодирование должно учитывать регистр символов.
'''

inputString = input()
i = 0
firstLetter = inputString[0]
letterCounter = 0
resultString = ""

while i < len(inputString):
    if firstLetter == inputString[i]:
        letterCounter += 1
    else:
        resultString = resultString + firstLetter + str(letterCounter)
        firstLetter = inputString[i]
        letterCounter = 1
    i += 1

print(resultString + inputString[-1::] + str(letterCounter))
