
number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))

print("1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")
operation = int(input("Choose an operation: "))

if operation == 1:
    print("Result: ", number1 + number2)
elif operation == 2:
    print("Result: ", number1 - number2)
elif operation == 3:
    print("Result: ", number1 / number2)
elif operation == 4:
    print("Result: ", number1 * number2)
else:
    print("Please select a valid operation.".upper())
