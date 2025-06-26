# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
print("\nArithmetic Operations Results:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# To avoid division by zero
if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2}")
    print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
    print(f"Modulus: {num1} % {num2} = {num1 % num2}")
else:
    print("Division, floor division, and modulus operations not possible (division by zero).")

print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")
