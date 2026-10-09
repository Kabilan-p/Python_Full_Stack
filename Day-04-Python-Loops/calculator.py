print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 + num2}")
elif choice == "2":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 - num2}")
elif choice == "3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 * num2}")
elif choice == "4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Invalid choice")