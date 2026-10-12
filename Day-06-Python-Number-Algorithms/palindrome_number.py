number = int(input("Enter a number: "))
original = number
rev = 0

if number < 0:
    print("Invalid input")
else:
    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")