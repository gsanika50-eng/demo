import sys

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(op: str, a: float, b: float) -> float:
    if op in ("add", "+"):
        return add(a, b)
    elif op in ("subtract", "sub", "-"):
        return subtract(a, b)
    elif op in ("multiply", "mul", "*"):
        return multiply(a, b)
    elif op in ("divide", "div", "/"):
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operation: {op}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 calculator.py <operation> <num1> <num2>")
        print("Operations: add (+), subtract (-), multiply (*), divide (/)")
        sys.exit(1)

    op = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
        result = calculate(op, num1, num2)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
