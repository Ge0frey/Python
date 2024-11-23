num1 = float(input("Num1: "))
operator = input("operator: ")
num2 = float(input("Num2: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
   result = num1 - num2
elif operator == '/':
    result = num1 / num2
elif operator == '*':
   result = num1 * num2

print(f"{result}")
# print(f"difference: {result}")
# print(f"divide: {result}")
# print(f"multiply: {result}")
