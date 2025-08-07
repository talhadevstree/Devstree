class banka():
    def __init__(self):
        self.balance = 0
    def deposit(self , amount):
        self.balance += amount
        print(f"{amount} is deposit")
    def withdraw(self , amount):
        if amount > self.balance:
            print("Insufficient fund")
        else:
            self.balance -=amount
            print(f"{self.balance}")
    def checkb(self):
        print(f"{self.balance}")
a = banka()
a.deposit(1000)
a.withdraw(500)
a.checkb()

