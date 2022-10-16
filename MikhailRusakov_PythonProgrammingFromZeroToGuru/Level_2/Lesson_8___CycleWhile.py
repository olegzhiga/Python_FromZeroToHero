
sumOfInputValue = 0
while True:
    inputValue = input("Введите любое целое число: ")
    if inputValue == "exit" or inputValue == "quit":
        break
    elif inputValue == "sum":
        print(sumOfInputValue)
        sumOfInputValue = 0
    else:
        sumOfInputValue += int(inputValue)




'''
1) Напишите программу, которая будет принимать числа от пользователя и суммировать их, пока он не напишет слово «sum».
2) Когда пользователь напишет слово «sum», должна быть выведена сумма всех чисел и начат процесс заново.
3) Если пользователь напишет «exit» или «quit», программа должна быть завершена.
'''