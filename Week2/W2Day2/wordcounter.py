words = "hello world this is a sample paragraph".split()

dir = {}

for n in words:
    if n in dir:
        dir[n] =+1
    else:
        dir[n]=1
print(dir)
