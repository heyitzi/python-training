def calculator(a, b, symbol):
    operators = ["+", "-", "*", "/"]
    if operators.index(symbol) == 0:
        return a + b
    elif operators.index(symbol) == 1:
        return a - b
    elif operators.index(symbol) == 2:
        return a * b
    else:
        return a / b
    
num1 = input("First number: ")
num2 = input("Second number: ")
operation = input ("Add the symbol for the operation you want to execute: ")

print(calculator(int(num1), int(num2), operation))