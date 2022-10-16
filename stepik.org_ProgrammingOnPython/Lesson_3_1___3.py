'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
'''


def modify_list(l):
    # put your python code here
    counter = 0
    while counter < len(l):
        # remove all odd numbers
        if l[counter] % 2 != 0:
            l.remove(l[counter])
        # divide all even numbers
        elif l[counter] % 2 == 0:
            l[counter] = int(l[counter] / 2)
            counter += 1
        else:
            break

# Test 1
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

# Test 2
lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)  # [5, 4]

# Test 3
lst = [1, 3, 5, 7]
modify_list(lst)
print(lst)  # []
