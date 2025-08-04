num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

operator = input("Select the operator for your SUM:'+' , '-' , '*' , '/':")

# match(operator):
#     case '+':
#         print(num1+num2)
#     case '-':
#         print(num1-num2)
#     case '*':
#         print(num1*num2)
#     case '/':
#         print(num1/num2)

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 -num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    print(num1/num2)
else:
    print("invalid operator")
