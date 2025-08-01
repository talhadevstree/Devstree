# #str to int
str1 = "555"
print("From string to integer:",int(str1))

# # #int to float

int1 = 34
print("From Integer to Float:",float(int1))

# # int to string

int2 = "hello"
strv = str(int2)
print("From Integer to String:",strv)


# handle conversion errors
try:
    str0 = "7654"
    print(int(str0))
    print("Convertion successful")
except:
    print("Failed to convert ")