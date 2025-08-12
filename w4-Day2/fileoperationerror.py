#FileNotFoundError

try:
    with open('file.py' , 'r') as r:
        content = r.read()
        print(content)
except FileNotFoundError:
    print("File Not Found!")

#PermissionError

try:
    with open('secret.text', 'r') as r:
        content = r.read()
        print(content)
except PermissionError:
    print("You don't have permission to Read / Write this")

#IOError

try:
    with open('secret.text' , 'w') as f:
        f.write("Hello World")
except IOError:
    print("Something Went Wrong With Input / Output Operations!")
