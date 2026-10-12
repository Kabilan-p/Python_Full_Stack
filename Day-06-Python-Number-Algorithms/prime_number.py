number = int(input("Enter a number: "))

if number < 2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print("Prime")
    else:
        print("Not prime")