n = int(input("ENTER THE NUMBER: "))
i = 1
fact = 1

if n < 0:
    print("Invalid input")
else:
    while i <= n:
        fact *= i
        i += 1

    print(f"FACTORIAL OF {n} is {fact}")