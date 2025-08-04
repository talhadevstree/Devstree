phonebook = []
while True:
    choose = input("You Want to Store 'Data' or 'Display':")

    if choose == 'Data':
        name = input("Enter a Name:")
        phone = int(input("Enter a Number:"))
        phonebook.append(name )
        phonebook.append(phone)
        print("########################")
        print("Item Added in Phone Book")
        print("########################")
    elif choose == 'Display':
        print(phonebook)


    choice = input("You want to co continue? : 'Y' or 'N':")

    if choice == 'Y':
        print("continue")
    elif choice == 'N':
        print("exiting")
        break
