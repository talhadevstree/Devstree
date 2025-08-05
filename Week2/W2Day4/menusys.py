menu_system = []

while True:
    choice = input("""Enter Your Choice"
 1. Add Item
 2. Display Item
 3. Remove Item
 4. Search Item
 5. update Item
 6. Exit
""")
    
    if choice == '1': #add
        numberitem = int(input("How many items you want to add"))
        for i in range(numberitem):
            item = input(f"Enter Item {i+1} to Add in menu System:")
            if item in menu_system:
                print("Item Already in Menu Please Try Again")
                continue
            else:
                menu_system.append(item)
                print("Item added in menu system!")
        

    elif choice == '2': #display
        if not menu_system:
            print("Menu List is Empty Nothing to Display ")
            continue
        if item in menu_system:
            print(menu_system)
        else:
            print("Nothing to Display in menu system Please Add 1 item to see")

    elif choice == '3': #remove
        if not menu_system:
            print("List is empty nothing to remove!")
            continue
        removeitem = int(input("How many item want to remove?"))
        for i in range(removeitem):
            item = input(f"Enter to {i+1} remove:")        
            if item in menu_system:
                    menu_system.remove(item)
                    print("Your item has been remove successfully ")
            else:
                    print("Item not in menu system. Please Try Again!")

    elif choice == '4': #search
        item = input("Enter item to search:")
        if menu_system:
            if item in menu_system:
                print(f"Your Item Has been found --->>> {item}")
            else:
                print("Item not Found! Please Try Again")

    elif choice == '5': #update
        updateitem =input("Enter item to update")
        if updateitem in  menu_system:
                index = menu_system.index(updateitem)
                name = input("Chnage name")
                menu_system[index]= name
                print("item updated")
        else:
            print("Item not in list")

    elif choice == '6':
        break
    else:
        print("Invalid Choice!")