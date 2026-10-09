number = int(input("ENTER THE NUMBER : "))

if number < 0:
    print("Invalid input")
else:
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    print(f"REVERSED NUMBER : {reverse}")