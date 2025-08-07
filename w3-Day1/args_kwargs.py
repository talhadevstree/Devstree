def greet(name):
    return name
print(greet("world"))

def add(*args):
    return max(args)
print(add(1,3,6))

def abcd(**kwargs):
    print("kwargs:", kwargs)
abcd(name="hello")
