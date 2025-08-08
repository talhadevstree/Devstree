def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n-1)
print(factorial(5))

def fibonacci(n):
    if n <=0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
num = int(input("Enter your number:"))
for i in range(num):
    print(fibonacci(i),end=" ")

