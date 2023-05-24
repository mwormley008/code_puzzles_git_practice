def calculator(x,y,op):
    if isinstance(x, int) and isinstance(y, int):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
        else:
            return "unknown value"
    return "unknown value"