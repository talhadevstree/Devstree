# Order Management app in python with various function and With Database

import sqlite3

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

total = []
adminid = "admin"
adminpass = "admin@123"

cursor.execute("""CREATE TABLE IF not  exists products(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   category TEXT,
                   price REAL,
                   stock INTEGER)"""
)

cursor.execute("""CREATE TABLE IF not exists orders(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_name TEXT,
                   price REAL,
                   status TEXT)"""
)

while True:
    print("Welcome to our shop:")
    print("Select operation to perform:")
    choice = input(
        "1. Place order \n 2. View Products \n 3. Search Products \n 4. View My order \n 5. Login as admin \n 6. Exit \n"
    )

    if choice == "1":
        productname = input("Enter product name to add:")
        cursor.execute("SELECT id , name , price , stock FROM products WHERE name = ?" , (productname,))
        p =  cursor.fetchone()
        if p and p[3]>0:
            qty = int(input("Enter the quantity:"))
            if qty <= p[3]:
                cursor.execute("INSERT INTO orders (product_name , price , status ) VALUES (? , ? , ?)" , (p[1] , p[2]*qty ,"Pending"))
                cursor.execute("UPDATE products SET stock  = stock - ? WHERE id=?" , (qty, p[0]))
                connection.commit()
                print("Order placed!")
            else:
                print("Not enough stock!")
        else:
            print("product not available or out of stock!")
        
    elif choice == "2":
        cursor.execute("SELECT * from products")
        for orders in cursor.fetchall():
            print(orders)
            
    elif choice == "3":
        searchpro = input("Enter product name to search:")
        cursor.execute("SELECT * from products WHERE name LIKE ? ", ('%' + searchpro + '%',),)
        result = cursor.fetchall()
        if result:
            for product in result:
                print(product)
        else:
            print("no product found")
            
    elif choice == "4":
        cursor.execute("SELECT * FROM orders")
        order = cursor.fetchall()
        if order:
            for row in order:
                print(row)
        else:
            print("No order found!")
                
    elif choice == "5":
        id = input("Enter admin id:")
        pasw = input("Enter admin password")
        
        if id == adminid and pasw == adminpass:
            print("Login success")
            print("Enter Your choice : ")
            choice = input("1. update products  2. Add products ")
            
            
            if choice == '1':
                proname = input("Enter product name")         
                cursor.execute('SELECT * from products')
                products = cursor.fetchone()
                
                if products:
                    print("Which this do you want to update :")
                    choice = input('1. product name \n  2. product category \n  3. product price \n  4. product stock \n ')
                    
                    if choice == '1':
                        upname = input("Enter product name to update:")
                        cursor.execute('UPDATE from products SET name = ? WHERE name = ?' , (upname , proname),)
                        print("product name has been updated")
                        connection.commit()
                        
                    elif choice == '2':
                        upcategory = input("Enter product category to update:")
                        cursor.execute('UPDATE products SET category = ? WHERE name = ?' , (upcategory , proname),)
                        print("product category has been updated")
                        connection.commit()
                        
                    elif choice == '3':
                        upprice = input("Enter product price to update:")
                        cursor.execute('UPDATE from products SET price = ? WHERE name = ?' , (upprice , proname),)
                        print("product price has been updated")
                        connection.commit()
                        
                    elif choice == '4':
                        upstock = input("Enter product stock to update:")
                        cursor.execute('UPDATE from products SET stock = ? WHERE name = ?' , (upstock , proname),)
                        print("product stock has been updated")
                        connection.commit()
                else:
                    print("Invalid operator!")
                                        
            if choice == '2':
                prodname = input("Enter product name :")
                procat = input("Enter product category :")
                proprice = input("Enter product price :")
                prostock = input("Enter product stock :")
                
                cursor.execute("INSERT INTO products (name , category , price , stock) VALUES ( ? , ? , ? , ?)", (prodname , procat , proprice , prostock),)
                print("Product Added successfully")
                connection.commit()
        else:
            print("Error While Login")


        connection.commit()
        connection.close()
