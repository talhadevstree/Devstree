from api import data
temp = data.get("main", {}).get("temp")
print(f"Current temperature is {temp}°C")
