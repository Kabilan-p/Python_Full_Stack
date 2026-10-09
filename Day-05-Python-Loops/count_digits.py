number = int(input("ENTER THE NUMBER : "))
digit=0
if number < 0:
    print("Invalid input")
elif number==0:
    digit=1
else:
      while number > 0:
           number//=10
           digit=digit+1
print(f"TOTAL COUNT OF DIGITS {digit}")           