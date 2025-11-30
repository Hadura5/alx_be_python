def perform_operation(num1, num2, operation):
    operations = {
        'add': num1 + num2,
        'subtract': num1 - num2,
        'multiply': num1 * num2,
        'divide': num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."
    }
    return operations.get(operation, "Error: Invalid operation.")