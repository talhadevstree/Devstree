shopping_list = []

while True:
    choice = input("Choice: 'add', 'remove', 'display','update','exit':")

    if choice == 'add':
        item = input("Enter an item to add:")
        if item in shopping_list:
            print("This item aleady in list")
        else:
            shopping_list.append(item)
            print({item},"Added")

    elif choice == 'remove':
        removeitem = input("Enter an item to remove from list:")
        if removeitem in shopping_list:
            shopping_list.remove(removeitem)
            print({removeitem},"has been remove successfully!")
        else:
            print("Item not in List")

    elif choice == 'display':
        print(shopping_list)

    elif choice == 'exit':
        break
    else:
        print("Invalid operator")