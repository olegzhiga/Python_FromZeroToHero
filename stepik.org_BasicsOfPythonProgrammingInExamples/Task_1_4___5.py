'''
Задача
Посчитать, сколько банок краски необходимо, чтобы окрасить внутреннюю площадь бассейна кубической формы со стороной а метров,
если расход краски на 1 квадратный метр  составляет b миллилитров, а в банке содержится v литров краски.

При вводе неверных данных  вывести '"error".
'''
import math

a = float(input())
b = float(input())/1000
v = float(input())

if a <= 0 or b <= 0 or v <= 0:
    print("error")
else:
    S = a**2 * 5
    paintCaps = (S * b) / v
    print(math.ceil(paintCaps))
