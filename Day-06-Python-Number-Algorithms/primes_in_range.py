start = int(input("Enter start: "))
end = int(input("Enter end: "))

if start > end:
    print("Invalid range")
else:
    for number in range(start, end + 1):
        # Skip numbers below 2
        if number < 2:
            continue
            
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
                
        if is_prime:
            print(number)