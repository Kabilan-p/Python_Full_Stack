num = int(input("Enter a number for the table: "))

print(f"\n--- Forward Table for {num} ---")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print(f"\n--- Reverse Table for {num} ---")
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num * i}")