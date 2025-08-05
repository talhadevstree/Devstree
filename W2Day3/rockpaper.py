while True:
    player1 = input("Enter your move:'stone' , 'Paper' , 'Scissor':")
    player2 = input("Enter your move:'stone' , 'Paper' , 'Scissor':")

    if player1 == player2:
        print("Tie! Play Another Game To WIN!")
    elif player1 == 'stone'and player2 == 'paper':
        print("Player2 WIN")
    elif player1 == 'paper'and player2 == 'stone':
        print("Player1 WIN")
    elif player1 == 'scissor'and player2 == 'paper':
        print("Player1 WIN")    
    elif player1 == 'paper'and player2 == 'scissor':
        print("Player2 WIN")
    elif player1 == 'scissor'and player2 == 'stone':
        print("Player2 WIN")
    elif player1 == 'stone'and player2 == 'scissor':
        print("Player1 WIN")
    else :
        print("Invalid Choice! Please try Again")
        continue

    choice = input("Want to Restart Your Game? 'Y' , 'N':")

    if choice == 'Y':
        print("continue")
        # continue
    elif choice == 'N':
        break
    else:
        print("Invaid operator")
