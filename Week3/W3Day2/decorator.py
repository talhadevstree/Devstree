import time
#time decorator 
def time_decorator(funca):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = funca(*args , **kwargs)
        end = time.time()
        print(f"{funca.__name__} run in {end  - start:.2f} {kwargs} seconds ")
        return result
    return wrapper
@time_decorator
def slow(name):
    time.sleep(2)
    print('\n')
    print("### Time Decorator is Running ###")
    print("finished this in 12hr")

slow(name="world")

#logging decorator

def logging_decorator(func):
    def wrapper(*args , **kwargs):
        print("\n")
        print("### Logging Decorator is Running ###")
        print(f"function calling: {func.__name__} ")
        print(f"Argument calling: {args} , {kwargs}")
        result = func(*args , **kwargs)
        print(f"result:{result}")
        return result
    return wrapper
@logging_decorator
def add(a,b, name):
    return a+b and name
add(1,4 , name="hello")

