student_name = {}

while True:
    choice = input("Enter Your Choice: 'add' , 'analyze':")
    
    if choice == 'add':
        name = input("Enter student name:")
        grade = int(input("Enter student Grade:"))
        if name in student_name:
            print("Alreaday in list") 
        else:
            student_name[name]= grade
            print(f"Student Added -->{name}")
    elif choice == 'analyze':
        name = input("Enter student name to analyze:")

        if name in student_name:
            grade = student_name[name]
            print(f"grade is {grade}")

            if grade > 90:
                print('A')
            elif grade >=80:
                print('B')
            elif grade >=70:
                print('c')
            elif grade >=60:
                print('D')
            else:
                print('F')
        else:
            print("Cannot find student?")
    else:
        print("Invalid operator")
            
