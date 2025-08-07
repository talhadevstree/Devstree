import math 

def areaofsquare(side):
    return side * side
def reactangle(length , width):
    return length * width
def triangle(base , height):
    return 0.5 * base * height
def circle(radius):
    return math.pi * (radius**2)

print("AREA CALCULATIONS:")
print(areaofsquare(3))
print(reactangle(3 , 9))
print(triangle(10 ,19))
print(circle(12))

def kelvintofarhenit(kelvin):
    return (kelvin-273.15)* 5/9 + 273.15
def kelvintocelcius(kelvin):
    return kelvin - 273.15
def celciustokelvin(celcius):
    return celcius+273.15
def celciustofarhenit(celcius):
    return (celcius* 5/9 )+ 32
def farhenittocelcius(farhenit):
    return (farhenit-32) * 5/9
def farhenittokelvin(farhenit):
    return (farhenit-32 )*5/9 + 273.15 

print("TEMPERATURE CONVERSION:")
print(kelvintofarhenit(34))
print(kelvintocelcius(12))
print(celciustokelvin(90))
print(celciustofarhenit(120))
print(farhenittocelcius(120))
print(farhenittokelvin(88))
