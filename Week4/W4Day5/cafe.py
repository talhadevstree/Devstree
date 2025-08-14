menu = {
     "Pasta" : 220,
     "Burger" : 150,
     "Pizza" : 300,
     "Brownie" : 140,
     "Mojito" :120
}

username = "admin"
password = "admin@123"

print("Welcome to our CAFE: \nWhat You Want to order")
print("1. Pasta : 220 \n 2. Burger : 150 \n 3. Pizza : 300 \n 4. Brownie : 140 \n 5. Mojito : 120 \n Admin ")
total = 0

item_1 = input("Enter item u want to order:")
if item_1 in menu: 
    total += menu[item_1]
    print(f"Your {item_1} added in ur cart")
else:
    print(f"this {item_1} is not available")
    
another_order = input("Want to order Another item Y / N:")
if another_order == 'Y':
    item_2 = input("Enter Your second item:")
    if item_2 in menu:
        total +=menu[item_2]
        print(f"Your {item_2} has been added")
    else:
        print(f"This {item_2} not available")
    print(f"Total order is : {total}")
    

else:
    print("exiting")


