# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# c=int(input("enter the third number"))
# if a>=b and a>=c:
#     print(f"{a} is greater")
# elif b>=a and b>=c:
#     print(f"{b} is greater")
# else:
#     print(f"{c} is greater")


mark= int(input("ENTER YOUR MARK : "))
if mark<0 or mark>100:
    print("IVALID SCORE")
elif mark>=90:
    print("A")
elif mark>=75:
    print("B")
elif mark>=50:
    print("C")
else:
    print("fail")
