"""Simple CLI calculator.

Usage: run the script and follow prompts. Enter 'q' at the first prompt to quit.
Supported operations: +, -, *, /, %, ** (power), ^ (power)
This file exposes `calculate(a, b, op)` so it can be imported and tested non-interactively.
"""

def calculate(a, b, op):
    """Perform calculation on two numbers.

    a, b: numbers (int or float)
    op: one of '+', '-', '*', '/', '%', '**', '^'
    Returns the numeric result or raises ValueError/ZeroDivisionError for invalid cases.
    """
    if op in ('+', 'add'):
        return a + b
    if op in ('-', 'sub'):
        return a - b
    if op in ('*', 'x', 'mul'):
        return a * b
    if op in ('/', 'div'):
        if b == 0:
            raise ZeroDivisionError('division by zero')
        return a / b
    if op in ('%', 'mod'):
        if b == 0:
            raise ZeroDivisionError('modulus by zero')
        return a % b
    if op in ('**', '^', 'pow'):
        return a ** b
    raise ValueError(f"Unknown operation: {op}")


def main():
    print("Simple calculator. Enter 'q' to quit at the first prompt.")
    while True:
        try:
            s = input("Enter number a (or 'q' to quit): ").strip()
            if s.lower() in ('q', 'quit', 'exit'):
                break
            a = float(s)
            b = float(input("Enter number b: ").strip())
            op = input("Enter operation (+ - * / % ** ^): ").strip()
            result = calculate(a, b, op)
            # show ints without trailing .0
            if isinstance(result, float) and result.is_integer():
                print("Result:", int(result))
            else:
                print("Result:", result)
        except ValueError as e:
            print("Invalid input:", e)
        except ZeroDivisionError:
            print("Error: Division or modulus by zero is not allowed.")
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            break
    print("Goodbye.")


if __name__ == '__main__':
    main()












# a = float(input("Enter number a: "))
# b = float(input("Enter number b: "))
# op = input("Choose operation (+, -, *, /, ** for power, xor): ").strip().lower()

# if op == "+":
#     result = a + b
# elif op == "-":
#     result = a - b
# elif op == "*" or op == "x":
#     result = a * b
# elif op == "/":
#     if b == 0:
#         print("Error: Division by zero.")
#         quit()
#     result = a / b
# elif op in ("**", "^"):  # treat ^ as power here
#     result = a ** b
# elif op == "xor":  # real bitwise XOR (integers only)
#     result = int(a) ^ int(b)
# else:
#     print("Unknown operation. Use +, -, *, /, ** (power), or xor.")
#     quit()

# print("Result:", result)
