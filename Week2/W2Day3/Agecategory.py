# Classify people into age categories (child, teen, adult, senior) with nested conditions

# Child	    0 to 12 years
# Teen	    13 to 19 years
# Adult	    20 to 59 years
# Senior	60 years and above

name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))

if age >= 60:
    print(f"{name} You are in Senior category")
elif age >=20 :
    print(f"{name} You are in Adult category")
elif age >=13:
    print(f"{name} You are in Teen category")
elif age >=0 :
    print(f"{name} You are in Child category")
else:
    print("none")
