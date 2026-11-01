first_number = float(input("Enter the first number: "))
operation = input("Choose an operation (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        print("Error: cannot divide by zero.")
        raise SystemExit(1)
    result = first_number / second_number
else:
    print("Error: unsupported operation.")
    raise SystemExit(1)

print("Result:", result)