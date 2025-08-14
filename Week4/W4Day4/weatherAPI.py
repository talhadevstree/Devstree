import requests
import datetime as dt

city = choice = input("Welcome to weather FORCASTING: Which city Weather you want to check:")
api_key = 'e06b9dbdeb5f13f05cb3fcfc4e2c8899'
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")

data = response.json()

while True:
    if choice == data:
        temp = data['main']
        desc = data['weather'][0]
        country = data['sys']
        print(f'Your City :{city}')
        print(f"Current Tempreature of  {city} is : {temp['temp']} C")
        print(f" Description is : {desc['description']}")
        print(f"country is : {country['country']}")
        break
    else :
        print("Invalid operator")