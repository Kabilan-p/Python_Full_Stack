age = int(input("ENTER YOUR AGE : "))
if age < 0:
    print("INVALID AGE")
elif age >= 18:
    print("ELIGIBLE FOR VOTE")
else:
    print("NOT ELIGIBLE FOR VOTE")