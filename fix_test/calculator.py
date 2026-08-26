def calculator(a, b, operation):
    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        return a / b

    else:
        return "Invalid operation"


if __name__ == "__main__":
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	operation = input("Enter operation (+, -, *, /): ")
	result = calculator(num1, num2, operation)
	print("Result:", result)