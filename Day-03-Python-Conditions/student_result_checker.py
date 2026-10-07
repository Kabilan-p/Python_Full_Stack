student_name = input("Enter your name: ")
mark1 = int(input("Enter your mark1: "))
mark2 = int(input("Enter your mark2: "))
mark3 = int(input("Enter your mark3: "))

# 1. Check for invalid marks first
is_valid = (mark1 < 0 or mark1 > 100 or mark2 < 0 or mark2 > 100 or mark3 < 0 or mark3 > 100)

if is_valid:
    print("Invalid marks")
else:
    print("STUDENT_NAME: ", student_name)
    
    total = mark1 + mark2 + mark3
    print("Total out of 300: ", total)
    
    average = total / 3
    print("Average: ", average)
    
    # Highest mark using conditions without max()
    high = mark3
    if mark1 >= mark2 and mark1 >= mark3:
        high = mark1
    elif mark2 >= mark1 and mark2 >=mark3:
        high = mark2
    print("Highest mark: ", high)
    
    # 3 & 4. Pass/Fail check (all marks must be at least 35)
    if mark1 < 35 or mark2 < 35 or mark3 < 35:
        print("Fail")
    else:
        print("Pass")
        # 5. Assign grade using the average
        if average >= 90:
            print("Grade: A")
        elif average >= 75:
            print("Grade: B")
        elif average >= 50:
            print("Grade: C")
        else:
            print("Grade: D")