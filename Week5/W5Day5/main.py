import requests
import sqlite3

connection = sqlite3.connect("myexpense.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE if not exists expense
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               income REAL ,
               expense REAL,
               balance REAL,
               transcation TEXT)
               """)

print("Welcome to Personal Expense Tracker 💸💸")


while True:
    choice = input("Enter your choice:\n 1. Add Income\n 2. Add expense\n 3. View Transcation\n 4. View Balance\n 5. Get Currency Exchange Rate\n 6. Get stock price\n 7. Exit\n")
    
    if choice == "1":
        try:
            income = int(input("Enter your income:"))
            desc = input("Enter your income source : salary or Bouns?")
            cursor.execute("INSERT INTO expense (income , transcation) VALUES (?, ?)", (income,f"Income is {desc}"))
            print("Income added in a database")
            connection.commit()
        except:
            print("Failed to add Income")
            
    elif choice =="2":
        try:
            expense = int(input("Enter your expense:"))
            desc = input("Enter your expense source : rent or grocery?")
            cursor.execute("INSERT INTO expense (expense , transcation) VALUES (? , ?)" , (expense,f"expense is{desc}"))
            print("Expense added in a database")
            connection.commit()
        except:
            print("Failed to add expense")
            
    elif choice =="3":
        cursor.execute("SELECT transcation FROM expense WHERE transcation IS NOT NULL")
        transcations = cursor.fetchall()
        if transcations:
            print("\n Your transcations are:")
            for tsx in transcations:
                print(f" - {tsx[0]}")
        else:
            print("No transcation found")
            
    elif choice =="4":
        cursor.execute("SELECT SUM(income) , SUM(expense) FROM expense")
        income , expense= cursor.fetchone()
        income = income or 0
        expense = expense or 0
        balance = income - expense
        print(f"Your balance is {balance}")        
    elif choice =="5":
        currencyapi = ""
    elif choice =="6":
        stockapi = ""
    elif choice =="7":
        print("Quit 👋")
        connection.commit()
        break
    else:
        print("Invalid operator")

        connection.commit()
        connection.close()