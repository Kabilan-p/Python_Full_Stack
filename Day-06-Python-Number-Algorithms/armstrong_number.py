number = int(input("Enter a number: "))
original = number

if number < 0:
    print("Invalid input")
else:
    # 1. First loop: Count the digits (treating 0 as one digit)
    count = 0
    temp = number
    
    if temp == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp = temp // 10

    # 2. Reset working copy to the original number
    temp = original
    total = 0

    # 3. Second loop: Extract each digit and accumulate power
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp = temp // 10

    # Edge case handler for 0 (since 0 > 0 skips the second loop)
    if original == 0:
        total = 0

    # 4. Compare total with the original number
    if original == total:
        print("Armstrong")
    else:
        print("Not Armstrong")