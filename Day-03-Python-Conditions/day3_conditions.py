# age = int(input("Enter your age: "))

# if age >= 18:
#     print("ADULT")
# else:
#     print("Under 18")


# num=int(input("ENTHER THE NUMBER"))
# if num%2==0:
#     print("EVEN")
# else:
#     print("ODD")    

##JOB ELIGIBILTY CHECK 

# age=int(input("ENTER THE AGE: "))
# test_score=int(input("ENTER THE mark: "))
# if age<18 or test_score<0 or test_score>100:
#     print("NOT ELIGIBLE or Inavlid input")
# elif test_score>=70:
#     print("SELECTED")
# else:
#     print("NEED PRACTICE") 



    
# print("1.Kilometers to miles")
# print("2. Celsius to Fahrenheit")
# choice=input("ENTER YOUR CHOICE:")
# if choice==1:
#     distance=float(input("ENTEHR DISRANCE IN KILO METRERS"))
#     miles=distance*0.621371
#     print("MILES COVERED:",miles)
# elif choice==2:
#         temperature=float(input("Enter the  celsius : "))
#         fahrenheit = (temperature * 9 / 5) + 32
#         print(f"THE FARENHEIT FOR THE {temperature} is {fahrenheit}")
# else:
#      print("IVAID CHIOCE")

user_name=input("ENTER THE USER NAME: ")
password=input("ENTER THE PASSWORD: ")
is_valid=( user_name=="kabil" and password=="python123")
if not is_valid:
    print("Login failed")
else:
    role=input("ENTER YOUR ROLE: ")
    if role=="admin":
        print("ADMIN DASHBORAD")
    else:
        print("USER DASHBOARD")