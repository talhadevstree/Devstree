from dotenv import load_dotenv
import os
import json

load_dotenv()

API = os.getenv("API")
DB_PASS = os.getenv("DB_PASS")

#config file
try:
    with open("a.json", "r") as r:
        data = json.load(r)
        print("App name", data["app"])
        print("App Version:", data["version"], "v")
        print("Database Host:", data["database"]["host"])
        print("Database User:", data["database"]["user"])
        print("Database Port:", data["database"]["port"])
        print(f"API : {API}")
        print(f"Database Password : {DB_PASS}")
except FileNotFoundError as e:
    print("This File you can access is not found!!")
