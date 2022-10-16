'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера,
у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

matrixInput = []
inputValue = input()

while inputValue != "end":
    matrixInput.append(inputValue.split())
    inputValue = input()

for i in range(len(matrixInput)):
    for j in range(len(matrixInput[i])):
        print(int(matrixInput[i-1][j]) + int(matrixInput[i-len(matrixInput)+1][j]) + int(matrixInput[i][j-1]) + int(matrixInput[i][j-len(matrixInput[i])+1]), end =" ")
    print()

