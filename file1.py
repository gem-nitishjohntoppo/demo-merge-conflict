def divide_numbers(a, b):
    try:
        return a / b  # Exception handling added
    except ZeroDivisionError:
        return "Error: Division by zero"

result = divide_numbers(10, 0)
print("Result:", result)