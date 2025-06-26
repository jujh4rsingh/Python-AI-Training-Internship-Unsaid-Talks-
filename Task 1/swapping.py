# Input two numbers
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

# Swapping without a third variable
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
