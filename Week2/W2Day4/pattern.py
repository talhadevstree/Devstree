print("""
Choose Your option:
    1: 'Triangle'
    2: 'Diamond'
""")

choice = input("Enter Your Choice:")

rows = int(input("Enter Your Number of Rows:"))

if choice == 'Triangle':
    for i in range(rows):
        for j in range(i + 1):
            print("*", end="")
        print()
elif choice == 'Diamond':
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for j in range(rows - 1, 0, -1):
        print(" " * (rows - j) + "*" * (2 * j - 1))
else:
    print("Invalid Choice Try Again!")


  
    