from api.connection import data

current_temp = data.get("main", {}).get("temp")

print(f"Current temperature in London is {current_temp}°C")
