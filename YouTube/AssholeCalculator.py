## Asshole calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("What shoud we do with this numbers: ")
result = 0

if operation == "+":
    result = a + b
    print(f"Result {a} {operation} {b} = {result}")
elif operation == "-":
    result = a - b
    print(f"Result {a} {operation} {b} = {result}")
elif operation == "*":
    result = a * b
    print(f"Result {a} {operation} {b} = {result}")
elif operation == "/":
    result = a / b
    print(f"Result {a} {operation} {b} = {result}")
else:
    print("Do not understand command!")

