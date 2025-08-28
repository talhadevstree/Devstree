def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Not divide by 0")

def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Out of index")

numbers = [1, 2, 3]
print("Division:", divide(10, 0))   # ZeroDivisionError
print("Item:", get_item(numbers, 5))  # IndexError



#Fixed code::

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Error: Index out of range")
        return None

numbers = [1, 2, 3]
print("Division:", divide(10, 0))     
print("Item:", get_item(numbers, 5))   
