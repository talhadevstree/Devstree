class banka():
    def __init__(self):
        self.balance=0
    def deposit(self , amount):
        self.balance += amount
        print(f"{amount} deposit is added in BankAccount!")
    def withdraw(self , amount):
        if amount > self.balance:
            print("Insufficient fund")
        else:
            self.balance-=amount
            print(f"{self.balance} Amount Successfully withdraw from BankAccount")
    def checkb(self):
        print(f"{self.balance} Your Balance ")
a = banka()
amount = int(input("Enter a despoit you  want to add:"))
a.deposit(amount)
withdraw = int(input("Enter a withdraw you  want to add:"))
a.withdraw(withdraw)
a.checkb()

