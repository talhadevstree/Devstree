phonebook = {}
while True:
    choose = input("You Want to Store 'Data' or 'Display','search', 'remove' :")

    if choose == 'Data':
        name = input("Enter a Name:")
        phone = int(input("Enter a Number:"))
        phonebook[name] = phone
        print("########################")
        print("Contact Added in Phone Book")
        print("########################")

    elif choose == 'Display':
            if phonebook:
                for name , phone in phonebook.items():
                    print("########################")
                    print(f"Name: {name} , Phone:{phone}")
                    print("########################")
            else:
                print("Phonebook is empty nothing to see anything!")
                
    elif choose == 'search':
            searchname = input("Enter name to search:")
            if phonebook:
                if searchname in phonebook:
                    for name  in phonebook:
                        phonebook[name]= searchname
                        print(f"Name is found {name}")
            else:
                        print("name not found")
    
    elif choose == 'remove':
        removerecord = input("Enter name to remove:")
        if phonebook:
            if removerecord in phonebook:
                del phonebook[removerecord]
                print(f"{removerecord} has been deleted")
        else:
                print("No record found!")

    else:
        print("Invalid operator! Please Try Again")
        continue

    choice = input("You want to co continue? : 'Y' or 'N':")

    if choice.lower().upper() == 'Y':
        print("continue")
    elif choice.lower().upper() == 'N':
        print("exiting")
        break 
        
