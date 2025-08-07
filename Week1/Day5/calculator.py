choice = input("Enter Your Choice: '+' , '-' , '/' , '*' :")
num1 = int(input("Enter 1 Number:"))
num2 = int(input("Enter 2 Number:"))

if choice == '+':
    print(num1 + num2)
elif choice == '-':
        print(num1 - num2)
elif choice == '*':
        print(num1 * num2)
elif choice == '/':
        print(num1 / num2)
else:
    print("Invaild Operator") 
    
