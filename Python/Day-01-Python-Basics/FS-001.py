# Write a program that:
# 1. Asks for the customer’s name.
# 2. Asks for the quantities of two purchased products as whole numbers.
# 3. Adds the quantities.
# 4. Prints the customer’s name and total quantity with clear labels.
# 5. Uses meaningful variable names.
# Test twice: first with quantities 3 and 2, then with 0 and 5.

name=input("Enter your name: ")
qty_product1=int(input("Enter the quantity of product 1: "))
qty_product2=int(input("Enter the quantity of product 2: "))
total_quantity=qty_product1+qty_product2
print("Customer Name:", name)
print("Total Quantity:", total_quantity)