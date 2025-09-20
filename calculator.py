num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /, %, **): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error! Modulo by zero."
elif operator == "**":
    result = num1 ** num2
else:
    result = "Invalid operator."

print(f"Result: {result}")
