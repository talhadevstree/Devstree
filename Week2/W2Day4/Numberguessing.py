secret_number = 70
while True:
    print("Welcome to GUSSING GAME!!")
    num = int(input("Enter a secret number:"))
    if num == secret_number:
        print("You Guess Right Number")
        break
    elif abs(num - secret_number) <= 5:
        print("Too Close Try Again")
    elif num > secret_number:
        print("HINT : You Enter Number is too higher!! ")
    elif num < secret_number:
        print("HINT : You Enter Number is too lower!! ")
    else:  
        print("Invalid Operator!")