'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

inputNum = [int(i) for i in input().split()]
resultArr = []
inputNum.sort()

if len(inputNum) == 1:
    print()
else:
    for i, item in enumerate(inputNum):
        if item == inputNum[i-1] and item not in resultArr:
            resultArr.append(item)

print(*resultArr)
