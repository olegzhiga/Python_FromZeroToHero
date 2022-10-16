'''
В институте биоинформатики ...
'''

n = int(input())

# find last number of input value
lastNum = n % 10
# find 2 last number of input value
last2Num = n % 100

print(lastNum)
print(last2Num)

if n > 99 and (last2Num == 11 or last2Num == 12 or last2Num == 13 or last2Num == 14):
    print(f"{n} программистов")
elif n == 11 or n == 12 or n == 13 or n == 14:
    print(f"{n} программистов")
else:
    if (lastNum == 1):
        print(f"{n} программист")
    elif (lastNum >= 2 and lastNum <= 4):
        print(f"{n} программиста")
    elif (lastNum == 0 or lastNum >= 5 and lastNum <= 9):
        print(f"{n} программистов")
