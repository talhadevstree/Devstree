from services.currency import get_currency_rate
from services.stock import get_stock
from services.operations import add_income , add_expense , view_transcation , view_balance
from db import init_db

init_db()

while True:
    print("Welcome to Personal Expense Tracker 💸💸")
    
    choice = input(
        "Enter your choice:\n 1. Add Income\n 2. Add expense\n 3. View Transcation\n 4. View Balance\n 5. Get Currency Exchange Rate\n 6. Get stock price\n 7. Exit\n"
    )
    
    if choice =="1":
        income = int(input("Enter your income:"))
        desc = input("Enter your source : (Salary or Bouns) :")
            
        msg = add_income(income , desc)
        print(f"Income added : {msg}")
            
    elif choice == "2":
        expense = int(input("Enter your expense"))
        desc = input("Enter your source : (rent or food) :")
            
        balance = add_expense(expense , desc)
        print(f"Expense added : {balance} ")
        
            
    elif choice == "3":
        print(view_transcation())
        
        
    elif choice == "4":
        print(view_balance())
        
    elif choice =="5":
        base = input("Enter the base currency:").upper()
        current = input("Enter the currency to convert:").upper()
        amount = int(input(f"Enter the amount to convert in {base}"))
        print(get_currency_rate(base , current , amount))
        
    elif choice =="6":
        symbol = input("Enter the stock symbol:").upper()
        print(get_stock(symbol))
        
    elif choice=="7":
        print("Quit")
        break
    else:
        print("Invalid operator")
    
