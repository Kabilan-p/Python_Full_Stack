number = int(input("ENTER THE NUMBER : "))
couunt=0
if number < 0:
    print("Invalid input")
else:
    reverse = 0
    while number > 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number = number // 10
            couunt=couunt+1
print("REVERSE: ",reverse)
print("COUNT: ",couunt)        