# import json
import requests as rs

api = "https://randomuser.me/api/"
data = rs.get(api)
user = data.json()

first = user["results"][0]["name"]["first"]
last = user["results"][0]["name"]["last"]
print("Name is:", first, last)

print("Gender:", user["results"][0]["gender"])
print("Email:", user["results"][0]["email"])
print("Phone:", user["results"][0]["phone"])
print("Country:", user["results"][0]["location"]["country"])
print("Birth Date:", user["results"][0]["dob"]["date"])
id = user["results"][0]["login"]["username"]
password = user["results"][0]["login"]["password"]
print(f"ID: {id} - Password: {password}")
