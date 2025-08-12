#custom Exception
class InsufficientFundsError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

class MinimumBalanceError(Exception):
    pass

#banking function
def withdraw(amount , balance, minimum_balance):
    if amount < 0:
        raise NegativeAmountError("Amount cannot be negative")
    if amount > balance:
        raise InsufficientFundsError("You dont have balance to withdraw!")
    if balance - amount < minimum_balance :
        raise MinimumBalanceError("Withdraw would react minimum balance limit")
    balance -=amount
    return balance

def deposit(balance,amount):
    if amount < 0:
        raise NegativeAmountError("Deposit Amount cannot be Negative!")
    balance +=amount
    return balance

def main():
    balance = 5000
    minimum_balance = 1000

    while True:

        choice = input("Enter your choice: \n  'Deposit' \n  'withdraw' \n  'checkcurrentbalance' \n")
        if choice == 'withdraw'.lower():
            try:
                amount = int(input("Enter amount to withdraw"))
                balance = withdraw(amount , balance, minimum_balance)
                print(f"Withdraw successful. You have {balance} balance")
            except(InsufficientFundsError , NegativeAmountError , MinimumBalanceError) as e:
                print(f"{e}")

        elif choice == 'deposit'.lower():
            try:
                amount = int(input("Enter amount to deopsit"))
                balance= deposit(balance , amount)
                print(f"amount deposit {amount} and current balance is {balance}")
            except  NegativeAmountError as e:
                print(f"{e}")

        elif choice == 'checkcurrentbalance':
            try:
                print(f"{balance}")
            except InsufficientFundsError as e:
                print(f"{e}")
        else:
            print("Invalid Operator")
main()
