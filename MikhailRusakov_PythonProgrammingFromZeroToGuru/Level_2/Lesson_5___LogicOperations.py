
true = True
false = False

print("true or false =", true or false)
print("true and false =", true and false)
print("not false =", not false)
print("true != false =", true != false)
print("true == false =", true == false)

print("---------------")

x = 10
y = 100
print(x, ">", y, "=", x > y)
print(x, "<", y, "=", x < y)
print(x, ">=", y, "=", x >= y)
print(x, "<=", y, "=", x <= y)
print(x, "!=", y, "=", x != y)
print(x, "==", y, "=", x == y)

print("---------------")

print(True and (True or (False and True or False) and True or True != False))
print(15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))



'''
1) Самостоятельно подумайте, чему будет равно следующее логическое выражение: True and (True or (False and True or False) and True or True != False)
2) Проверьте себя, выведя результат этого выражения с помощью функции print().
3) Самостоятельно подумайте, чему будет равно следующее логическое выражение: 15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18)
4) Проверьте себя, выведя результат данного выражения с помощью функции print().
'''