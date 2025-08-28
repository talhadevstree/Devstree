# REST API Consumer:- Create a program that consumes a public API and displays formatted data
import requests
 
# Ask for only the 'name' and 'capital' fields to avoid 400 error
url = "https://restcountries.com/v3.1/all?fields=name,capital"
 
try:
    print("Making API request...")
    response = requests.get(url, timeout=10)
    print("Status code:", response.status_code)
 
    if response.status_code == 200:
        countries = response.json()
        print("Data received. Number of countries:", len(countries))
 
        print("\nShowing first 10 countries and capitals:\n")
        for i, country in enumerate(countries[:10], start=1):
            name = country.get("name", {}).get("common", "Unknown")
            capital = country.get("capital", ["N/A"])[0]
            print(f"{i}. {name}: Capital is {capital}")
    else:
        print("Request failed. Status:", response.status_code)
 
except Exception as e:
    print("An error occurred:", e)
 
 