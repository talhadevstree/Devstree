import requests
from api import weatherapi

city = "london"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherapi}&units=metric"

response = requests.get(url)
data = response.json()
print(data)