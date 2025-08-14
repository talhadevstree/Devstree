while True:
    try:
        num1 = int(input("Enter your value:"))
        num2 = int(input("Enter your value:"))
    except ValueError:
            print("Please Enter Number Only!!")
            continue
    operator = input("Select operation to Perform: \n 1 : + \n 2 : - \n 3 : * \n 4 : /  \n or q (quit:) : \n ")
    
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("Cannot Divide BY 0")
    elif operator == 'q':
        print("Exiting!!!")
        break
    else:
        print("Invalid operator!")
        
    choice = input("Want to continue : (Yes/ No):")
    if choice != 'Yes':
        break

        
