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
    
print(calculator(5, 7, "+"))